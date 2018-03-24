

#{ key:value,key:value }
# 'clear',
 #'copy', 
 #fromkeys',
 #'get',
 #'has_key',
 #'items',
 #'iteritems',
 #'iterkeys',
 #'itervalues', 
 #'keys', 
 #'pop',
 ##'popitem',
 #'setdefault', 
 #'update',
 #'values', 
 #'viewitems',
 #'viewkeys',
 #'viewvalues']
['keys1', 'keys3', 'keys2']  
 # 1 st methed
  
a={'name':'apple','id':100,'branch':'cat'}
print a
print dir(a) 
  
mohan={'mm1':10,'nn2':2,'ss3':4}  
mykeys=mohan.keys()                                          #keys#
print(mykeys)
myvalues=mohan.values()                                      #values#
print(myvalues)
myitems=mohan.items()                                        #items#
print(myitems)


mohan={'jack':15,'raja':17,'maohan':19}                      #clear
mohan.clear()
print(mohan)

mohan={'jack':15,'raja':17,'maohan':19}                     #copy
mohan2=mohan.copy()
print(mohan)
print(mohan2)

mytuple=(1,2,3,4,5,6,7,8)                                #fromkeys(seql,value
mydict=dict.fromkeys(mytuple,3)
print(mydict)

mylist=[1,2,3,4,5,6]                                       #fromkeys(seql,valuel)
mydict=dict.fromkeys(mytuple,20)
print(mydict)


mohan={1:"mohan",14:"sam",22:"roy"}                           #get (key[default])
myvalue=mohan.get(22 )
print(myvalue)


myvalue=mohan.get(50)
print(myvalue)

myvalue=mohan.get(10,0)
print(myvalue)

mohan={'keys1':10,'keys2':2,'keys3':4}   #value deleteed but value showing       #pop(key[,dfault]) 
mykeys=mohan.pop('keys3')
print(mykeys)


mohan={1:"mohan",14:"sam",22:"roy"}                                     #popitem
myrm=mohan.popitem()
print(myrm)
myrm=mohan.popitem()
print(myrm)

mohan={'jack':15,'raja':17,'maohan':19}                                  #setdefault            
myval=mohan.setdefault('jack',16)
print(myval)
myval=mohan.setdefault('mohan',16)
print(myval)


mohan={'raja':23}                                                         #update
mohan2={'ragu':40}
mohan.update(mohan2)
print(mohan)


mohan={'keys':10,'keys':2,'keys':4}
mykeys=mohan.keys()
print(mykeys)
myvalues=mohan.values()
print(myvalues)
myitems=mohan.items()
print(myitems)

mystr1="rAMAMOHANREDDY"
print mystr1.swapcase()
mystr1="Ramamohanreddy"
print mystr1.swapcase()
mystr1="RAMAMOHAN REDDY"
print mystr1.swapcase()


a="mystring"
print(a)



