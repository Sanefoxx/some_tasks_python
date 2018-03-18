import random
def bing():
	b = random.sample(range(1,15), 5)
	i = random.sample(range(16,30), 5)
	n = random.sample(range(31,45), 4)
	g = random.sample(range(46,60), 5)
	o = random.sample(range(61,75), 5)
    
	for x, item in enumerate(b):
		b[x] = "B" + str(item)
        
	for x, item in enumerate(i):
		i[x] = "I" + str(item) 

	for x, item in enumerate(n):
		n[x] = "N" + str(item) 

	for x, item in enumerate(g):
		g[x] = "G" + str(item) 

	for x, item in enumerate(o):
		o[x] = "O" + str(item) 

	return b + i + n + g + o

print(bing())