# string is a sequential data type.

# sentenses = "the brown box jumps over the lazy dogs"
# print(sentenses + ":", type(sentenses))

# print(sentenses.capitalize())
# print(sentenses.lower())
# print(sentenses.upper())

# String Concatenation.

"""name = "behan "
last_name = "kumar"
print(name.capitalize() + last_name)"""

# String formating in another way.

# name = 'behan'
# last_name = "kumar"

# print(f"my name is {name.capitalize()} {last_name}")

# *************************************************************

# name = 'behan'
# last_name = 'kumar'

# print(('my name is {0} {1}').format(name.capitalize(), last_name))

# String Slicing

# sentenses = "the brown box jumps over the lazy dogs"

# print(sentenses[0:9])
# print(sentenses.index('box'))
# print(sentenses[0: 29])

# lis = sentenses.split() # convert into list.
# print(lis)

# rendon_word = "           i am not lazy                "

# print(rendon_word.strip()) # remove any white space from beginning and the end.

# print(rendon_word.strip().replace("i", "we").upper().split())

# String Format

# user_name = input("enter name: ")
# res = "my name is " + user_name.capitalize()
# print(res)

name = "behan"
age = 24
detail = "my name is {} and my age is {}"

# print(detail.format(name, age))

quentity = 3
price = 30
detail = "i want to pay {1} doller for washing power with quentity {0}"
# print(detail.format(quentity, price))


# Escape Characters

text = "the brown box \"jumps\" over the lazy dog" # Escape character allow you to use bouble quotes while they all ready used.
# print(text)

text2 = "the man was \n down into the mug hahaha" # \n means to change the line after was.. 
# print(text2)

text3 = "the man was \t down into the mug hahaha" # \t means to take a white space after was..
# print(text3)

text4 = "           the man was \bdown into the mug hahaha" # remove backspace.
# print(text4)

fruit = ['apple', 'pineApple', "orange"]
new_s = " "
# print(new_s.join(fruit))
print(text4.lstrip())