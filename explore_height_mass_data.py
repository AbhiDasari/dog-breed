import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import data_handler as dta
import fitter as fit

def plot_points(height,mass):
    plt.figure(4390)
    plt.clf()
    ax=plt.gca()
    ax.plot(height,mass,'x')
    ax.set_xlabel("Height in cm")
    ax.set_ylabel("weight in kgs")
    ax.set_title("Dog Breeds")

    return ax

def finalize_plot(ax):
    title=ax.get_title()
    plt.savefid(title+".png")

breed,height,mass= dta.get_data()
scatterplot=plot_points(height,mass)
finalize_plot(scatterplot)
    
