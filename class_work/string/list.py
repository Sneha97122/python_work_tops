a=[1,2,3,4,5,6,7]
b=['a','e','c','b','a']
c=[2,6,54,7,6]

# to insert recodes in list
a.append(4)
print(a)

#to insert recode on specific index
a.insert(1,10)
print(a)

#to marge(joint) to string
a.extend(b)
print(a)

#to remove the value into string
a.remove('b')
print(a)

b.sort()
print(b)

c.sort()
print(c)

a.reverse()
print(a)

b.clear()
print(b)


print(a.index(10))

print(a.count('a'))

