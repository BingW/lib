#coding: utf-8
'''
Author: Bing Wang
Last Modified: 2012.3.19
useage:
    import sys
    sys.path.append("/Users/bingwang/VimWork/")
    import lib.func.paml as paml

    paml.write_ctl(             # aafile -> ctlfile
        aafile                  # aafile location
        treefile                # treefile location
        [ctlfile = aafile.ctl   # ctlfile output
        outfile = aafile.out    # main result file name
        noisy = 0               # 0,1,2,3,9: how much rubbish on the screen
        verbose = 1             # 0: concise; 1: detailed, 2: too much
        runmode = 0             # 0: user tree;  1: semi-automatic;  2: automatic
                                  3: StepwiseAddition; (4,5):PerturbationNNI; -2: pairwise noise 
        seqtype = 2             # 1:codons; 2:AAs; 3:codons-->AAs
        aaRatefile = wag.dat    # only used for aa seqs with model=empirical(_F)
                                  dayhoff.dat, jones.dat, wag.dat, mtmam.dat, or your own
        model = 8               # models for AAs or codon-translated AAs:
                                  0:poisson, 1:proportional, 2:Empirical, 3:Empirical+F
                                  6:FromCodon, 7:AAClasses, 8:REVaa_0, 9:REVaa(nr=189)
        Mgene = 0               # AA: 0:rates, 1:separate
        clock = 0               # 0:no clock, 1:global clock; 2:local clock
        fix_alpha = 1           # 0: estimate gamma shape parameter; 1: fix it at alpha
        alpha = 0.              # initial or fixed alpha, 0:infinity (constant rate)
        Malpha = 0              # different alphas for genes
        ncatG = 5               #  of categories in dG of NSsites models
        getSE = 1               # 0: don't want them, 1: want S.E.s of estimates
        RateAncestor = 0        # (0,1,2): rates (alpha>0) or ancestral states (1 or 2)
        Small_Diff = 1e-6
        cleandata = 1           # remove sites with ambiguity data (1:yes, 0:no)?
        fix_blength = 0         # 0: ignore, -1: random, 1: initial, 2: fixed
        method = 1]             # 0: simultaneous; 1: one branch at a time
        )

    paml.codeml(                #aafile+ctlfile -> outfile
        ctlfile
        )
'''
import os
class out():
    def __init__(self):
        self.sp0name = ""
        self.sp1name = ""
        self.sp2name = ""
        self.sp1_sp0 = 0
        self.sp2_sp0 = 0
        self.sp2_sp1 = 0
    def write_line(self):
        return self.sp0name+"\t"+self.sp1name+"\t"+\
                    self.sp2name+"\t"+str(self.sp1_sp0)+"\t"+\
                    str(self.sp2_sp0)+"\t"+str(self.sp2_sp1)+"\t\n"

def read_line(line):
    output = out()
    elements = line.split("\t")
    output.sp0name = elements[0]
    output.sp1name = elements[1]
    output.sp2name = elements[2]
    output.sp1_sp0 = float(elements[3])
    output.sp2_sp0 = float(elements[4])
    output.sp2_sp1 = float(elements[5])
    return output
        

def codeml(ctlfile):
    cmd = "codeml " + ctlfile
    os.system(cmd)

