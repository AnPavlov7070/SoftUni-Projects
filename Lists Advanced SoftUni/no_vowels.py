text = input()

vowels = 'auoeiAUOEI'

text_without_vowels = [char for char in text if char.lower() not in vowels]

print(''.join(text_without_vowels))


