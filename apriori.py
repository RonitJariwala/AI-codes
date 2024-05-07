from collections import Counter

# Defining the DataSet
data=[
    ['T1',['M','O','N','K','E','Y']],
    ['T2',['D','O','N','K','E','Y']],
    ['T3',['M','A','K','E']],
    ['T4',['M','U','C','K','Y']],
    ['T5',['C','O','O','K','E']]
]

# Confidence interval
sp = 0.6  #support threshold 60%
s=int(sp*len(data))

c=Counter()
for transaction in data:
    for item in transaction[1]:
        c[item]+=1

l=Counter()
for item,count in c.items():
    if count >= s and item != 'C4' and item != 'L4':
        l[frozenset([item])] += count
    
print('Frequent Itemsets (Size 1):')
for itemset,support in l.items():
    print(f"{list(itemset)}: {support}")
    
pl=l
pos=1
for count in range(2,4):
    nc=set()
    temp=list(pl)
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            t=temp[i].union(temp[j])
            if len(t)==count:
                nc.add(temp[i].union(temp[j]))
    nc=list(nc)
    c=Counter()
    for itemset in nc:
        c[itemset]=0
        for transaction in data:
            temp=set(transaction[1])
            if itemset.issubset(temp):
                c[itemset]+=1

    print(f'\nCandidate Itemsets (Size {count}):')
    for itemset,support in c.items():
        print(f"{list(itemset)}: {support}")
    
    l=Counter()
    for itemset,support in c.items():
        if support >= s:
            l[itemset] += support

    print(f'\nFrequent Itemsets (Size {count}):')
    for itemset,support in l.items():
        print(f'{list(itemset)}: {support}')

    if len(l)==0:
        break
    pl=l
    pos=count

print("\nFinal Frequent Itemsets:")
for itemset,support in pl.items():
    print(f"{list(itemset)}: {support}")