def write_ctl(aafile,treefile,ctlfile=None,outfile=None,noisy=None,verbose=None,
        runmode=None,seqtype=None,aaRatefile=None,model=None,Mgene=None,clock=None,
        fix_alpha=None,alpha=None,Malpha=None,ncatG=None,getSE=None,RateAncestor=None,
        Small_Diff=None,cleandata=None,fix_blength=None,method=None):
    
    seqfile = aafile
    if ctlfile == None:
        ctlfile = aafile[:aafile.rfind(".")] + ".ctl"
    if outfile == None:    
        outfile = aafile[:aafile.rfind(".")] + ".out"   
    if noisy == None:
        noisy = 0 
    if verbose == None:
        verbose = 1 
    if runmode == None:
        runmode = 0
    if seqtype == None:
        seqtype = 2    
    if aaRatefile == None:
        aaRatefile = "wag.dat" 
    if model == None:
        model = 8      
    if Mgene == None:
        Mgene = 0      
    if clock == None:
        clock = 0     
    if fix_alpha == None:
        fix_alpha = 1 
    if alpha == None:
        alpha = 0.  
    if Malpha == None:
        Malpha = 0   
    if ncatG == None:
        ncatG = 5
    if getSE == None:
        getSE = 1     
    if RateAncestor == None:
        RateAncestor = 0
    if Small_Diff == None:
        Small_Diff = 1e-6
    if cleandata == None:
        cleandata = 1
    if fix_blength == None:
        fix_blength = "0"     
    if method == None:
        method = "1"
    f = open(ctlfile,"w")
    f.write(        "         seqfile = " + seqfile      + "\n" +
                    "        treefile = " + treefile     + "\n" +
                    "         outfile = " + outfile      + "\t" + 
                                   "* main result file name \n" +
                    "           noisy = " + str(noisy)        + "\t" + 
               "* 0,1,2,3,9: how much rubbish on the screen \n" +
                    "         verbose = " + str(verbose)      + "\t" + 
                    "* 0: concise; 1: detailed, 2: too much \n" +
                    "         runmode = " + str(runmode)      + "\t" + 
         "* 0: user tree;  1: semi-automatic;  2: automatic \n" +
                    "                      " +
   "* 3: StepwiseAddition; (4,5):PerturbationNNI; -2: pairwise noise \n" +
                    "         seqtype = " + str(seqtype)      + "\t" + 
                         "* 1:codons; 2:AAs; 3:codons-->AAs \n" +
                    "      aaRatefile = " + aaRatefile   + "\t" +
          "* only used for aa seqs with model=empirical(_F) \n" +
                    "           model = " + str(model)        + "\t" + 
                 "* models for AAs or codon-translated AAs: \n" +
                    "                      " +
   "* 0:poisson, 1:proportional, 2:Empirical, 3:Empirical+F \n" +
                    "                      " +
    "* 6:FromCodon, 7:AAClasses, 8:REVaa_0, 9:REVaa(nr=189) \n" + 
                    "           Mgene = " + str(Mgene)        + "\t" +
                                 "* AA: 0:rates, 1:separate \n" +
                    "           clock = " + str(clock)        + "\t" +
               "* 0:no clock, 1:global clock; 2:local clock \n" +
                    "       fix_alpha = " + str(fix_alpha)    + "\t" + 
   "* 0: estimate gamma shape parameter; 1: fix it at alpha \n" +
                    "           alpha = " + str(alpha)        + "\t" +
      "* initial or fixed alpha, 0:infinity (constant rate) \n" +
                    "          Malpha = " + str(Malpha)       + "\t" +
                              "* different alphas for genes \n" +
                    "           ncatG = " + str(ncatG)        + "\t" +
                   "* of categories in dG of NSsites models \n" +
                    "           getSE = " + str(getSE)        + "\t" +
          "* 0: don't want them, 1: want S.E.s of estimates \n" +
                    "    RateAncestor = " + str(RateAncestor) + "\t" +
   "* (0,1,2): rates (alpha>0) or ancestral states (1 or 2) \n" +
                    "      Small_Diff = " + str(Small_Diff)   + "\n" +
                    "       cleandata = " + str(cleandata)    + "\t" +
         "* remove sites with ambiguity data (1:yes, 0:no)? \n" +
                    "     fix_blength = " + str(fix_blength)  + "\t" +
             "* 0: ignore, -1: random, 1: initial, 2: fixed \n" +
                    "          method = " + str(method)       + "\t" +
                "* 0: simultaneous; 1: one branch at a time \n")
    f.close()

def codeml_read(outfile):
    f = open(outfile)
    AA_distance = False
    Time_used = False
    paml_out = out()
    rate_matrix = []

    for line in f:
        if line.find("Time used:") != -1:
            Time_used = True
            AA_distance = False
        if AA_distance == True and Time_used == False and line != "\n":
            rate_matrix.append(line[:line.find("\n")])
        if line.find("AA distances") != -1:
            AA_distance = True
    f.close()
    
    paml_out.sp0name = rate_matrix[0][:rate_matrix[0].find(" ")]
    paml_out.sp1name = rate_matrix[1][:rate_matrix[1].find(" ")]
    paml_out.sp1_sp0 = float(rate_matrix[1][rate_matrix[1].find(" "):])
    paml_out.sp2name = rate_matrix[2][:rate_matrix[2].find(" ")]
    the_rest = rate_matrix[2][rate_matrix[2].find(" "):].lstrip()
    paml_out.sp2_sp0 = float(the_rest[:the_rest.find(" ")])
    paml_out.sp2_sp1 = float(the_rest[the_rest.find(" "):])

    return paml_out

if  __name__ == "__main__":
    filename = "Kwal0.3_SAKL0D07062g_KLLA0F01793g"
    treefile = "/Users/bingwang/VimWork/lib/func/3.tree"
    aafile = "/Users/bingwang/VimWork/lib/test/"+filename+".aa"
    ctlfile = "/Users/bingwang/VimWork/lib/test/"+filename+".ctl"
    outfile = "/Users/bingwang/VimWork/lib/test/"+filename+".out"
    write_ctl(aafile,treefile)
    codeml(ctlfile)
    print codeml_read(outfile).write_line()
