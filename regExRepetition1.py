import re
# Optional Matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())


# Matching Zero or More with the Star : The * (called the star or asterisk) means “match zero or more”
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoan')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())


# Matching One or More with the Plus: the + (or plus) means “match one or more.”
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

# Matching Specific Repetitions with Braces: to repeat a specific number of times
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
