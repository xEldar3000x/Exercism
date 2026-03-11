def find_anagrams(word, candidates):
    letter_list = list(word.lower())

    result = []
    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue
        elif len(candidate) == len(letter_list) and sorted(candidate.lower()) == sorted(letter_list):
            result.append(candidate)

    return result
            
        
