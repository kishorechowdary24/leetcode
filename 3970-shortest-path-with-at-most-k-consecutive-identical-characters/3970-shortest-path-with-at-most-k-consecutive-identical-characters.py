import heapq
from collections import defaultdict

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        pq = [(0, 0, 1)]
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        dist[0][1] = 0

        while pq:
            cost, node, count = heapq.heappop(pq)

            if node == n - 1:
                return cost

            if cost > dist[node][count]:
                continue

            for nei, weight in graph[node]:

                if labels[node] == labels[nei]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[nei][new_count]:
                    dist[nei][new_count] = new_cost
                    heapq.heappush(pq, (new_cost, nei, new_count))

        return -1