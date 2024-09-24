dict1 = {1: "banana",
      2: "salt",
      3: {1.1: "eg", 1.2: "cat", 1.3: "butter", 1.4: "cucumber", 1.5: "bread"},
      4: "sausage"}
print(dict1)

dict2 = {1: type(dict1[1]),
         2: type(dict1[2]),
         3: type(dict1[3]),
         4: type(dict1[4])}
print(dict2)