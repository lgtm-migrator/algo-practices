from typing import List

class ListNode:
  
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

    
def preorder(root: ListNode) -> List[int]:
  ret = []
  stack = [root]
  
  while stack:
    node = stack.pop()
    if node:
      ret.append(node.val)
      stack.append(node.right)
      stack.append(node.left)
      
  return ret

def inorder(root: ListNode) -> List[int]:
  ret, stack = []
  
  while True:
    while root:
      stack.append(root)
      root = root.left
    if not stack:
      return ret
    node = stack.pop()
    ret.append(node.val)
    root = root.right
      
