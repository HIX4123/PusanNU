#-------------------------------------------------------------------------------
# Name:        module1
# Author:      algor
#-------------------------------------------------------------------------------

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

myarray = np.array(
        [0.1, 0.12, 0.15, 0.83],
        [0.3, 0.42, 0.25, 0.73],
        [0.4, 0.52, 0.35, 0.63],
        [0.5, 0.62, 0.45, 0.53] )

df = pd.DataFrame(  myarray, columns=["a","b","c","d"])
array = df.to_numpy()

# Default heatmap
p1 = sns.heatmap(df)

plt.show()