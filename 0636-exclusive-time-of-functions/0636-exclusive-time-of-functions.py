class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev = 0

        for log in logs:
            fid, typ, t = log.split(':')
            fid = int(fid)
            t = int(t)

            if typ == "start":
                if stack:
                    ans[stack[-1]] += t - prev
                stack.append(fid)
                prev = t
            else:
                ans[stack.pop()] += t - prev + 1
                prev = t + 1

        return ans