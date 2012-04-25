#coding: utf-8
###########Input###############
import sys
import math
import networkx as nx
import matplotlib.pyplot as plt
sys.path.append("/Users/bingwang/VimWork/")
import My_Physical_engine as Phy
#import MonteCarlo as MC
###########Class###############
class Interaction_SGD():
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

class Interaction_BioGrid():
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

############Function############
def exp_gene_filter(interactions,exp_type,p0_genes=None):
    #This return a subset of interactions with specifc exe_type
    if p0_genes == None:
        return [item for item in interactions if item.exp_type in exp_type]
    else:
        return [item for item in interactions \
                if item.exp_type in exp_type and \
                (item.bait_name in p0_genes or item.hit_name in p0_genes)]

def write_gene_func(name_lists,write_file):
    #this write functions of name_lists to write_file
    import lib.read.read_SGD_features_tab as SGD 
    SGD_feature_tab_file = "/Users/bingwang/VimWork/db/SGD_features.tab"
    feature_table = SGD.read(SGD_feature_tab_file)
    f = open(write_file,"w")
    for name in name_list:
        index = SGD.get_feature_index(name,feature_table)
        description = feature_table[index].description
        f.write(node+"\t"+str(nx.degree(PP_net)[node])+"\t"+description+"\n")
    f.close()

def sub_by_degree(min_degree,net):
    #return a subset of net by biger than min_degree
    remove_node_list = [item for item in nx.degree(net) \
            if nx.degree(net)[item] < min_degree]
    new_net = nx.Graph()
    new_net.add_nodes_from(net.nodes())
    new_net.add_edges_from(net.edges())
    for name in remove_node_list:
        new_net.remove_node(name)
    return new_net

def sub_by_genes(genes,net):
    remove_node_list = [item for item in net if not(item in genes)]
    new_net = nx.Graph()
    new_net.add_nodes_from(net.nodes())
    new_net.add_edges_from(net.edges())
    for name in remove_node_list:
        new_net.remove_node(name)
    return new_net

def p_value(n_hit,n,p):
    pv = 0
    for i in range(n_hit,n+1,1):
        pv += ((math.factorial(n)/(math.factorial(i)* \
                math.factorial(n-i)))*(p**i)*((1-p)**(n-i)))
    return pv

##############main################
if __name__ == "__main__":
    interaction_file = "/Users/bingwang/VimWork/db/interaction_data.tab"
    interactions = []
    PP_net = nx.Graph()

    f = open(interaction_file)
    for line in f:
        line = line.strip()
        interaction = Interaction_SGD(line)
        interactions.append(interaction)
    f.close()
    exp_type = ["Reconstituted Complex","Two-hybrid","Protein-peptide", \
        "PCA","FRET","Far Western","Co-purification","Co-localization", \
        "Co-fractionation","Co-crystal Structure","Affinity Capture-Western",\
        "Affinity Capture-MS","Affinity Capture-Luminescence"]    #NON directed
    gal_genes =["YBR018C","YBR019C","YBR020W","YDR009W",\
            "YLR081W","YML051W","YMR105C",\
            "YPL248C"]
    #gene_name = [GAL7,GAL10,GAL1,GAL3,\
    #           GAL2,GAL80,GAL5,\
    #           GAL4]
    for item in exp_gene_filter(interactions,exp_type,gal_genes):
        PP_net.add_node(item.bait_name)
        PP_net.add_node(item.hit_name)
        PP_net.add_edge(item.bait_name,item.hit_name)

    pos = nx.circular_layout(PP_net)
    for item in PP_net:
        pos[item] -= 0.5
        try:
            gal_genes.index(item)
        except:
            pos[item] *= 3
    p1_genes = [name for name in PP_net]

    tail="/Users/bingwang/VimWork/output/functions/left_tail_of_Agos_Klac_Sklu.txt"

    p0_rate = {}
    f = open(tail)
    for line in f:
        elements = line.split("\t")
        p0_rate[elements[4]] = elements[0]

    count = 0
    for item in p0_rate:
        try:
            p1_genes.index(item)
            count += 1
        except:
            continue
    nodesize = [nx.degree(PP_net)[item]+min_degree for item in PP_net]
    Phy.physics_engine(PP_net)

    print "p value:",p_value(count,len(p0_rate),len(p1_genes)*1./3070)
    nx.draw(PP_net,pos,node_size=nodesize,with_labels=True)
    plt.savefig("/Users/bingwang/VimWork/PP_Gal_"+str(min_degree)+".png",dpi=300)
    plt.clf()



