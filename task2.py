


names = [
['Alice', 'bob', 'Charlie'],
['davin', 'Eve', 'Frank'],
['Grace', 'Heidi', 'Ivan'],
['Grace', 'Ken', 'laura']
]

Alice_found = False


for list in names:
    if "Alice" in list:
        list.remove("Alice")
        Alice_found = True     
        

if Alice_found:
    new_name = input("alice not found. Place enter new Name")
    names[0].append(new_name)

print(names)



for list in names:
    for name in list:
        print(name)






