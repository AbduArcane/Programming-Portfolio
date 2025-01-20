Rivers = {
    'nile': 'Egypt',
    'Amazon': 'Brazil',
    'Indus': 'Pakistan',
    'mississippi': 'United States'
}

for River, country in Rivers.items():
    print("The " + River.title() + " runs through " + country.title() + ".")

print("Names of each rivers included in the dictionary: ")
for River in Rivers.keys():
    print("* " + River.title())

print("Names of each country included in the dictionary: ")
for country in Rivers.keys():
    print("* " + country.title())
