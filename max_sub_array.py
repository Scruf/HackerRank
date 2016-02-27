import itertools
def max_subarray(A):

   def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        print max_ending_here
        max_so_far = max(max_so_far, max_ending_here)
        print max_so_far
    return max_so_far

a0 = int(raw_input())
for i in range(0,a0):
    num = int(raw_input())
    arr = map(int,raw_input().split(" "))
    max_non = 0
    max_continius= max_subarray(arr)
    for i in range(1,num+1):
        tup = itertools.permutations(arr,i)
        list = map(sum,tup)
        list.sort()

        if list[len(list)-1]> max_non:
            max_non = list[len(list)-1]
    print max_non



