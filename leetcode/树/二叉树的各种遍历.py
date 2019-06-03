#------树的前中后序非递归遍历----------
class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#----建树----

        
#----前序----
def preOrder(Tree T):
    if T is None:
        return []
    list1 = []
    list2 = []
    list1.append(T)
    while len(list1) > 0:
        t = list1.pop()
        list2.append(t)
        if t.right not None:
            list1.append(t.right)
        if t.left not None:
            list1.append(t.left)
    return list2

#----中序----
def inOrder(Tree T):
    if T is None:
        return []
    list1 = []
    list2 = []
    while T or len(list1)>0 :
        if T :
            list1.append(T)
            T = T.left
        else:
            T = list1.pop()
            list2.append(T)
            T = T.right
    return list2

#----后序----
def postOrder(Tree T):
    if T is None:
        return []
    list1 = []
    list2 = []
    list1.append(T)
    while len(list1)>0 :
        t = list1.pop()
        list2.append(t)
        if t.left not None:
            list1.append(t.left)
        if t.right not None:
            list1.append(t.right)
    return list2[::-1]

#----层次-----
def levelOrder():
    if T is None:
        return []
    list1 = []
    list2 = []
    list1.append(T)
    while len(list1)>0 :
        t = list1[0]
        del list1[0]
        list2.append(t)
        if t.left not None:
            list1.append(t.left)
        if t.right not None:
            list1.append(t.right)
    return list2

#同样的算法，用栈作为数据结构就是后序遍历，用队列做数据结构就是层次遍历

#----层次(隔开各层)-----
def levelOrder():
    if T is None:
        return []
    list1 = [T]
    list2 = [ [T] ]
    while len(list1)>0 :
        list3 = []
        for i in list1:
            if i.left:
                list3.append(i.left)
            if i.right:
                list3.append(i.right)
        list1 = list3
        if len(list3)!=0:
            list2.append(list3)
    return list2

#二叉查找树查找
def find(data , t):
    if t is None:
        return
    else:
        while t not None:
            if data > t.val :
                t = t.right
            elif data < t.val:
                t = t.left:
            else:
                return t.val

def insert(data , t):
    if t is None:
        return
    else:
        while t not None:
            if data > t.val:
               
