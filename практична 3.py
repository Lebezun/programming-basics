kratos = {
    "name": "Kratos",
    "age": 3000,
    "Other": {
        "city": "Sparta",
        "street": "there is no",
        "weapon 1":"Leviathan Axe",
        "weapon 2": "Blades of Chaos"},
	 "weight_kg": 136 }
type_items = {}
for k, v in kratos.items():
    if type(v) == dict:
        for k1, v1 in v.items():
            type_items[k1] = type(v1)
    else:
        type_items[k] = type(v)
print(type_items)
