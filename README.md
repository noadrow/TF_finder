
# Description:
 This script search for patterns in fasta file format
 It creates bed and fasta files for each sequence that has that pattren
 
## Required packases:
1. python 3
2. python pacakes: Bio, re

## Please Note:
 This script takes only the file name "fileToSearch"
 This script search and create files that located at the same folder of the script
 This script uses regx for special nuclotide notation (such as N) you can place all nucletodies under []
 
## Example:
 For example there is a file called GFR_positive.fa
 you can run the following command in the terminal: 
``` bash
python SearchForSeq.py GFR_positive TGA[AG]TCA  ATTCC CCGGAA
```

format:
python SearchForSeq.py "file name" "Pattren 1" ..... "Pattren n"

## output:  
this file containes list of records that their names is their position in the following format:
"chromosome number": "first nucleotide position" - "last nucleotide position"
 
After using this script it well create 6 files
for each pattren there is a bed file an a fasta file
the naming of the files are in the following format:
"name of origin file" _ "pattren" 


