N = int(input())
files = {}
extend = []
for i in range(N):
    file = input()
    file = file.split('.')
    if file[1] not in files:
        files[file[1]] = 1
        extend.append(file[1])
    else:
        files[file[1]] +=1

extend.sort()
for e in extend:
    print(e, end=' ')
    print(files[e])
#print(files)
#print(extend)