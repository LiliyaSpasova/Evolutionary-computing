import random
import numpy
import os
import pingouin as pg
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
glsSolutions=[4, 3, 6, 5, 3, 4, 6, 3, 4, 3, 5, 6, 4, 6, 4, 8, 5, 10, 6, 8, 3, 4, 8, 6, 3]    
mlsSolutions=[9, 5, 13, 9, 16, 13, 15, 15, 15, 12, 9, 12, 9, 11, 15, 13, 13, 11, 13, 16, 9, 9, 16, 11, 9]  
ilsSolutions=[19, 16, 25, 17, 24, 13, 18, 20, 7, 18, 14, 16, 18, 6, 17, 21, 15, 24, 21, 18, 14, 18, 13, 17, 15]


def MannWhitneyTest(experiment_data, out_name):
    data = pd.read_csv(experiment_data)
    out_df = pd.DataFrame(columns=["algorithms", "U statistic", "p-value"])
    for i in range(0, 2):
        for j in range(i+1, 3):
            mwu = pg.mwu(data.iloc[:, i], data.iloc[:, j], alternative="two-sided")
            u_statistic = mwu["U-val"][0]
            p_val = mwu["p-val"][0]
            algorithms = data.columns[i] + "_" + data.columns[j]
            test_data = {"algorithms": algorithms, "U statistic": u_statistic, "p-value": p_val}

            out_df = out_df.append(test_data, ignore_index=True)

   

    out_df.to_csv(out_name, index=False)
    return out_df


def boxplots( out_name):
    n=25
   
    new_data = {"algorithm": ["mls"]*n + ["ils"]*n + ["gls"]*n,
                "minCut": mlsSolutions + ilsSolutions + glsSolutions }
    new_df = pd.DataFrame(new_data)
    sns.boxplot(data=new_df, x="algorithm", y="minCut",
                showmeans=True,
                meanprops={"marker": "o",
                           "markerfacecolor": "white",
                            "markeredgecolor": "black",
                            "markersize": 12})
    sns.stripplot(data=new_df, x="algorithm", y="minCut",
                  color="black",
                  alpha=0.7)
    plt.suptitle(out_name, y=1, fontsize=15)
    plt.title("minimum cuts for each algorithm\ncomputed over 25 runs",
              y=0.99,
              fontsize=10)
  
    plt.savefig(out_name)
    plt.clf()

def meanMedianSD():
    print ("MLS")
    print ("mean",numpy.mean(mlsSolutions))
    print ("median",numpy.median(mlsSolutions))
    print ("sd",numpy.std(mlsSolutions))
    print ("ILS")
    print ("mean",numpy.mean(ilsSolutions))
    print ("median",numpy.median(ilsSolutions))
    print ("sd",numpy.std(ilsSolutions))
    print ("GLS")
    print ("mean",numpy.mean(glsSolutions))
    print ("median",numpy.median(glsSolutions))
    print ("sd",numpy.std(glsSolutions))
    
#boxplots("Data")
#MannWhitneyTest("dataForMannWhitney.csv","MannWhitney")
meanMedianSD()