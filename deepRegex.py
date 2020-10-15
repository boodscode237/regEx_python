import re
# The Caret and Dollar Sign Characters
beginsWithHello = re.compile(r'^Hello')
endsWithWorld = re.compile(r'world!$')
print(beginsWithHello.search('Hello, world!'))
print(endsWithWorld.search('Hello, world!'))
print(beginsWithHello.search('He said hello.') == None)

alldigitsRegex = Regex = re.compile(r'^\d+$')
print(alldigitsRegex.search("252456435465645165wd1546545146545"))

# The Wildcard Character

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat in the flat mat'))

atRegex1 = re.compile(r'.{1,2}at')
print(atRegex1.findall('The cat in the hat sat in the flat mat'))


# find a first name and a name

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
name = nameRegex.findall('First Name: Donald Last Name: Brice')
print(name)

# To match any and all text in a non-greedy fashion, use the dot, star, and question mark (.*?).
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve woman> for dinner.>')
print(mo.group())


'''
The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.
'''

# Substituting Strings with the sub() Method
namesRegex = re.compile(r'Agent \w+')
censored = namesRegex.sub(
    'CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(censored)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
partOfName = agentNamesRegex.sub(
    r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(partOfName)

# Managing Complex Regexes
phoneRegexComplicated = re.compile(
    r'((\d{3} |\(\d{3}\))?(\s | - |\.)?\d{3}(\s | - |\.)\d{4}(\s*(ext | x | ext.)\s *\d{2, 5})?)')


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
