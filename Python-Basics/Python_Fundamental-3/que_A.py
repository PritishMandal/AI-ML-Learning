info = [
    ("Alice","MAth"),
    ("Bob","DBMS"),
    ("Charlie","TFCS"), 
    ("Alice","OS"),
    ("Bob","Math"),
    ("Alice","DBMS" ),
    ("Charlie","OS"),

]
courses_set= set()
for tup in info:
    courses_set.add(tup[1])#course

    print(courses_set)

