#!/home/xuzhongtian/anaconda3/bin/python
# coding=utf-8
'''
Author: xuzhongtian
LastEditors: Xu Zhongtian
email: xuzhongtian11@163.com
github: https://github.com/BiocompZTXu
Date: 2021-03-21 22:56:54
LastEditTime: 2021-03-22 00:55:39
motto: Still water run deep
Description: Modify here please
FilePath: /0.temp/sRNAs_collapse2unique.py
'''

import sys
import os 

#df getParse():
#    '''
#    Using argpaser to parse the input parameters
#    '''
#    parser = argparse.ArgumentParser(description="Collapse the identical sRNAs to unque")
#    parser.add_argument('-l','--minlength',type=int, nargs=1, help="minimal value of the length range")
#    parser.add_argument('-L','--maxlength',type=int, nargs=1, help="maximum value of the length range")
#    parser.add_argument('-f','--fasta',type=str, nargs=1, help="fasta format file contain sequense length information/first base composition")
#    return parser

try:
    fqfile = sys.argv[1]
except IndexError as ie:
    raise SystemError("Error: please speicify the fastq format file\n")

if not os.path.exists(fqfile):
    raise SystemError("Error: File dose not exist in that path")

def getRecord(lines=None):
    keynames = ["name","sequence","optional",'quality']
    return {k:v for k,v in zip(keynames, lines)}

fqfile = sys.argv[1]

#Store the unique reads for vevlet assembly
NotUniqueFasta = fqfile.replace(".fastq",".forVelvetAssembly.fasta")
NotUniqueFastafile = open(NotUniqueFasta, "w")

with open(sys.argv[1]) as fq:
    lines = []
    notUniqueID = 0
    seqnum = dict()
    for line in fq:
        lines.append(line.strip())
        if len(lines) == 4:
            record = getRecord(lines)
            reads = record["sequence"]
            if reads.count("N")==0 and (len(reads) >= 18 and len(reads) <= 30):
                notUniqueID +=1
                NotUniqueFastafile.write(">seq_%s\n%s\n" % (notUniqueID,reads))
                if reads in seqnum:
                    seqnum[reads] =  int(seqnum[reads]) + 1
                else:
                    seqnum[reads] = 1
            lines= []
NotUniqueFastafile.close()
#print(seqnum)

#Store the collapsed reads
UniqueFasta = fqfile.replace(".fastq",".collapsed.fasta")
UniqueFastafile = open(UniqueFasta, "w")
seqid = 0
for k,v in sorted(seqnum.items(), key = lambda item: (-item[1], item[0])):
    UniqueFastafile.write(">rna7.7_%d_%dx\n%s\n" % (seqid, v, k))
    seqid +=1 
UniqueFastafile.close()
