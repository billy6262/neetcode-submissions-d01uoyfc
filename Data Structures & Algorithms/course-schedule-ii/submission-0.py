class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for c, p in prereq:
            adj[p].append(c)

        visited = set()
        
        arr = []
        cycle = [False]

        def DFS(course, path):
            if cycle[0]:
                return
            if course in path:
                cycle[0] = True
                return
            if course in visited:
                return
            path.add(course)
            dep = adj[course]
            for c in dep:
                DFS(c,path)
            path.remove(course)
            visited.add(course)
            arr.append(course)

        for c in range(numCourses):
            if c not in visited:
                DFS(c,set())

        if cycle[0]:
            return []
         
        return arr[::-1]