
import re
regexp = re.compile( r"[-a-zA-Z]+,"             # last name and comma
                r" [-a-zA-Z]+"                  # first name
                r"( [-a-zA-Z]+)?"               # optional middle name
                r": (\d\d\d-)?\d\d\d-\d\d\d\d"  # colon and phone number
                )
file = open("sample.txt", 'r')
for line in file.readlines():
    print("Input Line =>", line)
    if regexp.search(line) != None  :
        print("Yeah, I found a correct line:")
    else : print("Something Worong")


file.close()


#####
print("\n\n 더 나은 버전\n\n")

regexp = re.compile(r"(?P<last>[-a-zA-Z]+),"    # last name and comma
                r" (?P<first>[-a-zA-Z]+)"       # first name
                r"( (?P<middle>([-a-zA-Z]+)))?" # optional middle name
                r": (?P<phone>(\d\d\d-)?\d\d\d-\d\d\d\d)" # colon and phone number
                )
file = open("sample.txt", 'r')
for line in file.readlines():
    result = regexp.search(line)
    if result == None:
        print("Oops, I don't think this is a record")
    else:
        lastname = result.group('last')
        firstname = result.group('first')
        middlename = result.group('middle')
        if middlename == None:
            middlename = ""
        phonenumber = result.group('phone')
        print('이름: ' + firstname + ' ' + middlename + ' ' + lastname + '   전화번호: ' + phonenumber)

file.close()

