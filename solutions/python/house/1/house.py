def recite(start_verse, end_verse):
    subject_dic = {
    1: ("house that Jack built"),
    2: ("lay in", "malt"),
    3: ("ate", "rat"),
    4: ("killed", "cat"),
    5: ("worried", "dog"),
    6: ("tossed", "cow with the crumpled horn"),
    7: ("milked", "maiden all forlorn"),
    8: ("kissed", "man all tattered and torn"),
    9: ("married", "priest all shaven and shorn"),
    10: ("woke", "rooster that crowed in the morn"),
    11: ("kept", "farmer sowing his corn"),
    12: ("belonged to", "horse and the hound and the horn")
}
    result = []

    for verse in range(start_verse, end_verse + 1):
        verse_result = ""
        
        if verse == 1:
            result =["This is the house that Jack built."]
            continue
            
        first_line = f" This is the {subject_dic[verse][1]} "
        verse_result += first_line
        last_line = "that lay in the house that Jack built."
        
        for line in range(0, verse - 2):
            filler_line = f"that {subject_dic[verse - line][0]} the {subject_dic[verse - line - 1][1]} "
            verse_result += filler_line
            
        verse_result += last_line
        verse_result = verse_result.strip()
        result.append(verse_result)
        
    return result