class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        # Step 1: Build graph
        graph = {}

        for a, b, d in roads:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b, d))
            graph[b].append((a, d))

        visited = set()

        ans = float('inf')

        def dfs(city):
            nonlocal ans

            visited.add(city)

            for neighbour, distance in graph[city]:

                # Update minimum road
                ans = min(ans, distance)

                if neighbour not in visited:
                    dfs(neighbour)

        dfs(1)

        return ans