
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodeParent = [i for i in range(len(edges) + 1)]


        def find(n): #compresses the path from the leaf so the leaf is dirtectly attached to the root
            parent = nodeParent[n]

            while parent != nodeParent[parent]:
                nodeParent[parent] = nodeParent[nodeParent[parent]]
                parent = nodeParent[parent]
            return parent

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False

            nodeParent[p1] = p2
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1,n2]