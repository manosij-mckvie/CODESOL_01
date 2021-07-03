import re

t = int(input())
i = 0
l = list()
while i < t:
    n,k = map(int,input().split())
    s = input()
    l = re.findall("0+",s)
    if len(l) == 0:
        print("NO")
        i+=1
        continue
    if len(max(l)) >= k:
        print("YES")
        i+=1
        continue
    for j in range(len(l)):
        if len(l[j]) < k and len(l[j]) > 0:
            k = 2 * (k-len(l[j]))
        else:
            k=0
            break
    if k > 0:
        print("NO")
    else:
        print("YES")
    l.clear()
    i+=1
