# REGULAR EXPRESSION
# ------------------

# it hava a module name re
import re

# a='welcome to all'

'''re.sub'''
# re.sub is used to replace a content from the given variable

'''print(re.sub('w','W',a))'''

'''re.split'''
# re.split is used to split words and change to a list

'''print(re.split(' ',a))'''

'''re.findall'''
# re.findall is used to find a word or letter in the whole variable and it is stored in a list.it shows the whole str which is searched. 

'''print(re.findall('e',a))'''

'''re.search'''
# re.search it is used to search a variable.it only shows the first string which is to be searched

'''print(re.search('e',a))'''

a='abcd'


'''. (dot) is used to search a single value next to the searched value''' 

'''print(re.search('a.',a))'''
# OUTPUT : <re.Match object; span=(0, 2), match='ab'>

'''print(re.search('d.',a))'''
# OUTPUT : None

'''print(re.search('c.',a))'''


''' * (star) is used to search full item occurence'''

'''print(re.search('a.*',a))'''
# OUTPUT :<re.Match object; span=(0, 4), match='abcd'>

'''print(re.search('b.*',a))'''
# OUTPUT :<re.Match object; span=(1, 4), match='bcd'>

'''print(re.search('d.*',a))'''
# OUTPUT :<re.Match object; span=(3, 4), match='d'>


'''+ (plus) is used to find one or more occurence'''

'''print(re.search('d.+',a))'''
# OUTPUT : None

'''print(re.search('a.+',a))'''
# OUTPUT :<re.Match object; span=(0, 4), match='abcd'>

'''print(re.search('b.*',a))'''
# OUTPUT :<re.Match object; span=(1, 4), match='bcd'>


''' ? (question mark) is to find zero or one occurence '''

'''print(re.search('b.?',a))'''
# OUTPUT :<re.Match object; span=(1, 3), match='bc'>

'''print(re.search('a.?',a))'''
# OUTPUT :<re.Match object; span=(0, 2), match='ab'>

'''print(re.search('d.?',a))'''
# OUTPUT :<re.Match object; span=(3, 4), match='d'>

#'''[] 

'''print(re.search('[a-z]',a))'''

'''print(re.search('[A-Z]',a))'''

'''print(re.search('[a-z][0-9]',a))'''

'''print(re.search('[a-z 0-9]',a))'''

'''print(re.search('[a-z].',a))
print(re.search('[a-z].+',a))
print(re.search('[a-z].*',a))
print(re.search('[a-z].?',a))'''

# print(re.search('[a-z].*[0-9]',a))

a='abcd789'
# print(re.search('[a-z].*[0-9]',a))

# print(re.search('[a-z].{3}',a))
