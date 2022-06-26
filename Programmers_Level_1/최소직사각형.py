
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

def solution(sizes):
    answer = 0
    max_size=max(map(max, sizes))
    idx =0
    for size in sizes:
        if max_size == size[0]:
            idx = 0
        elif max_size ==size[1]:
            idx = 1
    print(idx)        
    re_idx =-1
    if idx ==0:
        re_idx = 1
    else:
        re_idx = 0
    re_=[]
    for size in sizes:
        if size[idx] < size[re_idx]:
            tmp = size[idx]
            size[idx] = size[re_idx]
            size[re_idx] = tmp
        re_.append(size[re_idx])    

    re_.sort()
    re_.sort()
    max2 = re_[len(re_)-1]
    print(max_size)
    return max_size * max2    