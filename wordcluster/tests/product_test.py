import wordcluster
mylist = ['vanlı','vanda','vansız','vandan','vanlılar','mut','olmut','muttu','vanlılardan','muttulamak']
#for treshold in range(1,5):
treshold = 3  
wcu = wordcluster.WordCluster(mylist,treshold)
cluster_categories = wcu.find_cluster_categories()
categorized_words =wcu.categorize_all_words(cluster_categories)
print(categorized_words)


