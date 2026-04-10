def abbreviate(words):
    words = words.replace("-", " ")
    words = words.replace(",", "")
    words = words.replace("'s", "")
    words = words.replace("_", "")

    return "".join([word[0].upper() for word in words.split()])
        
        
    
