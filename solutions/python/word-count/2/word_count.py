def count_words(sentence):
    separators = {":", "?", ";", ",", "!", ".", " ", "\n", "", "'", "_"}
    
    result_dic = {}
    for index, char in enumerate(sentence):
        if not char.isalpha():
            continue
        sentence = sentence[index::] + " "
        break
    
    start=0    
    for index, char in enumerate(sentence):
        if (not char.isalpha() and char != "'") or char.isnumeric():
            end = index - 1
            word = sentence[start:end + 1]
            word = word.strip(":?;,!.\t \n'&@$%^&_")
            start = end + 1
            if word in separators:
                continue
            result_dic[word.lower()] = result_dic.get(word.lower(), 0) + 1
    if not result_dic:
        return sentence
        
    return result_dic  