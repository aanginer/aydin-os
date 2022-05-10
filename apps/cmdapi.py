# region boilerplate
from encode import *
from fileapi import *
from dbapi import *
import time

running = True
username = get_username()

cmdhelp = """
Commandline help:
keywords:
    top: top of the stack (pops it)
preixes:
    sudo: run as admin
    as <username>: run as another user
commands:
    help: shows this help
    db <command> <val[optional]>: database commands (db help for more info)
    exit <code>: exits the program with the given exit code
    encrypt <text>: encrypts the text prints and pushes it to the stack
    decrypt <text>: decrypts the text prints and pushes it to the stack
    username: prints the username and pushes it to the stack
    eula: prints the eula
    echo <text[multiple]>: prints the text
    table <table>: view sql table
    sqlget <query>: runs the query and pushes the result to the stack prints too
    mode <mode> (must be run as admin): changes the mode (see mode help for more info)
"""

modehelp = """
Mode help:
modes:
    admin: all commands are run as admin
    dev: debug information
    debug: same as dev
    encode: encodes args
    encrypt: same as encode
"""

dbhelp = """
Database help:
prefix: db
commands:
    help: show this help
    post: post a message to the database 
    get: get all messages from the database 
    clear: clear all messages from the database 
"""

eula = """
███████╗██╗░░░██╗██╗░░░░░░█████╗░
██╔════╝██║░░░██║██║░░░░░██╔══██╗
█████╗░░██║░░░██║██║░░░░░███████║
██╔══╝░░██║░░░██║██║░░░░░██╔══██║
███████╗╚██████╔╝███████╗██║░░██║
╚══════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
▄▀ █▀▀ █▄░█ █▀▄   █░█ █▀ █▀▀ █▀█   █░░ █ █▀▀ █▀▀ █▄░█ █▀ █▀▀   ▄▀█ █▀▀ █▀█ █▀▀ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ ▀▄
▀▄ ██▄ █░▀█ █▄▀   █▄█ ▄█ ██▄ █▀▄   █▄▄ █ █▄▄ ██▄ █░▀█ ▄█ ██▄   █▀█ █▄█ █▀▄ ██▄ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ▄▀


█▀█ █▀█ █▀█ █▀▄ █░█ █▀▀ ▀█▀
█▀▀ █▀▄ █▄█ █▄▀ █▄█ █▄▄ ░█░

Many companies DO NOT offer the user the product, but license it. We at aydin-os are proud to say that we offer the product to you and not some license. YOU have access to the product, and you can use it as you please as long as you do not use it for illegal purposes or breach this agreement.


█░█ █▀ ▄▀█ █▀▀ █▀▀
█▄█ ▄█ █▀█ █▄█ ██▄

The user must accept this agreement to use the software. So long as you use the software, you agree to this agreement and cannot override it without our permission. If you so wish to change the eula, you can do so by emailing us your request. We may accept your request to change the eula at any time. If we do, we will notify you of the change. Email to contact us at: aydinanginer087@gmail.com. If you wish to terminate the eula, you may do so by emailing us your request. We may accept your request to terminate the eula at any time. If we do, we will notify you of the termination. You must present a valid reason for terminating the eula. 


█▀█ █▀█ █ █░█ ▄▀█ █▀▀ █▄█
█▀▀ █▀▄ █ ▀▄▀ █▀█ █▄▄ ░█░

The main privacy concern for aydin-os is the MySql database connected to the OS. All information stored in the database can be accessed by the command line. If the user wishes to put sensitive information in the database, they must use the command line to access the database. The user must be careful to not use the command line to access sensitive information. To encrypt sensitive information, the user must use the password encryption software.
-----------------
shell
-> encrypt <your info here>
-> db post top 
----------------
This will post your sensitive info to the database encrypted. You may not use the command line to access sensitive information of other users. This includes passwords, which are stored in the database (encrypted). You may noy decrypt any encrypted information without permission from the person who encrypted it. If you would like to encrypt and decrypt your own information, see https://github.com/aanginer/aydinOS-docs/blob/master/readmes/encode.md for more information. Another concern is that the system files are easily accessed in the file explorer. To ensure nobody can access the system files, use the following on the command line:
-----------------
shell
-> fileapi -settings
-> set system_files_user sudo_ 
-> set top unchangable         <-------- ensures that this cannot be changed
-> end -settings
-> sudo disable user sudo_     <-------- disables the user sudo_, so the files cannot be accessed
----------------
to get back access to those files
-----------------
shell
-> new user sudo_
-> sudo enable user sudo_
-> password <enter password>
-> sudo delete new user
----------------
The process is quite complex, sorry about that. The reason system file access is not disabled by default is that it is very useful for software developers and modders to view game files or system files.

If a privacy bug occurs, contact us at aydinanginer087@gmail.com


█░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀
█▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█

Hacking into aydin-os is allowed for educational purposes, and we encourage people learning to hack to use our software to understand things about databases. You may also decompile the code in whatever way you want, so long as you do not claim it as your own. You do not have to even decompile, as the software is open-source. You may not hack or decompile for malicious purposes such as creating a proxy to track whenever a new user signs up, then taking that users information (username and password). Any hacking will not be tolerated unless you are in development mode.
-----------------
shell
-> sudo mode dev
-> sudo set_user dev
----------------


█ █▄░█ █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ ▀█▀ █ █▀█ █▄░█
█ █░▀█ █▀░ █▄█ █▀▄ █░▀░█ █▀█ ░█░ █ █▄█ █░▀█

The software is open-source the emulator source code can be accessed at: https://github.com/aanginer/aydin-os 
.
The documentation is incomplete and should not be relied on. If you would like to access it for whatever reason, you can do so at: https://github.com/aanginer/aydinos-docs
This software is provided as is, and we are not responsible for any damages that may occur.
We are not liable for any damages or privacy breaches caused by the user.


▄▀█ █▀█ █▄▄ █ ▀█▀ █▀█ ▄▀█ ▀█▀ █ █▀█ █▄░█
█▀█ █▀▄ █▄█ █ ░█░ █▀▄ █▀█ ░█░ █ █▄█ █░▀█

Any user may not file a lawsuit against aydin-os. If you do, you will be removed from the system.


█▀▀ █░█ ▄▀█ █▄░█ █▀▀ █▀▀ █▀
█▄▄ █▀█ █▀█ █░▀█ █▄█ ██▄ ▄█

Any changes in the EULA must be followed after 30 days of them being implemented. If you weren't breaking the EULA before, and a change comes into effect and you continue after 30 days with the changes announced, you will be banned from the system. If you would like to submit a change for the EULA, you may do so by emailing us at: aydinangner087@gmail.com. These changes will be reviewed and announced on github.

█▀▀ █▄░█ █▀▄
██▄ █░▀█ █▄▀

Thank you for reading the EULA. If you have any questions, please email us at aydinanginer087@gmail.com
"""

