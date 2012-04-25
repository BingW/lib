# -*- coding:utf-8 -*-
'''
Author: Bing Wang
Last Modified: 2012.3.26
Version: V0.02
'''
#########################
#######Imput#############
import os
import sys
import time
import math
import numpy as np
sys.path.append("/Users/bingwang/VimWork/")
import lib.read.read_orthogroups_tab as orth
import lib.func.read as read
import lib.func.alnrefine as alr 
import lib.func.paml as paml
TIME_START = time.time()
WORKPATH = "/Users/bingwang/VimWork/"
#######  Class ##########
class Species():
    def __init__(self,name):
        self.name = name
        self.gene = {}
        f = open(WORKPATH+'db/'+self.name+"AA.fasta")
        for line in f:
            line = line.strip()
            if line[0] == ">":
                name = line[1:]
            else:
                self.gene[name] = line
        f.close()

######## Function ##########
def time_left(percent):
    time_used = time.time() - TIME_START
    print percent*100,'%'
    print "Time used:\t %.2f"%((time_used)/60.),'min'
    print "Time left:\t %.2f"%((time_used)*(1-percent)/(60.*percent)),'min'

def check_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def prepare_aln(sp0,sp1,sp2,outdir):
    print "************************************"
    print "*** Prepare Alignment input Data ***"
    print "************************************"
    for item in sp0.orth_sp1:
        try:
            sp0.orth_sp2[item]
            try:
                sp0.gene[item]
                sp1.gene[sp0.orth_sp1[item]]
                sp2.gene[sp0.orth_sp2[item]]
                write_f_name = item+"_"+sp0.orth_sp1[item]+"_"+ \
                        sp0.orth_sp2[item]+".fasta"
                f = open(outdir+write_f_name,"w")
                f.write(">"+item+"\n"+sp0.gene[item]+"\n")
                f.write(">"+sp0.orth_sp1[item]+"\n"+sp1.gene[sp0.orth_sp1[item]]+"\n")
                f.write(">"+sp0.orth_sp2[item]+"\n"+sp2.gene[sp0.orth_sp2[item]]+"\n")
                f.close()
            except:
                print "WARNING: gene",item,"not write" 
                continue
        except:
            pass

def batch_run_dialign(path):
    print "************************************"
    print "***         Doing Alignment      ***"
    print "************************************"
    fsalist = []
    conf = "/Users/bingwang/VimWork/lib/conf/"
    dialign = "dialign-tx "
    for item in os.listdir(path):
        if item[item.rfind(".")+1:] == "fasta":
            fsalist.append(item)
    total = len(fsalist)
    for i,item in enumerate(fsalist):
        time_left(i*1.0/total+0.0001)
        infile = path+item
        outfile = path+item[:item.rfind(".")]+".fa"
        cmd = dialign+" "+conf+" "+infile+" "+outfile
        os.system(cmd)

def batch_refine_aln(path):
    print "**************************"
    print "*** Refining Alignment ***"
    print "**************************"
    for item in os.listdir(path):
        if item[item.rfind(".")+1:] == "fa":
            alr.refine(path + item)


def batch_write_ctl(aa_path,treefile=None):
    print "*****************************"
    print "*** Writing paml ctl file ***"
    print "*****************************"
    if treefile == None:
        treefile = WORKPATH + "lib/func/3.tree"
    for item in os.listdir(aa_path):
        if item[item.rfind(".")+1:] == "aa":
            paml.write_ctl(aa_path+item,treefile)
           
def batch_codeml(ctl_path):
    print "*********************"
    print "*** Runing codeml ***"
    print "*********************"
    ctllist = []
    for item in os.listdir(ctl_path):
        if item[item.rfind(".")+1:] == "ctl":
            paml.codeml(ctl_path+item)

def batch_read_output(out_path,outfile):
    f = open(outfile,"w")
    f.write("Sp0\tSp1\tSp2\tsp1+sp0\tsp2+sp0\tsp2+sp1\t\n")
    for item in os.listdir(out_path):
        if item[item.rfind(".")+1:] == "out":
            paml_out = paml.codeml_read(out_path+item)
            f.write(paml_out.write_line())
    f.close()

def check_num_of_file(outdir):
    count_fasta = 0
    count_aa = 0
    count_out = 0
    for item in os.listdir(outdir):
        a = item[item.rfind(".")+1:]
        if a == "out":
            count_out += 1
        elif a == "fasta":
            count_fasta += 1
        elif a == "aa":
            count_aa += 1
    if count_out == count_aa and count_aa == count_fasta:
        return True
    else:
        return False

def pipe(sp_name):
    #########        Calculte function           ########
    outdir = WORKPATH+sp_name[0] +"_"+sp_name[1]+"_"+sp_name[2]+"/"
    check_dir(outdir)    #if not exist,creat it
    sp0 = Species(sp_name[0])
    sp1 = Species(sp_name[1])
    sp2 = Species(sp_name[2])
    sp0.orth_sp1 = orth.one(sp0.name,sp1.name)
    sp0.orth_sp2 = orth.one(sp0.name,sp2.name)
    prepare_aln(sp0,sp1,sp2,outdir)
    batch_run_dialign(outdir)
    batch_refine_aln(outdir)
    batch_write_ctl(outdir)
    batch_codeml(outdir)
    if check_num_of_file(outdir):
        outfile = WORKPATH+sp_name[0] +"_"+sp_name[1]+"_"+sp_name[2]+".txt"
        batch_read_output(outdir,outfile)

if __name__ == "__main__":
    pipe(["Agos","Sklu","Kwal"])
    pipe(["Agos","Klac","Kwal"])
    pipe(["Agos","kwal","Scer"])

