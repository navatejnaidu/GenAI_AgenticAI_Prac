# Variables in Python
First_name = 'Polineni Navatej'
Last_name = 'Naidu'
Country = 'India'
Union_territory = 'Andaman and Nicobar Islands'
Age = 15
Is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python','Node JS', 'MongoDB', 'MySQL', 'Git', 'GitHub', 'Docker', 'Kubernetes', 'AWS', 'Azure','Linux', 'C', 'C++', 'Java', 'Devops', 'Matpoltlib', 'Numpy', 'Pandas', 'Flask', 'Django']
Person_info = {
    'Firstname':'Neymar', 
    'Lastname':'da Silva Santos Júnior', 
    'Country':'Brazil',
    'City':'Rio de Janeiro',
    }

# Printing the values stored in the variables

print('First name:', First_name)
print('First name length:', len(First_name))
print('Last name: ', Last_name)
print('Last name length: ', len(Last_name))
print('Country: ', Country)
print('Union territory: ', Union_territory)
print('Age: ', Age)
print('Married: ', Is_married)
print('Skills: ', skills)
print('Person information: ', Person_info)

# Declaring multiple variables in one line

First_name, Last_name, Country, Age, Is_married = 'Sergio', 'Ramos', 'Spain', 34, False

print(First_name, Last_name, Country, Age, Is_married)
print('First name:', First_name)
print('Last name: ', Last_name)
print('Country: ', Country)
print('Age: ', Age)
print('Married: ', Is_married)