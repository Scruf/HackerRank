# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import chain, combinations

def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True

def powerset(iterable):
    xs = list(iterable)
    return chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1) )
counter = 0
sum_t = 0
cities = int(raw_input())
list_t = map(int, raw_input().split(" "))
for l in powerset(list_t):
    sum_t = sum(l)
    if isPrime2(sum_t):
        counter=counter+1
        
print counter
