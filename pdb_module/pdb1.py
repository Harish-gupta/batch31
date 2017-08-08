"""
To explain pdb module
"""
NUMBER1 = 10
NUMBER2 = 20
print RESULT1

class OwnException(Exception):
    '''
    own exception class
    '''
    pass

def fun(param1, param2):
    """
    To ad two numbers
    Parm:param1: int,
    Param: param2: int,
    return: int
    issues:
        expecting only ntegers
    Example:
    fun(10,20)
    The return value: 30
    """
    try:
        print "this is function"
        print "a1=%s, b1=%s" % (param1, param2)
        return param1 + param2
    except (own_exception, Exception) as err:
        print err
        return None

RESULT = NUMBER1 + NUMBER2
print "result=", RESULT
RESULT1 = fun(100, 200)
print "result1=", RESULT1
for i in range(-3, 3):
    if i != 0:
        print 10 / i
    else:
        print i
print "some other statement sin program "
print "program ended"
