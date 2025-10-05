n = int(input())
for r in range(1,n-1):
    blue = n-r
    if r<blue and blue%r==0:
        print(r,end=" ")
