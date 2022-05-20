import re

a = 'hello, world!'
# print(re.match('world!',a))

# print(re.search('^world!',a))

# print(re.search('world!$',a))


# str1 = '123 hello 678 HELLO'
# print(re.match('[0-9]+',str1))
# print(re.match('[0-9]*',str1))
# print(re.search('[0-9]*',str1))

# print(re.match('a*b','aaaaab'))
# print(re.match('a+b','b'))

# print(re.search('^[0-9]{2,3}-[0-9]{4}-[0-9]{4}$','002-1111-1111 tel'))

# p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
# print(p.search('ss7up@gmail.com'))
# print(p.search('shimseonjo@naver.com'))

p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
email = ''
while not p.search(email):
    email = input('email >>> ')
