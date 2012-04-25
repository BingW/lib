#codind: utf-8
'''
Author: Bing Wang
Last Modified: 2012.3.1
useage:
    import read_go_slim_map as slim
    go_slim = slim.read(go_slim_tab_file)
'''
def read(go_slim_tab_file):
    go_slim = Go_Slim(go_slim_tab_file)
    return go_slim

class Go_Slim():
    def __init__(self,go_slim_tab_file):
        self.orf = []
        self.gene = []
        self.SGDID = []
        self.aspect = []
        self.slim_term = []
        self.GOID = []
        self.feature_type = []
        f = open(go_slim_tab_file)
        for line in f:
            line = line.strip()
            element = line.split("\t")
            self.orf.append(element[0])
            self.gene.append(element[1])
            self.SGDID.append(element[2])
            self.aspect.append(element[3])
            self.slim_term.append(element[4])
            self.GOID.append(element[5])
            self.feature_type.append(element[6])

    def get_term(self,SGDID):
        indexs = [i for i,x in enumerate(self.SGDID) if x == SGDID]
        term = [self.slim_term[i] for i in indexs]
        aspect = [self.aspect[i] for i in indexs]
        return zip(aspect,term)


if __name__ == "__main__":
    go_slim_tab_file = "/Users/bingwang/VimWork/lib/test/go_slim_mapping.tab"
    go_slim = Go_Slim(go_slim_tab_file)
    print go_slim.get_term("S000007338")


