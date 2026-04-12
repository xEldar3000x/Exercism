def decode(string):
    result = []
    start = 0
    end = 0
    while start < len(string):
        if string[start].isnumeric():
            end = start + 1
            while string[end].isnumeric():
                end += 1
            print(string[start : end])
            result.append(int(string[start : end]) * string[end])
            start = end + 1
        else:
            result.append(string[start])
            start += 1
        
    return "".join(result)

def encode(string):
    string = string + "1"
    start = 0
    result = []
    for end in range(len(string)):
        if string[start] != string[end]:
            if end - start == 1:
                quantity = ""
            else:
                quantity = str(end - start)
            result.append(quantity + string[start])
            start = end

    return "".join(result)
    
            
