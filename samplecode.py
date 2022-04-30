# x=(12,13,14,15,"hello","hii")
#
# y=list(x)
#
# y.append("112")
# y.insert(1,"toogood")
# print(y.index(13))
# print(y)


u=100005
def minChanges(arr, n, k):
    arr.sort(reverse=False)
    freq=[0 for i in range(u)]
    p=0
    freq[p]=1
    for i in range(1, n, 1):
        if (arr[i]==arr[i-1]):
            freq[p]+=1
        else:
            p+=1
            freq[p]+=1
    freq.sort(reverse=True)
    ans=0
    for i in range(k, p+1,1):
        ans+=freq[i]
    return ans
if __name__ == "__main__":
    arr=[1, 2, 7, 8, 2, 3, 2, 3]
    n=len(arr)
    k=4
    print(minChanges(arr, n, k))