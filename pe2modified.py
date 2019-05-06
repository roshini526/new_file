def fib(n):
	a, b = 0, 1
	while a < n:
		yield a
		a, b = b, a + b
	return a 
print(sum(filter(lambda x:x % 2 == 0,fib(4000000)))) # we can aslo write as  li = [x for x in fib(4000000) if x % 2 == 0]
																				   #print(sum(li))
