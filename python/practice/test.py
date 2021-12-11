class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def array_to_bst(array_nums):
    if not array_nums:
        return None
    mid_num = len(array_nums)//2
    node = Node(array_nums[mid_num])
    node.left = array_to_bst(array_nums[:mid_num])
    node.right = array_to_bst(array_nums[mid_num+1:])
    return node
        
def insert(node, value):
    if node == None:
        return Node(value)
    if value > node.val:
        node.right = insert(node.right, value)
    elif value < node.val:
        node.left = insert(node.left, value)
        return node
  
def maxDepth(node): 
    if node is None: 
        return 0  
    else : 
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right) 
        if (lDepth > rDepth): 
            return lDepth + 1
        else: 
            return rDepth + 1
  
  
# 
arr = [5,4,6,2,3,4]
root = array_to_bst(arr) 
print(maxDepth(root) - 1)