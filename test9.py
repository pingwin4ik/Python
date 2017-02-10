string1 = '[]'
string2 = '[[]]'
string3 = '[[[]]]'
string4 = ']['
string5 = '][]['
string6 = '[]][[]'

def test(string):
    length = len(string)
    if length % 2 == 0:
        half = length / 2
        first = '[' * half
        last = ']' * half
        if string[0:half] == first and string[half:length] == last:
            return 'OK'
        else:
            return 'NOT OK'
    else:
        return 'NOT OK'

print test(string1)
print test(string2)
print test(string3)
print test(string4)
print test(string5)
print test(string6)