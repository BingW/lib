#coding: utf-8
###########Input###############
import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append("/Users/bingwang/VimWork/")
import My_Physical_engine as Phy
import read_orthogroups_tab as orth
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
def fileter_by_type(exp_type,interactions):
    #This return a subset of interactions with specifc exe_type
    collect_interaction = []
    for interaction in interactions:
        try:
            exp_type.index(interaction.exp_type)
            collect_interaction.append(interaction)
        except:
            continue
    return collect_interaction

def write_gene_func(name_lists,write_file):
    #this write functions of name_lists to write_file
    import lib.read.read_SGD_features_tab as SGD 
    SGD_feature_tab_file = "/Users/bingwang/VimWork/db/SGD_features.tab"
    feature_table = SGD.read(SGD_feature_tab_file)
    f = open(write_file,"w")
    for name in name_list:
        index = SGD.get_feature_index(name,feature_table)
        description = feature_table[index].description
        f.write(node+"\t"+str(nx.degree(DR_net)[node])+"\t"+description+"\n")
    f.close()

def sub_by_degree(min_degree,net):
    #return a subset of net by biger than min_degree
    remove_node_list = [item for item in nx.degree(DR_net) \
            if nx.degree(DR_net)[item] < min_degree]
    new_net = nx.Graph()
    new_net.add_nodes_from(net.nodes())
    new_net.add_edges_from(net.edges())
    for name in remove_node_list:
        new_net.remove_node(name)
    return new_net

##############main################
#interaction_file = "/Users/bingwang/VimWork/db/interaction_data.tab"
#interactions = []
#f = open(interaction_file)
#for line in f:
#    line = line.strip()
#    interaction = Interaction(line)
#    interactions.append(interaction)
#f.close()
#exp_type = ["Dosage Rescue"]
#DR_net = nx.Graph()
#for item in fileter_by_type(exp_type,interactions):
#    DR_net.add_node(item.bait_name)
#    DR_net.add_node(item.hit_name)
#    DR_net.add_edge(item.bait_name,item.hit_name)
#
#min_degree = 20
#DR_net = sub_by_degree(min_degree,DR_net)
#
#Phy.physics_engine(DR_net)
#MC.monte_carlo(DR_net)
#nodesize = [nx.degree(DR_net)[item]+min_degree for item in DR_net]
#nx.draw_circular(DR_net,node_size=nodesize,with_labels=False)
#plt.savefig("/Users/bingwang/VimWork/DR_"+str(min_degree)+".png",dpi=1000)

pombe_tab = "/Users/bingwang/VimWork/BIOGRID-ORGANISM-Schizosaccharomyces_pombe-3.1.86.tab.txt"
Scer_tab = "/Users/bingwang/VimWork/BIOGRID-ORGANISM-Saccharomyces_cerevisiae-3.1.86.tab.txt"
interactions = []
f = open(pombe_tab)
while(f.readline()[0:8] != "INTERACT"):
    pass
for line in f:
    interaction =  Interaction_BioGrid(line)
    interactions.append(interaction)
f.close()

exp_type = ["Dosage Rescue"]
DR_net = nx.Graph()
for item in fileter_by_type(exp_type,interactions):
    DR_net.add_node(item.bait_name)
    DR_net.add_node(item.hit_name)
    DR_net.add_edge(item.bait_name,item.hit_name)

min_degree = 1
#DR_net = sub_by_degree(min_degree,DR_net)
nodesize = [nx.degree(DR_net)[item]+min_degree for item in DR_net]
nx.draw_circular(DR_net,node_size=nodesize,with_labels=False)
plt.savefig("/Users/bingwang/VimWork/pombe/DR_"+str(min_degree)+".png",dpi=1000)

Scer_Spom_tab = "/Users/bingwang/VimWork/db/Scer-Spom-orthologs.txt"
Scer_Spom = orth.read(Scer_Spom) ##self.A    self.B    self.get_orth_index


