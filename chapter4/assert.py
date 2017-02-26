__author__ = 'hzliyong'


l = []
# assert len(l)
try:
    assert len(l),'Error'
except:
    print('Error')
else:
    print('No Error')
l.append(1)
assert len(l)