exit_meanings = {
    0: "You have exited the program.",
    1: " An error has occured.",
    69: "What are you doing? You're not supposed to be here.",
    404: "The requested command was not found.",
    405: "Arguments are not correct.",
    500: "The server encountered an error.",
    501: "Deprecated command.",
    200: "The command was executed successfully, command to exit",
}

def exit_program(exit_code: int):
    if exit_code != 0:
        print(f"Exited abnormally with code {exit_code}: {exit_meanings[exit_code]}")
    else:
        print(f"Done")

for i in range(2,404):
    if not i == 69 or not i == 200:
        exit_meanings[i] = "Exiting the program"

for i in range(405,499):
    exit_meanings[i] = "An error has occured"

for i in range(502,600):
    exit_meanings[i] = "The server encountered an error"

for i in range(601,700):
    exit_meanings[i] = "Command was not executed correctly"

for i in range(701,800):
    exit_meanings[i] = "Command is deprecated"

for i in range(801,900):
    exit_meanings[i] = "Command is not implemented/not found"

for i in range(901,1000):
    exit_meanings[i] = "Permission denied"

for i in range(1001,10000):
    exit_meanings[i] = "What are you doing? You're not supposed to be here."

def find_col(line,coln):
    col = coln
    try:
        char = line[col]
    except:
        return -1
    while char.isspace() and col < len(line):
        col += 1
        try:
            char = line[col]
        except IndexError:
            return -1 # string is empty or ends with whitespace
    return col

def find_col_end(line,coln):
    col = coln
    char = line[col]
    while not char.isspace() and col < len(line):
        col += 1
        try:
            char = line[col-1]
            if char == "'" or char == '"':
                ochar = char
                s = ""
                s += char
                col += 1
                char = line[col]
                while char != ochar and col < len(line):
                    col += 1
                    char = line[col]
                    s += char
                col += 1
                return col
        except IndexError:
            return -1
    return col

def filter(cm: str):
    args = []
    loc = 0
    endloc = 0
    while endloc != -1 and loc != -1:
        loc = find_col(cm,endloc)
        endloc = find_col_end(cm,loc)
        cmd = cm[loc:endloc]
        cmd = cmd.strip()
        args.append(cmd)
    return args[:-1]

#endregion boilerplate

