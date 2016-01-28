# Enter your code here. Read input from STDIN. Print output to STDOUT
original = raw_input()
sequence = raw_input()
target = 0
for i in range(0,len(original)):
    if  sequence==original[i:i+len(sequence)]:
        target=target+1
print target
