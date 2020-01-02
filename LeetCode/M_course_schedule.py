import collections

class Solution:
    def canFinish_v1(self, numCourses, prerequisites):
        def dfs(vertex):
            state[vertex] = 1
            for neighbor in adj_list[vertex]:
                if state[neighbor] == 0:
                    if not dfs(neighbor):
                        return False
                return False
            state[vertex]=2
            return True

        state = [0] * numCourses
        adj_list = collections.defaultdict(list)
        for edge in prerequisites:
            adj_list[edge[1]].append(edge[0])
        for i in range(0, numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False
        return True

    def canFinish_99percent(self, numCourses, prerequisites):
        def dfs(vertex):
            state[vertex] = 1
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    if state[neighbor] == 0:
                        if not dfs(neighbor):
                            return False
                    elif state[neighbor] == 1:
                        return False
            state[vertex]=2
            return True

        state = [0] * numCourses
        adj_list = collections.defaultdict(list)
        for edge in prerequisites:
            adj_list[edge[1]].append(edge[0])
        for i in range(0, numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False
        return True
