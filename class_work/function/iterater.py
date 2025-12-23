# ITERATERS

# l=[10,20,30,40,50]

# # for i in l:
# #     print(i)

# k=iter(l)
# print(next(k))
# print(next(k))


#GENRATERS

def squer(a):
    for i in range(1,a+1):
        yield i*i

a=iter(squer(5))
print(next(a))
print(next(a))