# 트리 구현
class Node:
  def __init__(self, value = 0, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right
class BinaryTree:
  def __init__(self):
    self.root = None
bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5)
bt.root.right.right = Node(value = 6)

# BFS
from collections import deque
def bfs(root):
  visited = []
  if root is None:
    return visited
  q = deque()
  q.append(root)
  while q:
    cur_node = q.popleft()
    visited.append(cur_node.value)
    if cur_node.left:
      q.append(cure_node.left)
    if cur_node.right:
      q.append(cur_node.right)
  return vistied

# DFS 접근
def dfs(cur_node):
  if cur_node is None:
    return
  dfs(cur_node.left)
  dfs(cure_node.right)

# 전위순회
def preorder(root):
  if root is None:
    return
  print(root.value)
  preorder(root.left)
  preorder(root.right)

# 중위순회
def inoder(root):
  if root is None:
    return
  inoder(root.left)
  print(root.value)
  inoder(root.right)

# 후위순회
def postorder(root):
  if root is None:
    return
  postorder(root.left)
  postorder(root.right)
  print(root.value)
