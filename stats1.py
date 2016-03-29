# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
a0 = int(raw_input())
list_t = map(int, raw_input().split())
mean = np.mean(list_t)
median = np.median(list_t)
min_element = np.min(list_t)
std = np.std(list_t)
if mean.dtype==np.int64:
    print mean
else:
    print round(mean,1)
if median.dtype == np.int64:
    print median
else:
    print round(median,1)
print min_element
if std.dtype == np.int64:
    print std
else:
    print round(std,1)
