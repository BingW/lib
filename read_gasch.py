#coding utf-8
class Stress():
    def __init__(self,UID):
        self.UID = UID
        self.heat_shock = [] #line[3:11]
        self.temp_ch_37_25 = [] #


f = open("complete_dataset.txt")
first_line = f.readline()
conditions = first_line.split("\t")
#print conditions[1:3]
#print conditions[3:11]  #hs1 [5,10,15,20,30,40,60,80]
#print conditions[11:18] #hs2 [0,0,0,5,15,30,60]
#print conditions[18:23] #37C to 25C [15,30,45,60,90]
#print conditions[23:28] #17,21,25,29,33 to 37 [20]
#print conditions[28:31] #29C to 33C [5,15,30]
#print conditions[31]    #33C vs 30C [90]
#print conditions[32:35] #29C +1M sorbitol to 33C + 1M sorbitol [5,15,30]
#print conditions[35:38] #29C +1M sorbitol to 33C + *NO sorbitol[5,15,30]
#print conditions[38:48] #constant 0.32 mM H2O2 (10 min)[10,20,30,40,50,60,80,100,120,160]
#print conditions[48:57] #1 mM Menadione [10,20,30,40,50,80,105,120,160]
#print conditions[57:65] #2.5mM DTT [5,15,30,45,60,90,120,180]
#print conditions[65:72] #DTT2 [0,15,30,60,120,240,480]
#print conditions[72:80] #1.5mM diamide [5,10,20,30,40,50,60,90]
#print conditions[80:87] #1M sorbitol [5,15,30,45,60,90,120]
#print conditions[87:92] #Hypo-osmotic shock [5,15,30,45,60]
#print conditions[92]    #steady-state 1M sorbitol
#print conditions[93:98] #aa strav [0.5,1,2,4,6]h
#print conditions[98:108] #Nitrogen Depletion [0.5,1,2,4,8,12,1d,2d,3d,5d]
#print conditions[108:115] #diauxic shift timecourse [0,9.5,11.5,13.5,15.5,18.5,20.5]h
#print conditions[115:125] #YPD-2 [2,4,6,8,10,12,1d,2d,3d,5d]
#print conditions[125:137] #YPD-1 [2,4,6,8,12,1d,2d,3d,5d,7d,13d,22d,28d]
#print conditions[137] #DBY7286 37degree heat - 20 min
#print conditions[138] #DBYmsn2-4- 37degree heat - 20 min
#print conditions[139] #DBYmsn2/4 (real strain) + 37degrees (20 min)
#print conditions[140] #DBYyap1- 37degree heat - 20 min (redo)
#print conditions[141] #DBYyap1 + 37degree heat (repeat)
#print conditions[142] #DBY7286 + 0.3 mM H2O2 (20 min)
#print conditions[143] #DBYmsn2msn4 (good strain) + 0.32 mM H2O2
#print conditions[144] #DBYmsn2/4 (real strain) + 0.32 mM H2O2 (20 min)
#print conditions[145] #DBYyap1- + 0.3 mM H2O2 (20 min)
#print conditions[146] #DBYyap1 + 0.32 mM H2O2 (20 min)
#print conditions[147] #Msn2 overexpression (repeat)
#print conditions[148] #Msn4 overexpression
#print conditions[149] #YAP1 overexpression
#print conditions[150] #ethanol vs. reference pool car-1
#print conditions[151] #galactose vs. reference pool car-1
#print conditions[152] #glucose vs. reference pool car-1
#print conditions[153] #mannose vs. reference pool  car-1
#print conditions[154] #raffinose vs. reference pool car-1
#print conditions[155] #sucrose vs. reference pool car-1
#print conditions[156] #YP ethanol vs reference pool car-2
#print conditions[157] #YP fructose vs reference pool car-2
#print conditions[158] #YP galactose vs reference pool car-2
#print conditions[159] #YP glucose vs reference pool car-2
#print conditions[160] #YP mannose vs reference pool car-2
#print conditions[161] #YP raffinose vs reference pool car-2
#print conditions[162] #YP sucrose vs reference pool car-2
#print conditions[163:168] #17,21,25,29,37 deg growth
#print conditions[168:176] #15,17,21,25,29,33,36,36 steady state
for condition in conditions:
    print condition
for line in f:
    expressions = line.split("\t")
    print expressions[0],expressions[3:11] #Heat Shock 1
