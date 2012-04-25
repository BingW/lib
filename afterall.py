#coding: utf-8
import numpy

class species():
    def __init__(self,sp_name):
        self.name = sp_name[:4]
        self.gene_name = []
        self.line = []
        f = open(WORKPATH+sp_name+'.txt')
        f.readline()
        for line in f:
            self.gene_name.append(line[:line.find("(")])
            self.line.append(line[:-1] + "\t")
        f.close()

    def read_ortholog(self,sp1):
        orthologlist = -1 * numpy.ones(len(self.gene_name),dtype = numpy.int16)
        f = open(WORKPATH + 'db/' + self.name + '-' + sp1.name + '-orthologs.txt')
        for line in f:
            if line[-2:] == '\t\n':
                line = line[:-2]
            else:
                line = line[:-1]
        #Some of the file end with '\n' some end with '\t\n'
        #This block clear the end
            if line.count('\t') > 1:
                continue
            #If one gene has more than one Ortholog, forget it
            try:
                s0num = self.gene_name.index(line[:line.find('\t')])
                line = line[line.find('\t')+1:]
            except:
                #print self.name, "do not have ", line[:line.find('\t')], "in common"
                continue
            if line != 'NONE':
                try:
                    orthologlist[s0num] = sp1.gene_name.index(line)
                except:
                    continue
                    #print sp1.name, "do not have ", line, "in common"
        f.close()
        return orthologlist

def after_all(sp_name):
    sp0 = species(sp_name[0])
    sp1 = species(sp_name[1])
    sp2 = species(sp_name[2])
    sp0.ortholog_sp1 = sp0.read_ortholog(sp1)
    sp0.ortholog_sp2 = sp0.read_ortholog(sp2)
    f = open(WORKPATH + "compare_result.txt","w")
    for i,ortholog_sp1 in enumerate(sp0.ortholog_sp1):
        if ortholog_sp1 != -1 and sp0.ortholog_sp2[i] != -1:
            f.write(sp0.line[i])
            f.write(sp1.line[ortholog_sp1])
            f.write(sp2.line[sp0.ortholog_sp2[i]])
            f.write("\n")
    f.close()
##main##
WORKPATH = "/Users/bingwang/VimWork/"
after_all(["Cgla_Scer_Scas","Kwal_Sklu_Klac","Agos_Klac_Sklu"])
