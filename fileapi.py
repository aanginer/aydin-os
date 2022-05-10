from collections import defaultdict
import os
from encode import decode,encode

def reload():
    global files
    fs = []

    for root, dirs, files in os.walk('C:\\aydin-os\\root'):
        for file in files:
            fs.append(root + '\\' + file)
        for dir in dirs:
            fs.append(root + '\\' + dir)

    for idx in range(len(fs)):
        fs[idx] = fs[idx].replace('\\','/').replace('C:/aydin-os/root','')

    files = defaultdict(dict)
    s = '{}'

    for f in fs:
        f2 = f.split('/')
        estring = 'files'
        for f3 in f2:
            if f3 == '':
                f3 = '/'
            if os.path.isfile('C:/aydin-os/root' + f):
                s = '"file"'
            else:
                s = '{}'
            estring += '["' + f3 + '"]'
        estring += f' = {s}'
        exec(estring)

reload()

def _openfile():
    reload()
    done = False
    _dir = 'root'
    dir2 = 'files["/"]'
    while not done:
        os.system('cls')
        print('folder: ' + _dir)
        for f in eval(dir2):
            print(f)
        x = input('which one: ')
        if not x in eval(dir2):
            print('invalid')
            continue
        dir2 += '["' + x + '"]'
        if eval(dir2) == 'file':
            done = True
            return _dir + '/' + x
        if _dir == 'root':
            _dir = '/' + x
        else:
            _dir += '/' + x

def _savefile(content: str, file_name: str):
    reload()
    done = False
    _dir = 'root'
    dir2 = 'files["/"]'
    while not done:
        os.system('cls')
        print('folder: ' + _dir)
        print('len',len(eval(dir2)))
        if len(eval(dir2)) == 0:
            done = True
            with open('C:/aydin-os/root' + _dir + '/' + file_name, 'w') as f:
                f.write(content)
            return True
        for f in eval(dir2):
            print(f)
        x = input('which one: ')
        if not x in eval(dir2):
            print('invalid')
            continue
        dir2 += '["' + x + '"]'
        if _dir == 'root':
            _dir = '/' + x
        else:
            _dir += '/' + x

def _sf():
    reload()
    done = False
    _dir = 'root'
    dir2 = 'files["/"]'
    while not done:
        os.system('cls')
        print('folder: ' + _dir)
        print('len',len(eval(dir2)))
        if len(eval(dir2)) == 0:
            done = True
            file_name = input('file name: ')
            content = input('content: ')
            with open('C:/aydin-os/root' + _dir + '/' + file_name, 'w') as f:
                f.write(content)
            return True
        for f in eval(dir2):
            print(f)
        x = input('which one: ')
        if not x in eval(dir2):
            print('invalid')
            continue
        dir2 += '["' + x + '"]'
        if _dir == 'root':
            _dir = '/' + x
        else:
            _dir += '/' + x

def create_dir(dir_name: str):
    if not os.path.exists('C:/aydin-os/root' + dir_name):
        fn = 'C:/aydin-os/root' + dir_name
        print(fn)
        os.makedirs(fn)

def write_file(file_name: str, content: str):
    with open('C:/aydin-os/root' + file_name, 'w') as f:
        f.write(content)

def read_file(file_name: str):
    try:
        with open('C:/aydin-os/root' + file_name, 'r') as f:
            return f.read()
    except Exception as e:
        print(e)
        return -1

def get_username():
    return decode(read_file('/system/data/currentuser.stat'))

def set_modes(modes: list):
    with open('C:/aydin-os/root/system/data/modes.stat', 'w') as f:
        for mode in modes:
            f.write(encode(mode) + '\n')