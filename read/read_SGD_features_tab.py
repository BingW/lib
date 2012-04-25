# coding:utf-8
'''
Author: Bing Wang
Last Modified: 2012.3.14
useage:
    import read_SGD_features_tab as SGD
    SGD_feature_table = SGD.read(SGD_feature_tab_file)
'''

def read(SGD_feature_tab_file):
    #TODO filetest
    #This file should be tab split file contains 15 tabs and 16 features, see readme
    features = []
    f = open(SGD_feature_tab_file)
    for line in f:
        feature = SGD_Feature(line)
        features.append(feature)
    return features
    f.close()

def get_feature_index(feature_name,features):
    for i,item in enumerate(features):
        if item.feature_name == feature_name:
            return i
    return None

class SGD_Feature():
    def __init__(self,line):
        line = line.replace("\n","")
        element = line.split("\t")
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

if __name__ == '__main__':
    SGD_feature_tab_file = "/Users/bingwang/VimWork/lib/test/SGD_features.tab"
    SGD_feature_table = read(SGD_feature_tab_file)
