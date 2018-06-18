# hello python

print('hello world!')
firstName = 'aquila'
lastName = 'strother'
# print(firstName.capitalize())
# print(lastName.capitalize())
print('Hiya' + ' ' + firstName.capitalize() + ' ' + lastName.capitalize())

# One statement per line
age = int(input("Please enter your age: "))
print('Hey, you are', age)
if age < 18:
    age = 18
    print('You are not old enough to skydive buddy')
else:
        print('You can now plunge from the sky!')
        