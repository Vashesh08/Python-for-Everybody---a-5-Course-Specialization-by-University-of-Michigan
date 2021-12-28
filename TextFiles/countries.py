input_filename = "country_info.txt"

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        countries[country.casefold()] = country_dict
        # print(country_dict)
        countries[code.casefold()] = country_dict
        # print(country_dict)

print(countries)
while True:
    country_name = input("Country Name: ").casefold()
    if country_name in countries:
        if countries[country_name]['capital'] != "":
            print("Capital of {} is {}".format(country_name.capitalize(), countries[country_name]['capital']))
        else:
            print("{} does not have a capital".format(country_name.capitalize()))
    elif country_name == "quit":
        break
    else:
        print("{} not there".format(country_name.capitalize()))
