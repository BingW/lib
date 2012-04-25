import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

def scatter(x,y,save_file,label_info):

    # definitions for the axes
    left, width = 0.05, 0.65
    bottom, height = 0.05, 0.65
    bottom_h = left_h = left+width+0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]
    rect_label = [left_h,bottom_h,0.2,0.2]

    # start with a rectangular Figure
    plt.figure(1, figsize=(8,8))

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)

    # no labels
    nullfmt   = NullFormatter()   
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    # the scatter plot:
    axScatter.scatter(x, y)

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(y))])
    lim = (int(xymax/binwidth) + 1) * binwidth
    
    
    gradient,intercept,r_value,p_value,std_err = stats.linregress(x,y)
    x_fit = np.array([np.amin(x),np.amax(x)])
    y_fit = gradient * x_fit + intercept
    r_square = " r^2   = %e" % r_value**2
    p_value = "p_value = %e" % p_value
    std_err = "std_err = %e" % std_err
    plt.figtext(left_h,bottom_h+0.05,r_square)
    plt.figtext(left_h,bottom_h+0.1,p_value)
    plt.figtext(left_h,bottom_h,std_err)
    axScatter.plot(x_fit,y_fit)


    axScatter.set_xlim((-lim, lim))
    axScatter.set_ylim((-lim, lim))
   
    axHistx.hist(x, bins=100)
    axHisty.hist(y, bins=100, orientation='horizontal')

    axHistx.set_xlim( axScatter.get_xlim() )
    axHisty.set_ylim( axScatter.get_ylim() )
    

    plt.figtext(0.5, 0.965, label_info, ha='center',  \
            color='black', weight='bold', size='large')
    plt.savefig(save_file)
    plt.clf()

if __name__ == "__main__":
    scatter(np.random.randn(1000),np.random.randn(1000),\
            "/Users/bingwang//VimWork/scatter_hist.png",\
            "x random vs y random")
