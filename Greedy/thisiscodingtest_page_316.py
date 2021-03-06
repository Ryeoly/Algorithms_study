def solution(food_times, k):
    ft_len = len(food_times)

    if k >= sum(food_times):    # 방송이 정지 되기전에 다 먹어 더이상 먹을 것이 없는 경우
        return -1
    if k < ft_len:              # 원소 크기가 최소 1이니까, 한바퀴도 못 돌았을 때 정전이 나는 경우
        return k+1
    if k == ft_len:             # 정확히 한바퀴 돌고, 정전이 난 경우
        return 1

    # 이분 탐색으로 어느 숫자가 k에 가깝게 만들어 주는지 찾음
    start = 1
    end = 100000000

    while start <= end:
        mid = int((start+end)/2)
        count = 0
        for i in range(ft_len):
            if food_times[i] < mid:
                count += food_times[i]
            else:
                count += mid
        if count > k:
            end = mid -1
        else:
            start = mid + 1

    # 여기서 찾은 크기로 list 초기화
    mid = int((start + end) / 2)
    remain = 0
    for i in range(ft_len):
        if food_times[i] <= mid:
            remain += food_times[i]
            food_times[i] = 0
        else:
            food_times[i] -= mid
            remain += mid

    # 먹을 것이 남아 있는 음식들을 확인해서 최종적으로 먹기 시작해야할 음식의 position을 찾음
    k -= remain
    for i in range(ft_len):
        if food_times[i] != 0:
            k -= 1
        if k == -1:
            return i+1

print(solution([3,1,2], 5))