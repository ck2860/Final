import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import tensorflow.compat.v1 as tf
tf.logging.set_verbosity(tf.logging.ERROR)

## Documentation for plot class
# this class has a graph function that you will be using for evaluations.


class plot():
    ## Documentation for graph function
    # Plot the x and y values for graphing and returns the graph of evaluation
    ##@param df1a: any dataframe
    ##@param df1Ameans: Decreasing-Epsilon means rewards
    ##@param df2Ameans: Greedy-Epsilon means rewards
    ##@param df3Ameans: Hybrid#1 means rewards
    ##@param df4Ameans: Hybrid#2 means rewards
    ##@param df5Ameans: Hybrid#3 means rewards
    ##@param df6Ameans: Hybrid#4 means rewards
    ##@param df7Ameans: Hybrid#5 means rewards

    def Eval_graph(self, df1a, df1_Ameans, df2_Ameans, df3_Ameans, df4_Ameans, df5_Ameans, df6_Ameans, df7_Ameans):
        df = pd.DataFrame({'x': df1a['x'], 'Epsilon-Decreasing': df1_Ameans, 'Epsilon-Greedy': df2_Ameans,
                          'Hybrid #1': df3_Ameans, 'Hybrid #2': df4_Ameans, 'Hybrid#3': df5_Ameans,
                           'Hybrid#4': df6_Ameans, 'Hybrid#5': df7_Ameans})

        plt.style.use('seaborn-darkgrid')

        plt.figure(figsize=(900/96, 900/96), dpi=96)
        palette = plt.get_cmap('tab10')

        num = 0
        for column in df.drop('x', axis=1):
            num += 1

            plt.subplot(3, 3, num)

            for v in df.drop('x', axis=1):
                plt.plot(df['x'], df[v], marker='', color='black', linewidth=0.5, alpha=0.5)

            # Plot
            plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=2.4, alpha=0.9, label=column)
            plt.xlim(0, 10000)
            plt.ylim(-8, 200)

            # Removing some ticks
            if num in range(5):
                plt.tick_params(labelbottom=False)
            if num in [2, 3, 5, 6]:
                plt.tick_params(labelleft=False)

            # Adding labels
            if num in range(1, 8, 3):
                plt.ylabel("Mean Reward", fontsize=10)
            if num in [5, 6, 7]:
                plt.xlabel("Episode", fontsize=10)

            # Add title
            plt.title(column, loc='left', fontsize=12, fontweight=0, color=palette(num))
            # general title
            plt.suptitle("In comparison of mean rewards", fontsize=13, fontweight=0, color='black', style='italic', y=1.02)
        return plt.show()

    def tukey(self, tukey_plot):
        # perform plot_simultaneous function from the statsmodel package
        tukey_plot.plot_simultaneous()
        return plt.show()
