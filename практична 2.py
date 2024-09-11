text = "Hello world"
name = "Максим Лебезун"
age = 16
list1=[text, name, age]
print(list1)
list2=[type(text), type(name), type(age)]
print(list2)
if type(text) == type(name) == type(age):
    print("Тип str, повторюється найчастіше")
elif type(text) == type(name) and type(name) == type(age) and type(text) == type(age):
    print("Тип str, повторюється найчастіше")
else:
    print("Дані незбігаються")
