message = "bobby's world"
# printing letters from 0 - 2
print(message[0:3])
# printing lower case letters and upper
print(message.lower())
# printing a message which counts the symbols I have written
print(message.count('bobby'))
# replacing words
message = 'hello world'
new_message = message.replace('world', 'universe')
print(new_message)
#printing combined messages
greetings = 'hello'
name = 'Andrey'
message = greetings + ', ' + name
print(message)

greetings = 'hello'
name = 'Andrey'
message = greetings + ', ' + name + '. Welcome!'
print(message)

#printing combined messages using strings
greetings = 'hello'
name = 'Andrey'
message = '{}, {}. Welcome!'.format(greetings, name)
print(message)
# "f" strings method
greetings = 'hello'
name = 'Andrey'
message = f'{greetings}, {name}. Welcome!'
print(message)
#check information on how to proceed with a string
print(dir(name))
print(help(str))
print(help(str.lower))