#this is the algorithm for the cipher
def atbash(character_):
    output = ""
    for i in character_ :
        extract = ord(i)
        if 65 <= extract <= 90:
            output += chr(155 - extract)
        elif 97 <= extract <= 122:
            output += chr(219 - extract)
        else:
            output += i
    return output
