#!/usr/bin/env python
def uniq(list, allowed_duplicate_count=1):
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
        if item not in d:
            d[item] = [ [index, item] ]
        elif len(d[item]) < allowed_duplicate_count:
            d[item].append( [index, item] )

    return [ value for index, value in
             sorted([ word_index_pair for word_index_list in d.values() for word_index_pair in word_index_list ], # flatten one level deep
                    key=lambda item: item[0]) ] # sort on the first value

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
