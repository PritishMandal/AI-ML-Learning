info = [
    ("Alice","MAth"),
    ("Bob","DBMS"),
    ("Charlie","TFCS"), 
    ("Alice","OS"),
    ("Bob","Math"),
    ("Alice","DBMS"),
    ("Charlie","OS"),
]

dict = {}

for name, course in info:
    if dict.get(name) == None:
        dict.update({name: set()})
    
    dict[name].add(course)

print(dict)
        # ye code ek dictionary banayega jisme har student ke naam ke saath uske courses ka set hoga, jisse duplicate courses ko avoid kiya ja sakega.