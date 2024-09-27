def fun(lst):
 cat1=[]
 cat2=[]
 for i in lst:
   if len(i) > 6:
    cat1.append(i) 
   else:
    cat2.append(i)
 return cat1,cat2

lst=["pankaj","nakshatra","naveen"]
cat1,cat2=fun(lst)
print(cat1,cat2)