a = 'Максим'
b = 'Лебезун'
c = 16
A = type(a)
B = type(b)
C = type(c)
list1 = [a, b, c]
list2 = [A, B, C]
list_string = []
list_int = []

if A == str:
    list_string.append(A)
elif A == int:
    list_int.append(A)

if B == str:
    list_string.append(B)
elif B == int:
    list_int.append(B)  

if C == str:
    list_string.append(C)
elif C == int:
    list_int.append(C)

if len(list_string) > len(list_int):
    print('Тип даних str переважає')
elif len(list_int) > len(list_string):
    print('Тип даних int переважає')