def run(args: list[str],stack: list[str|int],_cmd: str,path):
    global username
    username = get_username()
    running = True
    _modes = []
    with open('C:/aydin-os/root/system/data/modes.stat','r') as f:
        for line in f.readlines():
            if line == '\n':
                continue
            _modes.append(decode(line.strip('\n')))
    debug = 'debug' in _modes
    admin = 'admin' == decode(read_file("/system/data/currentuser.stat")) or 'admin' in _modes
    encmode = 'encode' in _modes
    if args[0] == 'help':
        print(cmdhelp)
    if encmode:
        for i,_arg in enumerate(args):
            args[i] = swap(_arg)
    _args = args.copy()
    if encmode:
        for i,_arg in enumerate(args):
            args[i] = deswap(_arg)
    st = time.time()
    if args[0] == 'as':
        username = args[1]
        if username == 'sudo_':
            admin = True
        else:
            admin = False
        args = args[2:]
    if args[0] == "sudo":
        args = args[1:]
        admin = True
    if args[0] == "exit":
        if len(args) == 1:
            args.append("1")
        if args[1] != "0":
            print(f"Exited abnormally with code {args[1]}: {exit_meanings[int(args[1])]}")
        else:
            print(f"Done")
        return False
    elif args[0] == 'encrypt':
        if len(args) == 1:
            print("Please enter a string to encrypt")
        else:
            h = encode(args[1])
            stack.append(h)
            print(h)
    elif args[0] == 'decrypt':
        if len(args) == 1:
            print("Please enter a string to encrypt")
        else:
            h = decode(args[1])
            stack.append(h)
            print(h)
    elif args[0] == 'db':
        mode = args[1]
        if mode == 'post':
            post(args[2], username)
        elif mode == 'get':
            l = []
            for i in get(username):
                l.append(i[0])
            stack.append(l)
            print(l)
            print(f"fetched {l} from {username}'s posts")
        elif mode == 'clear':
            clear(username)
        elif mode == 'sql':
            execute(args[2]) # sql query should be in double quotes
        elif mode == 'help':
            print(dbhelp)
    elif args[0] == 'username':
        stack.append(username)
        print(username)
    elif args[0] == 'eula':
        print(eula)
    elif args[0] == 'table':
        data = getDict(args[1])
        stack.append(data)
        print(data)
    elif args[0] == 'sqlget':
        data = fetch(args[1])
    elif args[0] == 'echo':
        print((_arg for _arg in args[1:]),sep="")
    elif args[0] == 'mode':
        mode = args[1]
        if not admin:
            print("You are not an admin")
        else:
            if mode == 'dev':
                debug = True
                _modes.append('debug')
                print("Dev/Debug mode enabled")
            elif mode == 'debug':
                debug = True
                _modes.append('debug')
                print("Dev/Debug mode enabled")
            elif mode == 'user':
                debug = False
                print("No mode enabled")
                _modes.clear()
            elif mode == 'encrypt':
                encmode = True
                print("Encryption mode enabled")
                _modes.append('encode')
            elif mode == 'encode':
                encmode = True
                print("Encryption mode enabled")
                _modes.append('encode')
            elif mode == 'admin':
                admin = True
                print("Warning: All commands will be run as admin")
                _modes.append('admin')
            elif mode == 'help':
                print(modehelp)
    elif args[0] == 'fs':
        # get all folders in directory path
        print('fs')
        if len(args) == 1:
            print("Please enter a directory")
        tags = args[1:]
        dirs = False
        files = False
        for tag in tags:
            if tag == '-d':
                dirs = True
            elif tag == '-f':
                files = True
        # find all directories in path
        fdirs = []
        if dirs:
            fdirs = []
            for root, _dirs, files in os.walk('C:\\aydin-os\\root' + path):
                for dir in _dirs:
                    print(os.path.join(root,dir).replace('\\','/').replace('C:/aydin-os/root',''))
                    fdirs.append(os.path.join(root,dir).replace('\\','/').replace('C:/aydin-os/root',''))
        # find all files in path
        ffiles = []
        if files:
            ffiles = []
            for root, dirs, _files in os.walk('C:\\aydin-os\\root' + path):
                for file in _files:
                    print(os.path.join(root,file).replace('\\','/').replace('C:/aydin-os/root',''))
                    ffiles.append(os.path.join(root,file).replace('\\','/').replace('C:/aydin-os/root',''))

        final = fdirs + ffiles
        stack.append(final)
        for i in final:
            print(i)
    elif args[0] == 'cd':
        if len(args) == 1:
            print("Please enter a directory")
        else:
            path = args[1]
    else:
        print(f"Bash: command '{_cmd}' not found args:{args}")
        exit_program(404)
    et = time.time()
    set_modes(_modes)
    if debug:
        print(f"Executed in {et-st} seconds")
        print(f"Stack: {stack}")
        print(f"Args: {_args}")
        print(f"Cmd: {_cmd}")
        print(f"Modes: {_modes}")
        print(f"Path: {path}")
    return running,debug,path