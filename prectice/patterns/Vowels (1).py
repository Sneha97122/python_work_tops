  #wrt program to count the vowels and consonent
# sentence=input("Enter the sentence:")
# vowels=['a','i','o','u','e']

# present_vowels=[]
# present_consonent=[]

# vowel_count=0 
# consonent_count=0

# for ch in sentence:
#     if ch in vowels:
#         vowel_count+=1 
#         if ch not in present_vowels:
#             present_vowels.append(ch)

#     else:
#         consonent_count+=1 
#         if ch not in present_consonent: 
#             present_consonent.append(ch)

# print("present vowels:",present_vowels)
# print("Total number of vowels:",vowel_count)
# print("present consonent:",present_consonent)
# print("Total number of consonent:",consonent_count)

print("----------------------------------------------------")

#To find the factorial of number 
# n=int(input("Enter the number:"))
# i=1 
# fact=1 
# while i<=n:
#     fact=fact*i
#     i+=1 
# print(f"Factorial of {n} is:",fact)

print('----------------------------------------------')

#To check the palindrom number 
# num=input("Enter the user input:")
# rev=num[::-1]
# if num==rev:
#     print("Palindrom")
# else:
#     print("Not Palindrom")

print("-----------------------------------------")

#swapping of two number without using theired varibale 
# a=int(input("Enter the number a:"))
# b=int(input("Enter the number b:"))

# a=a+b 
# b=a-b 
# a=a-b 
# print("After swapping of a:",a)
# print("After swapping of b:",b)

print("----------------------------------------------")

#Armostrong number 
# num=int(input("Enter the number:"))
# sum=0 
# temp=num 
# while temp>0:
#     digit=temp%10 
#     cube=digit**3 
#     sum=sum+cube 
#     temp//=10 
# if sum==num:
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")
    
print("------------------------------------------------")

# prime number
# n=int(input("Enter the number:"))
# if n<=2:
#     print("Not prime")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("Not prime")
#             break 
#     else:
#         print("Prime")

print("---------------------------------------------------")

#Fibonaccie series 
num=int(input("Enter the number:"))
a,b=0,1 
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b 
    
