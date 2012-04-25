#coding:utf-8
'''
Author: Bing Wang
Last Modified: 2012.3.23
version: 0.01
useage:
    import sys
    sys.path.append("/Users/bingwang/VimWork/")
    import lib.read as read
'''
class SGD_Feature():
    def __init__(self,line):
        elements = line.split("\t")
        self.primary_SGDID = element[0]
        self.feature_type = element[1]
        self.feature_qualifier = element[2]
        self.feature_name = element[3]
        self.standard_gene_name = element[4]
        self.alias = element[5].split("|")
        self.parent_feature_name = element[6]
        self.second_SGDID = element[7].split("|")
        self.chromosome = element[8]
        self.start_coord = element[9]
        self.stop_coord = element[10]
        self.strand = element[11]
        self.genetic_position = element[12]
        self.coord_version = element[13]
        self.sequence_version = element[14]
        self.description = element[15]

class SGD_Interaction():
    def __init__(self,line):
        elements = line.split("\t")
        self.bait_name = elements[0]
        self.bait_standard = elements[1]
        self.hit_name = elements[2]
        self.hit_standard = elements[3]
        self.exp_type = elements[4]
        self.Gen_or_Phy = elements[5]
        self.note = elements[8]
        self.phenotype = elements[9]
        self.Manual_or_High = elements[7]
        self.src = elements[6]
        self.ref = elements[10]
        self.ciation = elements[11]

class SGD_Go_Slim():
    def __init__(self,line):
        elements = line.split("\t")
        self.orf = elements[0]
        self.gene = elements[1]
        self.SGDID = elements[2]
        self.aspect = elements[3]
        self.slim_term = elements[4]
        self.GOID = elements[5]
        self.feature_type = elements[6]

class SGD_Gene_Association():
    def __init__(self,line):
        elements = line.split("\t")
        self.db = elements[0]
        self.db_object_id = elements[1]
        self.db_object_symbol = elements[2]
        self.qualifier = elements[3]
        self.go_id = elements[4]
        self.db_reference = elements[5]
        self.evidence = elements[6]
        self.with_from = elements[7]
        self.aspect = elements[8]
        self.db_object_name = elements[9]
        self.db_object_synonym = elements[10]
        self.db_object_type = elements[11]
        self.taxon = elements[12]
        self.date = elements[13]
        self.assigned_by = elements[14]

class BioGrid_Interaction():
    def __init__(self,line):
        elements = line.split("\t")
        self.bait_name = elements[0]
        self.hit_name = elements[1]
        self.bait_standard = elements[2]
        self.hit_standard = elements[3]
        self.bait_alias = elements[4]
        self.hit_alias = elements[5]
        self.exp_type = elements[6]
        self.src = elements[7]
        self.PMID = elements[8]

##############################################
def orth(sp1,sp2):
    orthogroup = {}
    f = open("/Users/bingwang/VimWork/db/"+sp1+"-"+sp2+"-orthologs.txt")
    for line in f:
        line = line.strip()
        element = line.split("\t")
        orthogroup[element[0]] = element[1:]
    return orthogroup

def one_orth(sp1,sp2):    #return a one orth dict
    def combine_orth(orth1,orth2):
        orth0 = {}
        for name in orth1:
            try:
                if orth2[orth1[name]] == name:
                    orth0[name] = orth1[name]
            except:
                continue
        return orth0
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

###################################################
if __name__ == "__main__":
    line = "\t"*20
    one_orth("Scer","Agos")

