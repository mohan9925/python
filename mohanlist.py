#list
#ist
list=[1,2,2,35,5,]
print list
print len(list)
print max(list)
print min(list)


#print dir(list)



'append'
'count'
'extend'
'index'
'insert'
'pop'
'remove'
'reverse'
'sort'


list=[123,'xyz','zara','abc']
print "update list:",append(2009)

list=[p

#print ls.count(2)
#print ls.index(4)
#print ls.index(2)
#print ls(0)
#print ls.insert(2,5)
#print ls.pop()
#print ls.remove(1)
#print ls.reverse()
#print ls.sort()



mylist=[1,'a','b']
mylist.append(c)
print(mylist)

mylist=[1,'a','b']
mylist.extend([2])
print(mylist)

mylist=[1,'a','b']
mylist.insert(5,6)
print(mylist)


mylist=[1,'a','b',12,10,1]
mylist.remove(12)
print(mylist)

mylist=[1,'a','b',12,10,1]
mylist=mylist.pop()
print(mylist)


#mylist=[1,'a','b',12,10,1]
#print mylist.clear()


mylist=[1,'a','b',12,10,1]
pos=mylist.index("b")
print(pos)

#mylist=[1,'a','b',12,10,1]
#pos=mylist.count(1)


#mylist=[1,'a','b',12,10,1]
#pos=mylist.copy()
#print(pos)

mylist=[1,'a','b',12,10,1]
mylist.reverse()
print(mylist)

mylist=[10,29,3,18,0,14.12,3,4]
mylist.sort()
print(mylist)

mylist=['z','az','b','a','o']
mylist.sort(key=len)
print(mylist)

mylist=['z','az','b','a','p','za','abc','o']
mylist.sort(key=str.lower)
print(mylist)

mylist=[1,-2,-34,11,-3,29,14,-5,-93]
mylist.sort(key=abs)
print(mylist)

mylist=[("mohan",23),("tom",34),("joy",13),("ram",67),("raju",56)]
mylist.sort()
print(mylist)





language = ['Python', 'Java', 'C++', 'French', 'C']
return_value = language.pop(4)
print('Return Value: ', return_value)
print('Updated List: ', language)
