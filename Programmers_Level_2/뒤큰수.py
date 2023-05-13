def find_nge_s(arr):
    n = len(arr)
    s = []
    res = [-1] * n
    for i in range(n-1, -1, -1):
        while s:
            if s[-1] > arr[i]:
                res[i] = s[-1]
                break
            else:
                s.pop()
        s.append(arr[i])
    for i in range(n):
        print(f"{arr[i]} --> {res[i]}")