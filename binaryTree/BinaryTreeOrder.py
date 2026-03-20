import BinaryTree 
t = BinaryTree.Tree()
t.add(7);t.add(2);t.add(1);t.add(8);t.add(4);t.add(1);t.add(3);t.add(5);t.add(9);t.add(0)


def preoder(root):
    _preoder(root)
def _preoder(current):
    print(current.value)
    if(current.left != None):
        _preoder(current.left)
    if(current.right != None):
        _preoder(current.right)
def postorder(root):
    _postorder(root)
def _postorder(current):
    if(current.left != None):
        _postorder(current.left)
    print(current.value)
    if(current.right != None):
        _postorder(current.right)

def inorder(root):
    _inorder(root)
def _inorder(current):
    if(current.left != None):
        _inorder(current.left)
    if(current.right != None):
        _inorder(current.right)
    print(current.value)

preoder(t.root)
