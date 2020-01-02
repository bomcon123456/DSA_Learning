class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def isValidBST:
  def helper(node, lower, higher):
      # this check whether the left subtree is smaller than this
      # and the right subtree is bigger than this
      if node == None:
          return True
      if node.val <= lower or node.val >= higher:
          return False
      if not helper(node.left, lower, node.val):
          return False
      if not helper(node.right, node.val, higher):
          return False
      return True
  return helper(root, float("-inf"), float("inf"))