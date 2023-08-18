class Bintreenode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST:
    def __init__(self,list=None):
        self.root = None
        if list:
            for val in list:
                self.insert(val)

    def zhongxu(self,root):
        if root:
            self.zhongxu(root.lchild)
            print(root.data,end=",")
            self.zhongxu(root.rchild)

    def insert(self,val):
        p = self.root
        if not p: #空树
            self.root = Bintreenode(val)
            return
        while True:
            if val<p.data:
                if not p.lchild:
                    p.lchild = Bintreenode(val)
                    p.lchild.parent = p
                    return
                else:
                    p = p.lchild
            elif val>p.data:
                if not p.rchild:
                    p.rchild = Bintreenode(val)
                    p.rchild.parent = p
                    return
                else:
                    p = p.rchild
            else:
                return

    def serch(self,val):
        p = self.root
        if not p:
            return None
        while p:
            if val<p.data:
                p = p.lchild
            elif val>p.data:
                p = p.rchild
            else:
                return p
        return None

    def __remove_1(self,node):   #要删除的节点没有任何子节点
        if not node.parent: #删除节点是根节点
            self.root = None
        #不是根节点：
        #如果该节点是父亲的左孩子
        if node.parent.lchild:
            if node.parent.lchild.data == node.data:
                node.parent.lchild = None
                return
            #如果该节点是父亲的右孩子
            #elif node.parent.rchild.data == node.data:
        node.parent.rchild = None

    def __remove_21(self,node): #要删除的节点有一个左孩子
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        #不是根节点
        #node是父亲的左孩子
        if node.parent.lchild:
            if node.parent.lchild.data == node.data:
                node.parent.lchild = node.lchild
                node.lchild.parent = node.parent
                return
            #elif node.parent.rchild.data == node.data:
        node.parent.rchild = node.lchild
        node.lchild.parent = node.parent

    def __remove_22(self,node): #要删除的节点有一个右孩子
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        #不是根节点
        if node.parent.lchild:
            if node.parent.lchild.data == node.data:
                node.parent.lchild = node.rchild
                node.rchild.parent = node.parent
                return
            #elif node.parent.rchild.data == node.data:
        node.parent.rchild = node.rchild
        node.rchild.parent = node.parent

    def delete(self,val):
        if not self.root:
            return False
        node = self.serch(val)
        if not node.lchild and not node.rchild:
            self.__remove_1(node)
        elif not node.rchild:
            self.__remove_21(node)
        elif not node.lchild:
            self.__remove_22(node)
        else:
            flag = node.rchild
            while flag.lchild:
                flag = flag.lchild
            node.data = flag.data
            if flag.rchild:
                self.__remove_22(flag)
            else:
                flag.parent.lchild =None


Tree1 = BST([4,6,7,9,2,1,3,5,8])
Tree1.zhongxu(Tree1.root)
print()
#print(Tree1.serch(9).parent.rchild.data)
Tree1.delete(9)
Tree1.delete(8)
Tree1.delete(7)
Tree1.delete(3)
Tree1.zhongxu(Tree1.root)







