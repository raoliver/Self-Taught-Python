import re
l = "Beautiful is better than ugly"

zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

string = 'Two too.'

line = '123?34 hello?'

# matches = re.findall("Beautiful", l)

matches = re.findall('beautiful', l, re.IGNORECASE)#ignores the case of the expression

m = re.findall('^If', zen, re.MULTILINE) #Searches multiple lines fo the string

m2 = re.findall('t[ow]o', string, re.IGNORECASE) #searches for any occurence of T-(O or W)-O

linematch = re.findall('\d', line, re.IGNORECASE) # searches for digits in string

print(linematch)


t = '__one__ __two__ __three__'

found = re.findall('__.*?__', t)

for match in found:
    print(match)

line2 = 'I love $'

m3 = re.findall('\\$', line2, re.IGNORECASE)
print(m3)