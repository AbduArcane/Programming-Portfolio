Pets = []

pet_information = {
    'Animal_Type': 'Cat',
    'Owners_Name': 'Mark'
}

Pets.append(pet_information)

pet_information = {
    'Animal_Type': 'Dog',
    'Owners_Name': 'Sara'
}

Pets.append(pet_information)

pet_information = {
    'Animal_Type': 'Hamster',
    'Owners_Name': 'Harrison'
}

Pets.append(pet_information)

for pet_information in Pets:
    print("\nThings I know about " +
          pet_information['Owners_Name'].title() + ":")
    for key, value in pet_information.items():
        print("\t" + key + ": " + str(value))
