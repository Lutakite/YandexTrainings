#[key, [left], [right]]
#[5, [2, None, [3, None, None]], [7, None, [8, None, None]]]

def printTree(tree):
    if tree[1] != None:
        printTree(tree[1])
    print(tree[0])
    if tree[2] != None:
        printTree(tree[2])
               
def printLeaves(tree):
    if tree[1] != None:
        printLeaves(tree[1])
    if tree[1] == None and tree[2] == None:
        print(tree[0])
    if tree[2] != None:
        printLeaves(tree[2])

def findMax(tree, father):
    if tree[2] == None:
        return (tree[0], father)
    return findMax(tree[2], tree[0])
    
def find2Max(tree, father):
    if tree[2] == None:
        if tree[1] != None:
            return findMax(tree[1], tree[0])
        else:
            return (father, father)
        #return (tree[0], father)
    return find2Max(tree[2], tree[0])
    
            
def find(tree, x):
    if len(tree) == 0:
        return 0
    if tree[0] == x:
        return 1
    if tree[0] < x:
        if tree[2] == None:
            return 0
        else:
            r = find(tree[2], x)
            if r == 0:
                return 0
            return 1 + r
    if tree[0] > x:
        if tree[1] == None:
            return 0
        else:
            r = find(tree[1], x)
            if r == 0:
                return 0
            return 1 + r
    
def add(tree, x):
    if len(tree) == 0:
        tree = [x, None, None]
    if tree[0] < x:
        if tree[2] != None:
            tree[2] = add(tree[2], x)
        else:
            tree[2] = [x, None, None]
    if tree[0] > x:
        if tree[1] != None:
            tree[1] = add(tree[1], x)
        else:
            tree[1] = [x, None, None]    
    return tree

def hight(tree):
    if tree[1] == None and tree[2] == None:
        return 1
    if tree[1] == None:
        return 1 + hight(tree[2])
    if tree[2] == None:
        return 1 + hight(tree[1])
    return 1 + max(hight(tree[1]), hight(tree[2]))

m = list(map(int, input().split()))

resultTree = list()
for i in m:
    if i == 0:
        break
    resultTree = add(resultTree, i)

printLeaves(resultTree)