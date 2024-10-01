a = "Hello World"
name = "Max"
surname = "Lebezun"
age = 16
lst = [a, name, surname, age ]
type_lst = []
value_lst = []
string = 0
integer = 0
floatt = 0
other = 0
for i in lst:
    x = type(i)
    y = i
    type_lst.append(x)
    value_lst.append(y)
    if type(y) == str:
        string += 1
    elif type(y) == int:
        integer += 1
    elif type(y) == float:
        floatt += 1
    else:
        other += 1
if string > integer and string > floatt and string > other:
    print("the most frequency type is 'str'")
elif integer > string and integer > floatt and integer > other:
    print("the most frequency type is 'int'")
elif floatt > string and floatt > integer and floatt > other:
    print("the most frequency type is 'float'")
