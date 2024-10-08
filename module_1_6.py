my_dict = {"serum": 897.60, "essence": 1500.00, "emulsion": 2500.50}
print(my_dict)
print(my_dict["essence"])
print(my_dict.get("cream"))
my_dict.update({"eye cream": 1100.00, "sleeping mask": 796.50})
print(my_dict)
a = my_dict.pop("emulsion")
print(a)
print(my_dict)

my_set = {1990, 1991, "year", True, True, 1991, 1990, "day", (1,5,7)}
print(my_set.add(1992))
print(my_set.add(1995))
print(my_set)
print(my_set.remove((1, 5, 7)))
print(my_set)