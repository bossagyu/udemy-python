import math


word = 'python'
print(word[0])
print(word[-1])
print(word[0:2])
print(word[:2])
print(word[2:5])
print(word[2:])
print(len(word))

print(r'C\name\name')
print("""
aaaa
bbb
""")

print('hi' * 3)


result = math.sqrt(25)
print(result)

num: int = 1
name = 'Mike'

print(num)
print(name, type(num))
print('hi', 'mike', sep='bbb', end='')

s = "My name is Mike"
print(s)
print(s.startswith('My'))
print(s.find("Mike"))
print(s.capitalize())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

print("My name is {name} {family}".format(name="koichi", family="yoshida"))

name = "koichi"
family = "yoshida"
print("My name is {0} {1}".format(name, family))

# f-string 今はこっちが主流で処理が早い
print(f'My name is {name} {family}')

