# name = "Lisa"
# age = "18"
# print(len(name))# кількість символів
# print(name[0])
# print(name[len(name-1])

# text=input()
# if len(text) >0:
#     print(text[0])
# else:
#     print("row is empty")

# text='Hello world'
# print(text[:5])
# print(text[6:])
# print(text[::2])
# print(text[::-1])
#
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.title())


# text = '    Python   '
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())

# user_login = "admin"
# login= input ("Enter your login : ").strip().lower()
# if user_login == login:
#     print("Welcome"+ user_login)


# text = "Python"
# for i in text:
#     print(i)

# password = input()
# digits=0
# u_letter=0
# if len(password)>=8:
#     for char in password:
#         if char.isdigit():
#             digits+=1
#         if char.isupper():
#             u_letter+=1
#     if digits>=2 and u_letter>=2:
#         print("Password is valid")
#     else:
#         print("Password is not valid")
# else:
#     print("Password is not valid")
#
# password.isdigit()
# password.isupper()
# password.islower()
# password.isalpha()
# password.isalnum()

# golosni = "аеєиїоуяію"
# count =0
# text= input("Enter a text:").lower()
# for char in text:
#     if char in golosni:
#         count += 1
# print(count)
#
# text = "Hello World!Python is the best!!"
# words = text.split()
# print(words)
# result = "-".join(words)
# print(result)
# new_text = text.replace("Python", "JavaScript")
# print(new_text)

# text = input().lower().strip()
# if text==text[::-1]:
#     print("polyndrom")
# else:
#     print("not polyndrom")

# text = input().strip().lower()
# words = text.split()
# max_word = words[0]
# for word in words:
#     if len(word)> len(max_word):
#         max_word = word
# print(max_word)

