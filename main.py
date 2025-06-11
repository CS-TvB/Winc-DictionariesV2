# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    big_brother_data_base = {}
    big_brother_data_base['name'] = name
    big_brother_data_base['date_of_birth'] = date_of_birth
    big_brother_data_base['place_of_birth'] = place_of_birth
    big_brother_data_base['height'] = height
    big_brother_data_base['nationality'] = nationality
    print(big_brother_data_base)
    return(big_brother_data_base)

def add_stamp(big_brother_data_base, lst_countries):
    big_brother_data_base = {}
    big_brother_data_base['stamps'] = lst_countries
    return(big_brother_data_base)

def add_biometric_data(big_brother_data_base, problem, value, date):
    biometric = {}
    biometric['data'] = problem
    biometric['data info'] = value
    biometric['date of info'] = date
    for x in range(1):
        big_brother_data_base['biometric'] = biometric
        big_brother_data_base['finger_prints', date] = value
        print (big_brother_data_base)
    return(big_brother_data_base)

big_brother_data_base = {}
lst_countries = ['Greece', 'Scotland', 'Spain', 'France']
name = 'Jhon Jones'
date_of_birth = '06-08-1986'
place_of_birth = 'Amsterdam'
height = float(1.84)
nationality = 'Netherlands'

problem = 'broken neck'
value = 'neck bracelet'
date = '22-09-2022'

create_passport(name, date_of_birth, place_of_birth, height, nationality)
add_stamp(big_brother_data_base, lst_countries)
add_biometric_data(big_brother_data_base, problem, value, date)

'''
If the passport did not yet have any biometric data: add the key for it, you can assume you'll only get passports with a chip to save biometric data.
If the type of biometric data was not yet in the passport: add it to the passport.
The value for the specific type of biometric data should again be a dictionary (so nested again). This dictionary should have two keys: date and value. See examples below for specific examples.
If the type of biometric data was already in the passport: update the biometric data in the passport, overwriting the previous value and date.
'''
