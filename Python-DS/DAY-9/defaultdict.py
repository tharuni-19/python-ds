#from collections import defaultdict
#a=defaultdict(list)
#words = ["cat","apple","rat","orange","dog","banana"]
#for word in words:
#   a[len(word)].append(word)
#print(list(a.values()))              example for default dictionary



#grouping anagram example
from collections import defaultdict  
grp_ana=defaultdict(list)
words=["eat","tea","ate","nat","bat","cat"]
for w in words:
    key=''.join(sorted(w))
    grp_ana[key].append(w)
print(list(grp_ana.values()))
        
       
       