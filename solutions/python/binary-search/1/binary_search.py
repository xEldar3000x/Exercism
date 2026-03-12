def find(search_list, value):
    if search_list == []:
        raise ValueError("value not in array")

    mid_index = len(search_list) // 2
    start = 0
    end = len(search_list)
    while value != search_list[mid_index]:
        if len(search_list[start: end]) == 1:
            raise ValueError("value not in array")
        if value < search_list[mid_index]:
            end = mid_index
            mid_index = len(search_list[start: end]) // 2
        elif value > search_list[mid_index]:
            start = mid_index
            mid_index = len(search_list[mid_index:end]) // 2 + mid_index
    
    return mid_index