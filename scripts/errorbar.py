import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def errorbar(data, addition = ""):
    
    _, axs = plt.subplots(5, figsize=(8, 6), sharex = True, layout="tight")
    
    sns.stripplot(x = data, jitter = 1.0, ax=axs[0])
    sns.pointplot(x = data, errorbar = "sd", capsize=.2, ax=axs[1])
    sns.pointplot(x = data, errorbar = "pi", capsize=.2, ax=axs[2])
    sns.pointplot(x = data, errorbar = "se", capsize=.2, ax=axs[3])
    sns.pointplot(x = data, errorbar = "ci", capsize=.2, ax=axs[4])
    
    axs[0].set_title((data.name + " " + addition).strip())
    axs[1].set_title("Standard deviation")
    axs[2].set_title("Percentile interval")
    axs[3].set_title("Standard error")
    axs[4].set_title("Confidence error")

    for ax in axs:
        ax.set_xlabel("")
        ax.tick_params(labelbottom = True)
    
    