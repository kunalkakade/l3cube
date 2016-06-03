
import os
import hashlib
from  Tkinter import *
from tkFileDialog import askdirectory
repeat=[]
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def deletefile(delist):
    for i in delist:
        os.remove(i)

def mergefile(merglist):
    outputfile=raw_input("enter the output file path:-")
    with open(outputfile, 'w') as outfile:
        for fname in merglist:
            with open(fname) as infile:
                outfile.write(infile.read())


class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)
        else:
            #print currentNode.payload ,"exitssdsadmsal"
            repeat.append(currentNode.payload)
            repeat.append(val)
            #print currentNode.payload ,"  \n"

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

kunal = BinarySearchTree()
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askdirectory(initialdir='/home/kunal/git') # show an "Open" dialog box and return the path to the selected file
        #print(filename)
for dirname, dirnames, filenames in os.walk(filename):
    for filename in filenames:
                #print os.path.join(dirname, filename) ,md5(os.path.join(dirname, filename))
                kunal[md5(os.path.join(dirname, filename))]= os.path.join(dirname, filename)


print "Following are the dublicate files:-"
repeat=list(set( repeat))
for p in repeat: print p

choice=raw_input("enter your choice \n 1) delete all the files \n 2)delete selected files  \n 3)merge all files \n 4)merge selected files ")

if choice=="1":
    deletefile(repeat)
elif choice=="2":
    count=raw_input("enter the number of files to be deleted:-")
    delist=raw_input("enter the list of files to be deleted:-").split()
    deletefile(delist)
elif choice=="3":
    mergefile(repeat)
elif choice=="4":
    count=raw_input("enter the number of files to be merged:-")
    merglist=raw_input("enter the list of files to be merged:-").split()
    mergefile(merglist)
