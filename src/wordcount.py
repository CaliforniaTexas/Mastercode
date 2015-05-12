#!/usr/bin/env python
import os
import sys

import re,os
import string


with open(sys.argv[0], 'r') as my_file:
    input_dir = sys.argv[1]
    output_file=sys.argv[2]
    
file=open(input_dir+"/Wordcount.txt","r+").read()
word_count={}
for word in file.lower().split():
    if word not in word_count:
        word_count[word]=1

    else:
            word_count[word]+=1

for item in word_count.items():
 f = open(output_file,"w")
for item in sorted(word_count.items()):
    f.write("{}\t{}\n".format(*item))
      
f.close()

#~python ./src/wordcount.py ./wc_input ./wc_output/wc_result.txt
