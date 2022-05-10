from fileapi import *
from encode import *

data = decode(read_file('/system/data/aydin-os.stat'))
if data == '0':
    import signup
elif data == '1':
    import login
else:
    print('Error')