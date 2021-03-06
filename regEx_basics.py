import re

# Finding a phone number using function


def isPhoneNumber(text):
    if len(text) != 12:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # no area code
    if text[3] != '-':
        return False  # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # not first 3 digit
    if text[7] != '-':
        return False  # missing dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # not last 4 digit
    return True


res = isPhoneNumber('415-555-1234')
print(res)


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# Finding a phone number using REGEX

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search(message)  # search gives us the first match
mo2 = phoneNumberRegex.findall(message)  # findall gives us all the matches
res1 = mo.group()

print(mo2)
