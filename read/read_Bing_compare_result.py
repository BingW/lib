#coding:utf-8
'''
Author: Bing Wang
Last Modified: 2012.3.1
useage:
    import read_Bing_compare_result as Bing
    compare_result = Bing.read(compare_result)
'''
import math

def read(compare_result_tab_file):
    return Compare_Result(compare_result_tab_file)

class Compare_Result():
    def __init__(self,compare_result_tab_file):
        self.position = compare_result_tab_file
        self.sp0_name = []
        self.sp1_sp0 = []
        self.sp2_sp1 = []
        self.sp2_sp0 = []
        self.sp0 = []
        self.sp1 = []
        self.sp2 = []
        self.sp0_speed = []
        self.count = 0

        f = open(compare_result_tab_file)
        f.readline() #TODO ignore the first comment line
        for line in f:
            line = line.rstrip()
            element = line.split("\t")
            
            sp1_sp0 = float(element[1])
            sp2_sp0 = float(element[2])
            sp2_sp1 = float(element[3])

            if math.isnan(sp1_sp0) == True or  \
               math.isnan(sp2_sp0) == True or \
               math.isnan(sp2_sp1) == True:
                continue

            sp0 = (sp2_sp0 + sp1_sp0 - sp2_sp1)/2
            sp1 = (sp2_sp1 + sp1_sp0 - sp2_sp0)/2
            sp2 = (sp2_sp1 + sp2_sp0 - sp1_sp0)/2

            if sp1 < 0.0001 or sp0 < 0.0001: # ignore sp0_speed part
                sp0_speed = 1.0
            else:
                sp0_speed = sp0 / sp1

            self.sp0_name.append(element[0][:element[0].find("(")])
            self.sp1_sp0.append(sp1_sp0)
            self.sp2_sp1.append(sp2_sp1)
            self.sp2_sp0.append(sp2_sp0)
            self.sp0.append(sp0)
            self.sp1.append(sp1)
            self.sp2.append(sp2)
            self.sp0_speed.append(sp0_speed)
            self.count += 1
    
    def get_tail_index(self,tail=None):
        #The sp0_speed has a distribution 
        #tail is a percent, default 5%
        #this function can return both tails indexs of sp0_speed
        if tail == None:
            tail = 0.05
        order = sorted(self.sp0_speed)
        left_score = order[int(self.count*tail)]
        right_score = order[self.count - int(self.count*tail)]
    
        self.left_tail_index = [i for i,speed in enumerate(self.sp0_speed) if
                left_score > speed > 0]
        self.right_tail_index = [i for i,speed in enumerate(self.sp0_speed) if 
                speed > right_score]


if __name__ == "__main__":
    Kwal_Sklu_Klac = read("/Users/bingwang/VimWork/lib/test/Kwal_Sklu_Klac.txt") 
    Kwal_Sklu_Klac.get_tail_index(0.05)




