#coding:utf-8
class Gene_Association():
    def __init__(self,gene_association_file):
        self.db = []
        self.db_object_id = []
        self.db_object_symbol = []
        self.qualifier = []
        self.go_id = []
        self.db_reference = []
        self.evidence = []
        self.with_from = []
        self.aspect = []
        self.db_object_name = []
        self.db_object_synonym = []
        self.db_object_type = []
        self.taxon = []
        self.date = []
        self.assigned_by	 = []
        f = open(gene_association_file)
        for line in f:
            if line[0] != "!":
                line = line.strip()
                element = line.split("\t")
                self.db.append(element[0])
                self.db_object_id.append(element[1])
                self.db_object_symbol.append(element[2])
                self.qualifier.append(element[3])
                self.go_id.append(element[4])
                self.db_reference.append(element[5])
                self.evidence.append(element[6])
                self.with_from.append(element[7])
                self.aspect.append(element[8])
                self.db_object_name.append(element[9])
                self.db_object_synonym.append(element[10])
                self.db_object_type.append(element[11])
                self.taxon.append(element[12])
                self.date.append(element[13])
                self.assigned_by.append(element[14])
        f.close()

gene_association_file = "/Users/bingwang/Downloads/gene_association.sgd"
gene_association = Gene_Association(gene_association_file)
for item in gene_association.aspect:
    print item

