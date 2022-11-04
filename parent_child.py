single_parent=[]
zero_parent=[]

def findNodesWithZeroAndOneParents(parentChildPairs):
    children = [child[1] for child in parentChildPairs]
    parent = [child[0] for child in parentChildPairs]


    for c in children:
        count= children.count(c)
        if count==1:
            single_parent.append(c)    
            
    filtered_parent = list(set(parent))
    for  p in filtered_parent:
        if p not in children:
            zero_parent.append(p)
            
    return  zero_parent, single_parent
            # print(p)       


parentChildPairs = [
    (5, 6), (1, 3), (2, 3), (3, 6), (15, 12),
    (5, 7), (4, 5), (4, 9), (9, 12), (30, 16)
]

print(findNodesWithZeroAndOneParents(parentChildPairs))