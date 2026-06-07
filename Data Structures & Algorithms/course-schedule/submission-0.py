class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        edges = dict()
        self.ret = True

        for edge in prerequisites:
            edgeList = edges.get(edge[1], [])
            edgeList.append(edge[0])
            edges[edge[1]] = edgeList

        def DFS(path, course):
            if course in path:
                self.ret = False
                return False
            if course in visited:
                return True
            
            path.add(course)
            if course in edges:
                for edge in edges[course]:
                    if not DFS(path, edge):
                        return False
            path.remove(course)
            visited.add(course)
            return True

        for i in range(0, numCourses):
            if not self.ret:
                break
            DFS(set(), i)
        return self.ret