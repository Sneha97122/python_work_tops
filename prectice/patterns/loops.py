name="sneha"
for i in range(5):
    print(name)

print("----------------------")

name="sneha"
i=1
while i<=5:
    print(name)
    i+=1

print("-----------------------")
print("reverse the string")

str="sneha"
str1=[1,2,3,4]
print(str[::-1])
print(str1[::-1])

print("_--------------")
print("palinram number")
s="madamm"
print("palindram" if s==s[::-1] else "not palindram")

print("-----------------------")
print("count vowals")

str="hello my name is sneha"
count=0
for ch in str:
    if ch in "aeiou":
        count+=1
print(count)


