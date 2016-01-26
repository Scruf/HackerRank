import collections
N = int(raw_input())
set_ph = {}
list_t = []
for i in range(N):
    name = raw_input()
    grade = float(raw_input())
    set_ph.update({name:grade})
for s in set_ph:
    list_t.append(set_ph[s])
list_t.sort()
lowest_score = list_t[1]
for key,value in set_ph.items():
    if value == lowest_score:
        print key

    


                
