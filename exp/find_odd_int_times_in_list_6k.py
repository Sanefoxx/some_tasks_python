from collections import Counter

a = dict(Counter([5 ,3 ,3 ,5 , 3]))

for key, value in a.items():
    if value % 2 == 1:
        print(key)

