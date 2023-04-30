Need to learn tree traversal.
Be careful: the different between append and + in list.
​
More efficient answer:
```
return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
```
​
Another answer:
```
class Solution:
def inorderTraversal(self, root: TreeNode) -> List[int]:
res, stack = [], [(root, False)]
while stack:
node, visited = stack.pop()  # the last element
if node:
if visited:
res.append(node.val)
else:  # inorder: left -> root -> right
stack.append((node.right, False))
stack.append((node, True))
stack.append((node.left, False))
return res
```
​
​