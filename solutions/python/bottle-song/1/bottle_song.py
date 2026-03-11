def recite(start, take=1):
    number_to_text = [
    "no", "One", "Two", "Three", "Four", "Five", 
    "Six", "Seven", "Eight", "Nine", "Ten"
]
    
    result = []
    for number in range(start, start - take, -1):
        current_word = number_to_text[number]
        next_word = number_to_text[number - 1].lower()
        s_current = "" if current_word == "One" else "s"
        s_next = "" if next_word == "one" else "s"
        
        result.append(f"{current_word} green bottle{s_current} hanging on the wall,")
        result.append(f"{current_word} green bottle{s_current} hanging on the wall,")
        result.append(f"And if one green bottle should accidentally fall,")
        result.append(f"There'll be {next_word} green bottle{s_next} hanging on the wall.")
        
        if number != start - take + 1:
            result.append("")
        else:
            continue
        

    return result