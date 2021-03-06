import sys
import itertools
from copy import deepcopy

def count(arr, combi, two_values, n, m):  # 2가 퍼져서 0인 안전지대 count하는 함수
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 파이썬 특성상 깊은 복사를 이용해야 한다.
    temp = deepcopy(arr)
    two_que = deepcopy(two_values)
    # 벽 3개 설치
    for i in combi:
        temp[i[0]][i[1]] = 1

    # 바이러스 전파 시뮬레이션
    while two_que:
        col, row = two_que.pop()

        for i in range(4):
            n_c, n_r = col + dy[i], row + dx[i]
            if 0 <= n_r < m and 0 <= n_c < n and temp[n_c][n_r] == 0:
                temp[n_c][n_r] = 2
                two_que.append((n_c, n_r))

    # 안전 지대 카운트
    result = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                result += 1

    return result


n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):  # 복잡도 n
    arr.append(list(map(int, sys.stdin.readline().split())))

zero_values = list()
two_values = list()
for i in range(n):  # 복잡도 n*m
    for j in range(m):
        if arr[i][j] == 0:
            zero_values.append((i, j))
        elif arr[i][j] == 2:
            two_values.append((i, j))

combis = list(itertools.combinations(zero_values, 3))

results = list()
# 벽을 설치하는 경우들을 하나씩 확인
for i in combis:
    results.append(count(arr, i, two_values, n, m))
print(max(results))