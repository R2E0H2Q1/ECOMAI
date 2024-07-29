text: str = "Hello, World!!"
print(len(text))

text1: str = "   Hello, World!!   "
print(text.strip())

text2: str = "Hello, World!!"
print(text2.lower())

text3: str = "Hello, World!!"
print(text3.upper())

text4: str = "Hello, World!!"
print(text4.replace("World", "Python"))
print(text4.replace("l", "t"))
print(text4.replace("t", ""))

text5: str = "Hello, World!! good morning"
print(text5.split())
text5 = "Hello,*World!!*good*morning"
print(text5.split('*'))

# input 2 numbers in 1 line for short -- bonus
# a, b, c, d = [7, 9, 'hi', [1, 123]]  # a = 7; b = 9; c = 'hi'; d = [1, 123]
# x, y = input('enter 2 numbers (with space)').split()
# # nice shortcut
# x, y = [int(num) for num in input('enter 2 numbers (with space)').split()]
# print(x, y)
# print(x + y)
# x, y = [int(num) for num in input('enter 2 numbers (with comma)').split(",")]
# print(x, y)
# print(x + y)

# Join
print(['H', 'E', 'L', 'L', 'O'])
print("".join(['H', 'E', 'L', 'L', 'O']))

text6: str = "Hello, World!! good morning"
print('text6.startswith("Hello") ?', text6.startswith("Hello"))

text7: str = "Hello, World!! good morning"
print('text7.endswith("good morning") ?', text7.endswith("good morning"))

text8: str = "hello, world!! good morning"
print('text8.capitalize() ', text8.capitalize())

text9: str = "hello, world!! good morning"
print('text9.title() ', text9.title())

print('"1234" text10.isalpha() ', "1234".isalpha())
print('"abcd".isalpha()', "abcd".isalpha())
print('"abcd_".isalpha()', "abcd_".isalpha())
print('"abcd*".isalpha()', "abcd1*".isalpha())

print('"1234" text10.isdigit()', "1234".isdigit())
print('"abcd".isdigit()" ', "abcd".isdigit())
print('"abcd1".isdigit()" ', "abcd1".isdigit())

print('"Aab".islower()', "Aab".islower())
print('"aab".islower()', "aab".islower())
print('"Aab".isupper()', "Aab".isupper())
print('"ABC".isupper()', "ABC".isupper())

print('"AasdasBcccC".swapcase()', "AasdasBcccC".swapcase())

print('"42".zfill(5)', "42".zfill(5))

print('Hello!'.center(12, '-'))
print('Hello!'.center(12, ' '))

print('"     ".isspace()', "    ".isspace())

print("Hello python course")
print('   [0]', "Hello python course"[0])
print("  [-1]", "Hello python course"[-1])
print("[::-1]", "Hello python course"[::-1])
print("  [5:]", "Hello python course"[5:])
print("  [:8]", "Hello python course"[:8])
print(" [::2]", "Hello python course"[::2])




