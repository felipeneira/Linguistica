import pandas as pd
import matplotlib.pyplot as plt
import random
from collections import defaultdict
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram

    
# =============================================================================
# 
# =============================================================================

def hamming(lengua1, lengua2):
    
    ## rasgos
    features_lengua1= D[lengua1]
    features_lengua2= D[lengua2]
    
    ## hamming!
    d=0
    n=0
    for feature in features_lengua1:
        if feature in features_lengua2: 
            if features_lengua1 != features_lengua2:
                d += 1.0
            n += 1.0
            
    return d/n



# =============================================================================
# 
# =============================================================================

ms = pd.read_csv("marking_strategy.csv", sep=";")
cs = pd.read_csv("constructional_structure.csv", sep=";")


languages = [ms.iloc[x].to_list() for x in range(0,52)]

D = {item[1]: item[2:12] for item in languages}

hamming("Ancash Quechua", "Cajamarca Quechua")
D["Ancash Quechua"]

for item in D["Ancash Quechua"]:
    print(item)
# =============================================================================
# class MS:
#     def __init__(self, language):
#         self.family = language[0]
#         self.language = language[1]
#         self.prefix = language[2]
#         self.suffix = language[3]
#         self.circumfix = language[4]
#         self.preverbal_clitic = language[5]
#         self.postverbal_clitic = language[6]
#         self.preverbal_particle = language[7]
#         self.postverbal_particle = language[8]
#         self.preverbal_aux = language[9]
#         self.postverbal_aux = language[10]
#         self.unclear = language[11]
#         self.more_than_one = language[12]
# 
# languages = [MS(item) for item in languages]
# =============================================================================


# =============================================================================
# 
# =============================================================================

languages[1][2:]

binary_features = np.array([language[2:] for language in languages])

# Perform hierarchical clustering using Ward linkage
clusters = linkage(binary_features, method='ward')

# Plot the dendrogram
plt.figure(figsize=(10, 6))
dendrogram(clusters, labels=[language[1] for language in languages], orientation='top')
plt.title('Dendrogram')
plt.xlabel('Languages')
plt.ylabel('Distance')
plt.show()
