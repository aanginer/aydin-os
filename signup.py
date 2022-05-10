import os
from encode import *
from fileapi import *
from dbapi import *
print("""
░█████╗░██╗░░░██╗██████╗░██╗███╗░░██╗░░░░░░░█████╗░░██████╗  ░░███╗░░
██╔══██╗╚██╗░██╔╝██╔══██╗██║████╗░██║░░░░░░██╔══██╗██╔════╝  ░████║░░
███████║░╚████╔╝░██║░░██║██║██╔██╗██║█████╗██║░░██║╚█████╗░  ██╔██║░░
██╔══██║░░╚██╔╝░░██║░░██║██║██║╚████║╚════╝██║░░██║░╚═══██╗  ╚═╝██║░░
██║░░██║░░░██║░░░██████╔╝██║██║░╚███║░░░░░░╚█████╔╝██████╔╝  ███████╗
╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝╚═╝░░╚══╝░░░░░░░╚════╝░╚═════╝░  ╚══════╝
""")

print("To use aydin-os, please sign up first.")
print("You must also accept the eula.")
print("""
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
-> $py encode.encrypt <your info here>
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
""")

acc = 'n'

while acc != 'y':
    acc = input("Do you accept the eula? (y/n) ")
    if acc == 'y':
        print("Thank you for accepting the eula")
    elif acc == 'n':
        print("You must accept the eula to use aydin-os.")
    else:
        print("Please enter y or n.")

os.system('cls')

username = input("Username: ")
password = input("Password: ")

# for safety reasons, clear the screen
os.system('cls')

cpass = ''
while cpass != password:
    cpass = input("Confirm password: ")
    if cpass != password:
        print("Passwords do not match.")
    else:
        print("Passwords match.")

print("Success\nPlease log in.")

execute(f'INSERT INTO users (username, password) VALUES ("{username}", "{encode(password)}")')

create_dir(f'/users/{username}/data')
write_file(f'/system/data/currentuser.stat', encode(username))
write_file(f'/system/data/aydin-os.stat', encode('1'))

import login