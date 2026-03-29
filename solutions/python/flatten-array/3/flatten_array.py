def flatten(iterable):
    opened_box = []

    if iterable is None:
        return opened_box

    for thing in iterable:
        if isinstance(thing, int):
            opened_box.append(thing)

        elif isinstance(thing, list):
            inner_things = flatten(thing)
            opened_box.extend(inner_things)

    return opened_box
        
            