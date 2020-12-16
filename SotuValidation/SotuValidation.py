# Validoi Suomalaisen henkilötunnuksen.
# Mahdollisia ainoastaan oikeamuotoiset
# Esim DDMMYY-123Y
# https://fi.wikipedia.org/wiki/Henkil%C3%B6tunnus
from datetime import date
import re
import datetime

finalCharacterValidationDictionary = {
    0 : 0,
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : 'A',
    11 : 'B',
    12 : 'C',
    13 : 'D',
    14 : 'E',
    15 : 'F',
    16 : 'H',
    17 : 'J',
    18 : 'K',
    19 : 'L',
    20 : 'M',
    21 : 'N',
    22 : 'P',
    23 : 'R',
    24 : 'S',
    25 : 'T',
    26 : 'U',
    27 : 'V',
    28 : 'W',
    29 : 'X',
    30 : 'Y'
}

def sotuCheck(sotu):
    sotuPattern = re.compile(r'(\d{6})(\+|-|a|A)(\d{3}\w)')
    matches = sotuPattern.finditer(sotu)
    
    for m in matches:
        # group(1) = DDMMYY
        # group(2) = +, -, or A
        # group(3) = NNNC
        if validateDate(m.group(1)): # pvm check
            century = getCentury(m.group(2)) # century person born
            gender = getGender(m.group(3)) # gender of the person
            if validationCharacter(m.group(1), m.group(3)): # last character validation
                date = formattedDate(m.group(1), century)        
                print('This number is valid. The person is {} and was in born in {}'.format(gender, date))
                return True    
    
    return False

def validateDate(date):
    dd = date[0:2]
    mm = date[2:4]
    yy = date[4:6]
    try:
        datetime.datetime(int(yy), int(mm), int(dd))
    except ValueError:
        print("Date is invalid")
        return False        
    return True

def getCentury(century):
    if century == '+':
        return '18'
    elif century == '-':
        return '19'
    elif century == 'A' or century == 'a':
       return '20'
    else:
        print("Invalid century")

def getGender(group):
    number = group[0:3]
    if int(number) % 2 == 0: # Jakojäännös. Naiset parillisia, miehet parittomia.
        return 'female'
    else:
        return 'male'

def formattedDate(group1, century):
    return group1[0 : 2] + '.' + group1[2 : 4] + '.' + century + group1[4 : 6]  

def validationCharacter(date, lastCharacters):
    fullNumber = date + lastCharacters[0:len(lastCharacters)-1]
    division = float(fullNumber) % 31
    finalChar = lastCharacters[len(lastCharacters)-1]
    if(finalCharacterValidationDictionary[division] == finalChar):
        return True
    else:
        return False
