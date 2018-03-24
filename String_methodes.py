#'capitalize'
'center'
'count'
#'decode'
#'encode'
'endswith'
#'expandtabs'
'find'
#'format',
'index'
'isalnum'
'isalpha'
'isdigit'
'islower'
'isspace'
'istitle'
'isupper'
'join'
'ljust'
'lower'
'lstrip'
'partition'
'replace'
'rfind'
'rindex'
'rjust'
'rpartition'
'rsplit'
'rstrip'
'split'
'splitlines'
'startswith'
'strip'
'swapcase'
'title'
'translate'
'upper'
#'zfill'


a="mohan"
print a.upper()






a='mohan '
print a.capitalize()
print a.capitalize()
print a.capitalize()



a='this is our string'
print a.center(50)
print a.center(50,'-')
print a.center(30,'^')



a='this is our string'
print a.count('t')
print a.count('s')
print a.count('i')



a= 'this is our string'
print a.endswith('g')
print a.endswith('z')
print a.endswith('g',14)


a='this is your string'
print a.find('g')
print a.find('z')
print a.find('s')



a='This is a string th'
print a.index('string')
print a.index('is')
print a.index('th')



a='1'
print a.isalnum()
b='1a'
print b. isalnum()
c='1a!'
print c.isalnum()




a='abcd'
print a.isalpha()
b='abcd123'
print b.isalpha()
c='abcd 123'
print c.isalpha()




a= 'abcd'
print a.isdigit()
b='123g'
print b.isdigit()
c='1234567'
print c.isdigit()



a='RAMAMOHANREDDY'
print a.islower()
b='ramamohanrerddy'
print b.islower()
c='ram12'
print c.islower()


a=' '
print a.isspace()
b='_'
print b.isspace()
c='4'
print b.isspace()


a='ramamohan'
print a.istitle()
c='Mohaan'
print c.istitle()
e='mohan'
print e.istitle()

b='mohan'
print b.isupper()
p='mohan'
print p.isupper()
d='REDDY'
print d.isupper()


a='my name is ramamohanreddy'
print'just____',a.ljust(50,'w')
b='mohan'
print b.ljust(30,'2')
c='reddy'
print c.ljust(20,'8')




c='RAMAMOHANREDDY'
print c.lower()
d='ramamohanrerDDY'
print d.lower()
c='chandhra'
print c.lower()



x="usa,canada,england"
y=x.split(',')
print y


# righr spece and left space mater
a='    mohan   '
print a
print a.lstrip()
print a.rsplit()
print a.strip()



a='python is fun'
print(a.partition('is'))
b='good morning mohan rara raju'
print(b.partition('ra'))



a='mohan rama moahan moraju'
print a.replace('mo','wwww')




a="ramammohanreddy"
print a.capitalize()

a="mohan"
print a.find('m')
print a.find('o')
print a.find('h')
print a.find('a')
print a.find('z')

a='This is a string'
print a.index('string')
print a.index('is')
print a.index('ri')

a="mohan"
print a.replace("mohan","Ramareddy")


a='This is our string'
print a.count('r')
print a.count('s')
print a.count('i')

str="abcdefghijklmnopqrstuvwxyz"
print len(str)
print max(str)
print min(str)

str="oooooooooooooooooomohanoooooooooooooo"
print str.strip('o')

#word count
#update
#slice


b=("a","b","c")
print "-".join(b)


a="lin1-abcdf /nline2-abc \nline-abcd";
print a.split()
print a.split(' ', 1)



a="mystringes"
print(type(a))

mystr1="mohan"
mystr2=mystr1.capitalize()
print(mystr2)

mystr1="mohaan"
print mystr1.capitalize()

mystr1="RAMAMOHANrEdDy"
print mystr1.lower()

mystr1="mohan"
print mystr1.center(30,'#')

mystr1="happy birthday"
print(mystr1)
print mystr1.ljust(20,'#')
print mystr1.rjust(20,'#')



mystr1="mohsn reddmy rajma jamy ramni"
print mystr1.count('m')


mystr1="hello world"                     #
print mystr1.encode()


mystr1="mohan reddy chikkepalli"         #True\\Flase
print mystr1.endswith("reddy")
print mystr1.endswith("chikkepalli")

mystr1="this is ramamohanreddy"           #True\\Flase
print mystr1.startswith("this")
print mystr1.startswith("is")


mystr1="this is \tmy \tstring,testing"
print mystr1.expandtabs(1)

mystr1="this is my name ramamohganreddy"
print mystr1.find("is")
print mystr1.find("name")

mystr1="this is my name  ramamohganreddy"    #
print mystr1.rfind("is")
print mystr1.rfind("z")


mystr1="this is my name  ramamohganreddy"
print mystr1.index("i")
print mystr1.index("y")
print mystr1.index("g")

mystr1="this is my name  ramamohganreddy"    #
print mystr1.rindex("i")
print mystr1.rindex("y")
print mystr1.rindex("g")

#marmat

mystr1="3.24"
print mystr1.zfill(100)

mystr1="python is very easy"
print mystr1.upper()

mystr1="ramamohanreddy"
print mystr1.title()

mystr1="rAMAMOHANREDDY"
print mystr1.swapcase()
mystr1="Ramamohanreddy"
print mystr1.swapcase()
mystr1="RAMAMOHAN REDDY"
print mystr1.swapcase()

mystr1="this\n name\r\n ramamohanreddy\v"
print mystr1.splitlines()


mystr1="this is* my* name* rajma"
print mystr1.split('*')

mystr1="this is* my* name* rajma"
print mystr1.rsplit('#',20)

mystr1="mohan"
print mystr1.replace("m","ramamohganreddy")


mystring="this is my string"
print mystring.partition(".")
print mystring.partition(",")

mystring="this is my string"
print mystring.rpartition(".")
print mystring.rpartition(",")



mystring="my name is mohan"
print mystring.strip("my")
mystring="www.youtube.com"
print mystring.lstrip("www.")
mystring="www.youtube.com"
print mystring.rstrip(".com")

a="a","b","c","d"
print " ".join(a)
print "-".join(a)
print "^".join(a)


a="bangaolre"
print a.count('b')

import string
a="cemvhny"
b="1234567"
x=string.maketrans(a,b)
s="the cow jumped over the moon"
print(a,b)
#print
print(s)
print s.translate(x)


a="mohan"
print a.upper()

a="mohan"
print a.title()

a="MOHANREDDY"
print a.swapcase()

a="ddddddddddmssssssssssmohanreddyooooooooooooo"
print a.strip('d')
print a.strip('s')
print a.strip('o')


a="ramamohanreddy"
print a.startswith("reddy",9,14)

n=11
f=1.2341
s="computre"
print("my number is {:d}".format(n))
print("my number is {:b}".format(n))
print("{:f}".format(f))
print("{:.3f}".format(f))
print("{:011.3f}".format(f))
print("{0} {1} {2}".format(n,f,s))



a='Happy birthday'
print a.center(35)
print a.center(70,'*')





string=raw_input("enter name:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)









#message = input("aBcDeFg: ")
#print("Capital Letters: ", sum(1 for c in message if c.isupper()))


#message = input("Type word: ")
#Type word: aBcDeFg
#print("Capital Letters: ", sum(1 for c in message if c.isupper()))


import string
value = "Bangalore in KADApa"
print len(filter(lambda x: x in string.uppercase, value))





