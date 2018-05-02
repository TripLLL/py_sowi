# -*- coding: utf-8 -*-


##############################################################################
# 1 - Variables and data types
##############################################################################


# First script
##############################################################################

# New file: variables_and_data_types.py

print 'Hello world!'


print 'Hallöchen Welt!' 

''' 
Wenn die folgende Zeile nicht ganz oben im Skript steht, bekommt ihr eine 
Fehlermeldung:
#  steht  -*- coding: utf-8 -*-
'''


# Basic build-in data types
##############################################################################

a = "This is a string"

print a

print type(a) # str

# print b

b = 1

print b

print type(b) # int

c = 1.2

print c

print type(c) # float

d = [a,b,c]

print d

print type(d) # list

e = (a,b,c)

print e

print type(e) # tuple

f = {'a': a, 'b': b, 'c': c, 'd':d, 'e':e} 

print f

print type(f) # dict

g = set([a,b,c,e])

print g

print type(g) # dict


n = None

t = True

f = False

print [a, n, t, f] # None, True, False


# Basic operators
##############################################################################

print 1 + 2

print 2 * 4

print 'hello' + 'world'

print 'hello' + ' ' + 'world'

# print 1 + '2' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print 1 + int('2')

print str(1) + '2'

print 'hello' * 2


# bis hierher outcomes immer int, str oder float, aber jetzt...

print 1 == 2

print [1,2] == [1,2]

print 'a' == 'a'

print ('a' == 'b') == False

print 'b' > 'a'

# Unterschied == und is

print 1 is 1

print 'a' is 'a' # 'identical' strings are identical to each other

print [1,2] is [1,2] # 'identical' lists are NOT identical to each other!




# integer and float
##############################################################################

a = 10

print a

print a / 3

print a / 3.0 

print type(1)

print type(1.0)

a = 1000000000000000000000000000

print a + 1 == a

a = 1000000000000000000000000000.0

print a + 1 == a

# einige Floats sind nur Annäherungen (Speicher ist immer endlich!)




# strings
##############################################################################

# print 'What if I want to write 'Hello world' in single quotes?'

print '...\'Hello world\'...'

print "...'Hello world'..."

print """...'Hello world'..."""

print '''...'Hello world'...'''

print """ 

I can also use triple quotes to spread text
	 accross 
	 	several
	 		lines 

	 		Ain't that great?! 

	 	:-)
""" 

print 'first line\n\tsecond line\n\t\tthird line'


# string functions. Schaut selber nach!

print 'A'.lower()

print ' A   '.strip()

# functions on strings

print len('abc')

print list('abc')

print int('123')



# lists
##############################################################################

# first experiment:

a = [1,2]

print a

b = a

print b

a = a + ['three'] 

print a

print b # b different from a

# second experiment:

a = [1,2]

print a

b = a

print b

print a.append('three')

print a

print b # b same as a!!!


# list functions

a = [6,2,9,7,4,2]

a.sort()

print a

a.sort(reverse=True)

print a

# functions on lists

print a.append(45)

print sorted(a)

print a # still reverse!

print len(a)



# tuples
##############################################################################

a = (1, 2)

# a.append('three') # AttributeError: 'tuple' object has no attribute 'append'


# indexing for strings, tuples, and lists
##############################################################################


a = [1, 'zwei', 3.5, None]

print a[1] # huch?!

print a[0] # Aha!

print a[0:2]

print a[:2] # Die Null kann man weglassen

# wie komme ich zum letzten Element?

print a[-1] # letztes Element

print a[0:-1] # ACHTUNG: nur BIS vor das letze Element!!!

# welche Zahl brauchen wir?

print a[0:4]

print a[0:99]

print a[0:len(a)] # Trick 17!

print a[0:] # einfach weglassen geht auch

print a[:] # forward

print a[::2] # forward two-step

print a[1::2] # forward two-step, begin second

print a[::-1] # backward


# dasselbe gilt für Strings!

a = 'Hello world!'

print a[4]

print a[:2]

print a[2:]

print a[2:4]

print a[-4:-1]

print a[1::2]

print a[4::-1]


# check for membership

print 'a' in 'abc'

print 'a' in [1,2,'a']


# dictionaries
##############################################################################

a = {'index the key':'get the value'}

print a

print a['index the key']

# print a[0]

a = {'key1':99}

print a['key1']

# print a['key2'] # KeyError: 'key2'

a['key2'] = 7

print a['key2']

print a

a = {1:1, 'two':2}

print a[1] # DIFFERENT from indexing in lists!!! Here 1 is a key

print a['two']

print a

a = {'one-two':[1,2]}

# a = {[1,2]:'one-two'} # TypeError: unhashable type: 'list'

a['two'] = a

print a

print a['two']

a['three'] = 3

print a

print a['two']

print a['two']['two']

print a['two']['two']['two']['two']['two']['two']['two']['two'] # Say whuuuuuuuuut?


# Sets
##############################################################################

a = set([1,2,'test'])

print a

# print a[0] # TypeError: 'set' object does not support indexing

# Set functions

a.add(89)

print a

a.add('test')

print a # 'test' war schon drin, und kann nur einmal vorkommen

print 2 in a

print 6 in a

a = set([1,2,3])

b = set([2,7])

print a.union(b) # union 

print a.difference(b) # differnce 

print b.difference(a) # differnce 


# geht auch einfacher zu schreiben:
print a & b # union 

print a - b # difference

print b - a # difference



# Transformations between build-in data types
##############################################################################

a = [1,2,3]

b = '4'

c = {'a':1, 'b':2, 'c':3}

print list(a)

print list(b)

print list(c)


print str(a)

print str(b)

print str(c)


print int(b)


print dict([['a',1],['b',2]])


print bool(a), bool(b), bool(c)

print bool([]), bool(''), bool({})

print bool(None)






# Formating Python files and Comments
##############################################################################


print 'To break command lines (not the printed text itself!)' \
', I use "\\" at the end of a line.'

# print "I make sure that '\\'' is the line's last character" \ 
# ", else it won't work." # SyntaxError: unexpected character after line continuation character


print "By the way..." # this is a comment. It won't get printed.

'''
This is also a comment. Like in the print example above, you can use triple
quotes to break lines, which can be important for loooooooooooooooooooooooooo-
oooooooooong comments...

Oh, and it is forbidden by law to use more than 80 characters on a single line!
...well, let's say up to 100 chars??? https://www.python.org/dev/peps/pep-0008/#maximum-line-length
'''


