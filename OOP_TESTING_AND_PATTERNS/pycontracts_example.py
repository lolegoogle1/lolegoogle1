from contracts import contract


# Decorator
@contract(x='int, >=0', returns='int,>=0')
def f(x):
    return x

# f(-1)


# Docstring
@contract
def f2(n):
    '''
        Function description.
        :type n: int, >= 0
        :rtype: int, > 0
    '''
    pass


@contract
def f3(n: 'int, >= 0') -> 'int, >= 0':
    print("It's fine to receive such great identation with -> {} <- argument, which just have pivoted.".format(n))
    return n


f3(12)
