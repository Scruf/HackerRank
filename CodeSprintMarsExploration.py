s = raw_input().strip()
i = 0
target = 0
temp =0
default = "SOS"
while i<len(s):
    for x in s[i:i+3]:
        if x!=default[temp]:
            target=target+1
            temp=temp+1
        else:
            temp=temp+1
    temp=0
    i=i+3
print target
