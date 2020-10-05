import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import warnings
warnings.filterwarnings("ignore")

##@package Tukey
#Documentation for Tukey.py
#
# we use a Tukey post hoc test to confirm where the differences occurred between greedy-bases strategies: Epsilon-Greedy, Epsilon-Decreasing, Hybrid#2, and Hybrid#4.
# No classes are created here. Statsmodels.stats.multicomp package is used; only pairwise_tukeyhsd function is performed.
df1= pd.read_csv('data/TukeyData.csv')
tukey = pairwise_tukeyhsd(endog=df1['MeanRewards'], groups=df1['Strategy'], alpha=0.05)
tukey.plot_simultaneous()
plt.show()