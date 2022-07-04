from Bio import SeqIO
from Bio import AlignIO
import os
import re

# This script search for patterns in fasta file format
# It creates bed and fasta files for each sequence that has that pattren
# Please Note:
# This script takes only the file name "fileToSearch"
# This script search and create files that located at the same folder of the script
# This script uses regx for special nuclotide notation (such as N) you can place all nucletodies under []

dfs = []
files = []
searchlist = []
pattrenList = []
fileToSearch = "GFR_positive"

def searchSeq(x):
    for i in x:
        dfs.append(["",""])
        files.append([open(fileToSearch+"_"+i+".fa","w"),open(fileToSearch+"_"+i+".bed","w")])
        
        pattrenList.append(re.compile(i))
   
searchSeq(['TGA[AG]TCA','ATTCC','CCGGAA'])

print (files)
print (dfs)

for (file, df, pattern) in zip(files,dfs,pattrenList):
    for seq_record in SeqIO.parse(fileToSearch+".fa", "fasta"):
            
        seqId = seq_record.id
        seq = str(seq_record.seq).upper()

        if pattern.findall(seq):
                    
            start = int(seqId.split(":")[1].split("-")[0])+pattern.search(seq).start()
            end = int(seqId.split(":")[1].split("-")[1])-len(seq)+pattern.search(seq).end()

            df[0] += f"{seqId}\n{seq}\n"
            chrx = seqId.split(":")[0]
            df[1] += f"{chrx}\t{str(start)}\t{str(end)}\n"

    file[0].write(df[0])
    file[1].write(df[1])
    file[0].close()
    file[1].close()

