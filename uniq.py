def uniq(list, keep_dupes=1):
    """return uniq elements in a list

    >>> test_list = [ 'no', 'way', 'way', 'friend', 'hello', 'there', 'my', 'way', 'friend' ]
    >>> uniq(test_list)
    ['no', 'way', 'friend', 'hello', 'there', 'my']
    >>> uniq(test_list, 2)
    ['no', 'way', 'way', 'friend', 'hello', 'there', 'my', 'friend']
    >>> uniq(test_list, 3)
    ['no', 'way', 'way', 'friend', 'hello', 'there', 'my', 'way', 'friend']
    """

    d = {}
    for index, item in enumerate(list):
        if not d.has_key(item):
            d[item] = [ [index, item] ]
        elif len(d[item]) < keep_dupes:
            d[item].append( [index, item] )

    return [value for index, value in sorted([item for key in d.values() for item in key], key=lambda item: item[0])]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

