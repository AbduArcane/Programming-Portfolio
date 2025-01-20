def describe_city(city, country='Japan'):
    message = f"{city.title()} is in {country.title()}."
    print(message)


describe_city('Tokyo')
describe_city('Reykjavik', 'Iceland')
describe_city('Islamabad', 'Pakistan')
