def cracker (number):
    secretmsg = ''
    with open ('encoded.txt') as file:
        lines = file.readlines()
        if 1 <= number <= len (lines):
            line=lines [number - 1 ].strip()
            for char in line:
                if char.isalpha():
                    secretmsg += char
            return secretmsg
            
secretmsg = cracker (int(input("")))
if secretmsg:
    print(secretmsg)   