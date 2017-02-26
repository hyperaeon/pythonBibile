# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import os
import sys
import datetime

py = '''#---------------------------------------------------
#To:
#---------------------------------------------------
#BY:
#---------------------------------------------------
'''

c = '''*---------------------------------------------------
*To:
*---------------------------------------------------
*BY:
*---------------------------------------------------
'''

if os.path.isfile(sys.argv[1]):
    print('%s already exist!' % sys.argv[1])
    sys.exit()

file = open(sys.argv[1], 'w')
today = datetime.date.today()
date = today.strftime('%Y') + '-' + today.strftime('%m') + '-' + today.strftime('%d')
filetypes = str.split(sys.argv[1], '.')
length = len(filetypes)
filetype = filetypes[length - 1]
if filetype == 'py':
    print('use python mode')
    file.writelines('# -*- coding:utf-8 -*-')
    file.wirte('\n')
    file.writelines('# File: ' + sys.argv[1])
    file.write('\n')
    file.write(py)
    file.write('# Date: ' + date)
    file.write('\n')
    file.write('#----------------------------------------------------------------')
elif filetype == 'c' or filetype == 'cpp':
    print('use c mode')
    file.writelines('/*')
    file.wirte('\n')
    file.writelines('* ----------------------------------')
    file.write('\n')
    file.write(c)
    file.write('* Date: ' + date)
    file.write('\n')
    file.write('*----------------------------------------------------------------')
    file.write('\n')
    file.write('*/ \n')
else:
    print('just create %s' % sys.argv[1])
file.close()
