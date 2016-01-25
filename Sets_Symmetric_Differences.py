a = set()
b = set()
m = raw_input()
temp_a = raw_input()
for i in temp_a.split(" "):
    a.add(int(i))
n = raw_input()
temp_b = raw_input()
for x in temp_b.split(" "):
    b.add(int(x))
list_holder = []
for ii in a.difference(b):
    list_holder.append(ii)
for xx in b.difference(a):
    list_holder.append(xx)
list_holder.sort()
for i in list_holder:
    print i
