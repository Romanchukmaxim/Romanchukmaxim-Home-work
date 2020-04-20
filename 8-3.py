def shorten_to_date(long_date):
    n = 0
    for i in long_date:
        if i != ',':
            n += 1
        else:
            break
    return long_date[0:n]