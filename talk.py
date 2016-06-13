import seaborn as sns
import matplotlib.pyplot as plt

def awesome_settings():
    # awesome plot options
    sns.set_style("white")
    sns.set_style("ticks")
    sns.set_context("paper", font_scale=2)
    sns.set_palette(sns.color_palette("deep"))
    # image stuff
    plt.rcParams['figure.figsize'] = (12.0, 6.0)
    plt.rcParams['savefig.dpi'] = 60
    plt.rcParams['lines.linewidth'] = 2

    return
