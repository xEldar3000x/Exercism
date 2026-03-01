def rows(letter):

    forward = []

    forward.append(f"{chr(32) * (ord(letter) - 65 )}{chr(65)}{chr(32) * (ord(letter) - 65)}")
        
    for index in range(0, ord(letter) - 65):

        forward.append(f"{chr(32) * (ord(letter) - 66  - index)}{chr(66 + index)}{chr(32) * ((index * 2) + 1)}{chr(66 + index)}{chr(32) * (ord(letter) - 66 - index)}")

    for line in reversed(forward[0: ord(letter) - 65]):

        forward.append(line)

    return forward
