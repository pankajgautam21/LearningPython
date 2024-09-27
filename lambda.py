#lambda function
f=lambda a,b:a+b
print(f(4,5))
#filter,map and reduce
lst=[10,13,15,18,23,45,67,86]
from functools import reduce
sum=0
final=reduce(lambda a,b:a+b,tuple(map(lambda i:i+2,tuple(filter(lambda i:i%2==0,lst)))))
print(final)