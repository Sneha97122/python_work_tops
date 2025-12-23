list=['apple','banana','mango','papaya']

serch_item ='mango'

find = False

for item in list:
    if item == serch_item:
        find = True
        break

if find:
    print(f"{serch_item} find in the list")
else:
    print(f"{serch_item} is not found in the list")



