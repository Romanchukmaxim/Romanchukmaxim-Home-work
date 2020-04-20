def is_uppercase(inp):
    for i in inp:
        if i != i.upper():
            return False
        else:
            continue
    return True