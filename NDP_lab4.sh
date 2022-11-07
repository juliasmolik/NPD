#!/bin/bash

# downloading files in fasta format
wget -nc https://ftp.ncbi.nlm.nih.gov/genomes/Viruses/MonkeyPox.fn
wget -nc https://ftp.ncbi.nlm.nih.gov/genomes/Viruses/MonkeyPox2.fn

# names of downloaded files
FILE1=MonkeyPox.fn
FILE2=MonkeyPox2.fn

# number of sequences in downloaded files
monkeypox_number1=$( cat "$FILE1" | grep -o ">" | wc -l)
monkeypox_number2=$( cat "$FILE2" | grep -o ">" | wc -l)

echo "Liczba sekwencji w pliku "$FILE1" wynosi $monkeypox_number1"
echo "Liczba sekwencji w pliku "$FILE2" wynosi $monkeypox_number2"

# retrieving a specific sequence from the downloaded files 
# and saving it to a new file

awk '
    /1899344314/ {f = 1; print; next}   # if the keyword is found, set the flag,
                                                #    print the line and continue with the next line
    f {                                         # if the flag is set
        if (/^>/) f = 0                         #    if next ">" is found, reset the flag
        else print                              #    otherwise print the line
    }
' "$FILE1" > out1.txt

awk '
    /661921128/ {f = 1; print; next}   # if the keyword is found, set the flag,
                                                #    print the line and continue with the next line
    f {                                         # if the flag is set
        if (/^>/) f = 0                         #    if next ">" is found, reset the flag
        else print                              #    otherwise print the line
    }
' "$FILE2" > out2.txt

# finding differences between two saved sequences
diff out1.txt out2.txt