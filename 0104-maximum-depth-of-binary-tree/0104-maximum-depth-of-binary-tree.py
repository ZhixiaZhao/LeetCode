# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        # DFS: Depth First Search. Using Recursion to find the max depth
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # More specific code:
        # num_left = 1 + self.maxDepth(root.left)
        # num_right = 1 + self.maxDepth(root.right)
        # if num_left > num_right:
        #     return num_left
        # else:
        #     return num_right
    
        # BFS: Breath First Search
        # put the tree in the queue, count the level of tree, using deque()
        # count = 0
#         q = deque([root]) # append() and popleft() are used to enqueue and dequeue
#         while q:
#             count += 1
#             q_len = len(q)
            
#             for i in range(q_len):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
                    
#         return count
#         Also can use list to complete this 
#         q = [root]
#         while q:
#             count += 1
#             q_len = len(q)
            
#             for i in range(q_len):
#                 node = q.pop(0)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#         return count
        
        
        # Iterative DFS
        # using stack to every node and find the maximum depth
        stack = [[root, 1]]
        count = 0   
        while stack:
            node, depth = stack.pop()
            # if node:
            #     count = max(count, depth)
            #     stack.append([node.left, depth + 1])
            #     stack.append([node.right, depth + 1])
            count = max(count, depth)
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        return count
                
        
        