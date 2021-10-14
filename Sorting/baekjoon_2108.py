import sys
from collections import Counter

n = int(sys.stdin.readline())

arr = list()
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
print(round(sum(arr)/n))
print(arr[n//2])
temp = Counter(arr).most_common()
if n == 1:
    print(arr[0])
elif temp[0][1] != temp[1][1]:
    print(temp[0][0])
else:
    print(temp[1][0])
print(max(arr)-min(arr))