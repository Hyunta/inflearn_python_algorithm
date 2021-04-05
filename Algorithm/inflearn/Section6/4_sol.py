import sys
def DFS(L,sum):
    if sum > total//2:
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+m[L])
        DFS(L+1, sum)



if __name__ =="__main__":
    n = int(input())
    m = list(map(int, input().split()))
    total = sum(m)
    DFS(0,0)
    print("NO")