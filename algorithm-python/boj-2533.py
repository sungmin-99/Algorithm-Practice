import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(x):
    visit[x] = 1
    dp[x][0] = 1
    for i in graph[x]:
        if not visit[i]:
            dfs(i)
            dp[x][0] += min(dp[i][0], dp[i][1])
            dp[x][1] += dp[i][0]

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dp = [[0,0] for _ in range(n + 1)]
visit = [0] * (n + 1)

dfs(1)
print(min(dp[1][0], dp[1][1]))