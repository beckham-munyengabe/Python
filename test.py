name = input("Enter your name: ")
email =input("Enter your email: ")
password = input("Enter your password: ")
skill =input("Enter your skill: ")
education = input("Enter your education: ")
ph = input("Enter your phone number: ")

user_input = {
    "name": name,
    "email": email,
    "password": password,
    "skill": skill,
    "education": education,
    "phone_number": ph
}

for i, j in user_input.items():
    print(i, j)


