#set is a donot duplicate
#  {}
   #difference'
# 'difference_update',
 #'discard',
 #'intersection',
 #'intersection_update',
 #'isdisjoint',
 #'issubset',
 #'issuperset',
 #'pop',
 #'remove',
 #'symmetric_difference', 
 #'symmetric_difference_update',
 #'union',
 #'update']

set={1,2,3,4,5,6,7,8,}
print set
print dir(set)
set1={(1,2,3),"mohan","raju",(3.14,10.5)}
print set1

set2={1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,}
print set2

a={}
print(a)

myset={1,3}
myset.add(2)
print(myset) 
myset.update([4,5,6,7])
print myset


set1={1,2,3,"mohan","raju",3.14,10.5,2,"mohan"}
print(set1)
#set2=set([1,2,3,"mohan"])
print(set2)
set2.add(5)
print(set2)
set2.update([7,8,9,"chandu","vara"])
print(set2)
set2.discard("vara")
print(set2)
set2.remove(1)
print (set2)


myset={1,3}
myset.add(2)
print(myset)  
myset.discard(2)
print myset

myset1={"suri","mohan","reddy"}
print myset1.pop()

myset3={"suri","naidu",(12,13,14)}
myset3.clear()
print myset3






myset={1,2,3,4,5,6}
print(myset)


myset2={1,2,3,4,"a","b"}
print(myset2)

myset3={(1,2),(3,4),(1,3)}
print(myset3)


myset={1,2,3,4,5}
myroz=frozenset(myset)
print(myroz)

myset={1,2,3,4}
myset.add(12)
print(myset)

myset.add((1,2,33,"mohan"))
print(myset)
  
myset={1,2,3,4,5,}
print(myset)

myset.clear()
print(myset)


myset={1,2,3,4,5,6,}
print(myset)

myset2=myset.copy()
print(myset2)

myset2.add(10)
print(myset2)
print(myset)

myset={1,2,3,4,5,}
myset1={2,4,6}
myset2={3}

myset4=myset.difference(myset1)
print(myset4)

myset5={1,2,3,4,5}
myset6=myset5.difference(myset1,myset3)
print(myset6)

myset={1,2,3,4,5,}
myset1={2,4,6}


myset.difference_update(myset1)
print(myset)

myset4={1,2,3,4,5,}
myset4.difference_update(myset,myset1)
print(myset4)


A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}
result = A.difference_update(B)
print('A = ', A)
print('B = ', B)
print('result = ', result)


vowels = {'a', 'e', 'i', 'u'}
vowels.add('o')
print('Vowels are:', vowels)
vowels.add('a')
print('Vowels are:', vowels)

