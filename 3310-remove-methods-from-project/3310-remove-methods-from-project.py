class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        # Step 1: Build directed graph
        graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)

        # Step 2: Find all suspicious methods reachable from k
        suspicious = set()
        stack = [k]

        while stack:
            method = stack.pop()

            if method in suspicious:
                continue

            suspicious.add(method)

            for next_method in graph[method]:
                if next_method not in suspicious:
                    stack.append(next_method)

        # Step 3: Check if any non-suspicious method
        # invokes a suspicious method
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                # Cannot remove suspicious methods
                return list(range(n))

        # Step 4: Remove all suspicious methods
        return [method for method in range(n) if method not in suspicious]