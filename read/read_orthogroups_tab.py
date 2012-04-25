#coding:utf-8
'''
Author: Bing Wang
Last Modified: 2012.3.21
version: 0.02
useage:
    import sys
    sys.path.append("/Users/bingwang/VimWork/")
    import lib.read.read_orthogroups_tab as orth
    orthogroup = orth.read(orthogroups_tab_file)
    one_orth = orth.one(sp1_name,sp2_name)
'''
def read(orthogroups_tab_file):
    orthogroup = {}
    f = open(orthogroups_tab_file)
    for line in f:
        line = line.strip()
        element = line.split("\t")
        orthogroup[element[0]] = element[1:]
    return orthogroup

def combine_orth(orth1,orth2):
    orth0 = {}
    for name in orth1:
        try:
            if orth2[orth1[name]] == name:
                orth0[name] = orth1[name]
        except:
            continue
    return orth0

def one(sp1,sp2):    #return a one orth dict
    orth_sp1_sp2 = {}
    f = open("/Users/bingwang/VimWork/db/"+sp1+"-"+sp2+"-orthologs.txt")
    for line in f:
        elements = line.strip().split("\t")
        if len(elements) == 2 and elements[1] != 'NONE':
            orth_sp1_sp2[elements[0]] = elements[1]
    f.close()

    orth_sp2_sp1 = {}
    f = open("/Users/bingwang/VimWork/db/"+sp2+"-"+sp1+"-orthologs.txt")
    for line in f:
        elements = line.strip().split("\t")
        if len(elements) == 2 and elements[1] != 'NONE':
            orth_sp2_sp1[elements[0]] = elements[1]
    f.close()

    return combine_orth(orth_sp1_sp2,orth_sp2_sp1)

if __name__ == "__main__":
    orthogroups_tab_file = "/Users/bingwang/VimWork/lib/test/Cgla-Agos-orthologs.txt"
    Cgla_Agos = read(orthogroups_tab_file)
    orth = one("Agos","Scer") 
    print orth

 


