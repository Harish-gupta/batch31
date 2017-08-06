#import module1
'''
import file1
file1.fun()
'''
'''
import file2
import module1
#print module1.f1.fun()
import module1
print module1.f1.fun()
print module1.f2.fun()
'''
#import module1
#from module1 import hr
#import module1
'''
from module1 import hr
print hr.fun()
'''
'''
import module1
print module1.hr.fun()
'''
'''
from module1 import hr,f1
print hr.fun()
print f1.fun()
'''
'''
import module1
print module1.inner.if1.fun()
'''
'''
from module1 import inner
print inner.if1.fun()
'''
'''
from module1.inner import if1
print if1.fun()
'''
import sys
sys.path.append('/home/tcloudost/Desktop')
import module1

