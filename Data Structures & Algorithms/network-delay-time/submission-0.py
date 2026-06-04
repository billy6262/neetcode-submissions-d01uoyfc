
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        dist = {n:float("inf") for n in range(1,n + 1)} #table of potential distances to each node from k
        edges = {n:[] for n in range(1,n + 1)}  #edge look up dict by source node

        dist[k] = 0
        for src,dest,ti in times:
            edges[src].append((ti,dest))
            
        minheap = [(0, k)]

        while minheap:
            cost, cur = heapq.heappop(minheap)
            dist[cur] = min(dist[cur], cost)

            for edge in edges[cur]:
                heapq.heappush(minheap,(edge[0] + cost, edge[1]))

            edges[cur] = []

        ret = max(dist.values())

        if ret == float("inf"):
            return -1

        return ret


        

