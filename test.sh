#!/bin/bash

DECODER=/home/plp/marian/build/marian-decoder
$DECODER -m model.npz -v data/vocab.ro.yml data/vocab.ur.yml --devices 0 < input.txt
echo "mukammal press release ka matan darj zail hai" | $DECODER -c model.npz.decoder.yml > output.txt
