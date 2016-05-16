#!/bin/bash
# Transform dic.:
# ㄡ -> 喔
echo "Removing redundant symbols"
cat train.tsv | 
tr ',~./@#$%^&*()_' ' ' |
tr '-' ' ' | tr '+' ' ' | tr '=' ' ' |
tr '{}[]|\:;<>' ' ' | tr '[a-z]' '[A-Z]' > train_.tsv
python preprocess.py train_.tsv
rm train_.tsv

cat test.tsv | 
tr ',~./@#$%^&*()_' ' ' |
tr '-' ' ' | tr '+' ' ' | tr '=' ' ' |
tr '{}[]|\:;<>' ' ' | tr '[a-z]' '[A-Z]' > test_.tsv
python preprocess.py test_.tsv
rm test_.tsv
