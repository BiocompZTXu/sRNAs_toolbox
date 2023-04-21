# sRNAs_toolbox

### How to use this code
#### Lets's begin with one demo datasets named random8000_for_hubiao.fq.gz

```bash
#Step1:Remove adapter seqeunce using Cutadapt; assuming 3' adater starts with "AGATCGGAAGAGC" 
cutadapt -a "AGATCGGAAGAGC" random8000_for_hubiao.fq.gz -j 5 -o random8000_for_hubiao.clean.fastq --untrimmed-output random8000_for_hubiao.notfound.fastq --minimum-length 8

#Step2: Preprocess with in-house Python script written by Z. Xu;
#Including: keep length between 18nt-30nt, remove any sequence contain "N", collapsed same sequence to unique one. 
python ~/biosoft/Code/sRNAs_collapse2unique.py random8000_for_hubiao.clean.fastq

#step3: Run virome analysis
perl ~/biosoft/VirusDetect_v1.7/virus_detect.pl --reference known_virus_reference --thread_num 5 random8000_for_hubiao.clean.forVelvetAssembly.fasta
```
