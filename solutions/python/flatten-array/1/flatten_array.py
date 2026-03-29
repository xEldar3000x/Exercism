def open_the_box(box):
    
    opened_box = []
    for thing in box:
        opened_box.append(thing)
        
    return opened_box

def check_for_instance(box, result):
            
    if box is None:
        pass
    
    elif isinstance(box, int):
        result.append(box)
        return True
    
    elif isinstance(box, list):
        result.extend(open_the_box(box))
        return True
    

    return False


def flatten(iterable):
    result = []
    while True:
        for box in iterable:
            check_for_instance(box, result)
        iterable = result.copy()
        try:
            sum(iterable)
            return iterable
        except TypeError:
            result.clear()
    return iterable
        
