from collections import deque

graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

## BFS 메서드 정의

def bfs(graph, node, visited) :
    #큐 구현을 위한 deque 라이브러리 활용
    queue = deque([node])

    #현재 방문한 노드 처리
    visited[node] = True

    #큐가 완전히 돌 떄까지 반복
    while queue:
        #큐에 삽입된 순서대로 노드 하나씩 꺼내기
        v = queue.popleft()
        #탐색 순서 출력
        print(v, end=" ")

        #현재 방문처리 중인 노드에서 방문하지 않은 인접 노드 모두 큐에 삽입

        for i in graph[v]:
            if not(visited[i]) :
                queue.append(i)
                visited[i] = True

