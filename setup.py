from encode import *
from fileapi import *
import appapi as ap
    
apps = 'git.cybercoding.tools.browse\nos.aydin-os.system.commandline\n'

create_dir('/system/data')
create_dir('/system/apps')
create_dir('/users')
create_dir('/apps')
create_dir('/AppData')
write_file('/system/data/aydin-os.stat', encode('0'))
write_file('/system/data/currentuser.stat', encode(''))
write_file('/system/apps/apps.list', apps)
write_file('/system/data/modes.stat', encode('user\n'))
write_file('/system/data/modes.stat', '')
ap.py_to_app('apps/browse.py','git.cybercoding.tools.browse') # found.author.catergory.name
ap.py_to_app('apps/commandline.py','os.aydin-os.system.commandline')

import loader