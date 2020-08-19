
person_1 = {
    'first_name' : 'Kushal',
    'last_name' : 'Gajurel',
    'sex' : 'Male',
    'age' : 23
    }
person_2 = {
    'first_name' : 'Kriti',
    'last_name' : 'Gajurel',
    'sex' : 'Female',
    'age' : 20
    }
person_3 = {
    'first_name' : 'Hari',
    'last_name' : 'Sigdel',
    'sex' : 'Male',
    'age' : 35
    }

people = [person_1, person_2, person_3]



for info in people :
    print(info['first_name'] + " " + info['last_name'] + " is a " + str(info['age']) +" year old " + info['sex'])
    print("\n")
