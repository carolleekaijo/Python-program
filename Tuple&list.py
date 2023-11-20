
a = (1,2,'a', 'g', 98)
b = list(a)
del (b[2])
b = tuple(b)
print(b)

c = [1,2,3]
d = 'apple'
e = (c,d)
print(e)

f = []
g = 9
h = 8
i = 12 
f.append(g)
print(f)

j = []
k = int(input('what is your name'))
a.append(j)
print(j)

ID_database = [] 
create_ID_input = input('Create ID:') 
create_ID_input_type=str(create_ID_input) 
ID_database.append(create_ID_input_type) 
Input_ID = input('Input ID:') 
Input_ID_type=str(Input_ID) 
if Input_ID_type in ID_database:    
    print("Available") 
else:    
    print("Not Available")