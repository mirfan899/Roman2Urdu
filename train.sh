#!/bin/bash

MARIAN=/home/plp/marian/build/marian
$MARIAN \
    --train-sets data/makhzan_roman_cleaned.txt data/makhzan_urdu_cleaned.txt \
    --type transformer \
    --vocabs data/vocab.ro.yml data/vocab.ur.yml \
    --model model.npz

