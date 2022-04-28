### Parallel Corpus
Link contains multiple datasets for this task
```text
https://opus.nlpl.eu/index.php
```

### Corpus
I'm using `makhzan` repository and `ijunoon` dictionary to convert urdu to roman and later use it for transliertaion using
`marian` tool.
Clone `makhazan` repository
```shell
git clone https://github.com/zeerakahmed/makhzan.git
```

### Data Generation.
Data is generated from `makhzan` xml files and only `<p>` is extracted.
```shell
python data_generation.py
```
It will create a file in data directory named `makhzan.txt` for later use.


### Urdu to Roman Conversion
I'm using `ijunoon.com` to get the Roman from Urdu text. Here is the script I'm using
```shell
python scrape.py
```
It uses `makhzan_urdu.txt` and reads line by line and get the possible roman transliteration and saved it. It creates two
files i.e. `makhzan_urdu.txt` and `makhzan_roman.txt` for line by line transliteration.

### Preprocessing
Preprocessing script cleans up the junk from Urdu and as well as Roman text files.
```shell
python preprocessing.py
```
It reads the `makhzan_urdu.txt` and `makhzan_roman.txt` files and cleans up the text and generates two new files.
`makhzan_urdu_cleaned.txt` and `makhzan_roman_cleaned.txt`.

### Training.
Now we are ready to use the cleaned files for training the model. We need to build the vocabulary files for both Urdu and
Roman texts.
```shell
./marian-vocab < makhzan_urdu_cleaned.text > vocab.ur.yml
./marian-vocab < makhzan_roman_cleaned.text > vocab.ro.yml
```

Now starts training.
```shell
MARIAN=/home/plp/marian/build/marian
$MARIAN \
    --train-sets data/makhzan_roman_cleaned.txt data/makhzan_urdu_cleaned.txt \
    --type transformer \
    --vocabs data/vocab.ro.yml data/vocab.ur.yml \
    --model model.npz
```

Now test the model
```shell
DECODER=/home/plp/marian/build/marian-decoder
$DECODER -m model.npz -v data/vocab.ro.yml data/vocab.ur.yml --devices 0 < input.txt
echo "mukammal press release ka matan darj zail hai" | $DECODER -c model.npz.decoder.yml > output.txt
```