def transform(legacy_data):
    new_dictionary = {}
    for point_value in legacy_data:
        for letter in legacy_data[point_value]:
            new_dictionary[letter.lower()] = point_value 

    return new_dictionary
