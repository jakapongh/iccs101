# Creating a set with integers 1, 8, 9
mySet: set[int] = {1, 8, 9}


# Sets do not store repeats
repeatingSet: set[int] = {5, 9, 9, 8, 8, 7, 5}
print(repeatingSet)


# Strings, there will be no repeats
names: set[str] = {"a", "b", "a", "b", "test", "name"}
print(names)


# Transforming an array to a set
name_list: list[str] = ["jack", "john", "bill", "jamie", "james", "jane", "jack"]

# Same here, no repeats will be stored
name_list_set = set(name_list)
print(name_list_set)


# A string is basically an array of characters, therefore:
word = "hello"
word_set = set(word)
# Positions seems to be random, as there is "no sequence"
print(word_set)

