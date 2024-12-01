punc='''!()-[]{};:'"\,<>/?@#$%^&*_'''

string=input("Enter anything here:")
emstr=""

for i in string:
    if i not in punc:
        emstr=emstr+i
