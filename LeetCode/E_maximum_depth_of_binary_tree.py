class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        depth = max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        return depth

    def maxDepth_iter(self, root):
        if root == None:
            return 0
        bfs = collections.deque([root])
        height = 0
        while bfs:
            height += 1
            for _ in range(len(bfs)):
                current = bfs.popleft()
                if current.left:
                    bfs.append(current.left)
                if current.right:
                    bfs.append(current.right)
        return height
