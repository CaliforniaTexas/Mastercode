#!/usr/bin/env python
import os
import sys
import pypstats
import glob
import numpy
#output_file="./wc_output/wc_result.txt"
#input_dir = "./wc_input"

with open(sys.argv[0], 'r') as my_file:
    input_dir = sys.argv[1]
    output_file=sys.argv[2]

    file_lines=[]
    Wcnt=[]
    m=[]
    #sys.stdout = open("C:\\Users\\SIVA\\Desktop\\Median_res.txt","w")
    
    list_of_files = glob.glob(input_dir+"/*.txt")
    #f = open("C:\\Users\\SIVA\\Desktop\\Proj\\output\\Median.txt", "a")
    for file in sorted(list_of_files):
        with open(file, 'r') as content_file:
            file_read=content_file.read()
            file_lines.append(file_read)
    #print(file_lines)
    
    for line_lf in file_lines:
        lineIn = line_lf.split('\n')
        for line in lineIn:
    #        print(line)
            word = line.split()
            Wcnt.append(len(word))
            m.append(numpy.median(Wcnt))
     #       print(m)

    f=open(output_file,"w")
    f.write(str(m).replace(',','\n').replace('[','').replace(']','').replace(' ',''))
    f.close()
    
# python ./src/median_calc.py ./wc_input/textfiles ./wc_output/med_result.txt
