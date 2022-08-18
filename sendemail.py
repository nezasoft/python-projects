import sys, smtplib, socket
from getpass import getpass
message_template ="""To:{}
From:{}
Subject: Test Message from sendemail.py
Hello,
This is a test message sent to you from the login.py program in Foundations of Python Network Programming"""

def main():
    if len(sys.argv)<4:
        name = sys.argv[0]
        print("Syntax: {} Server fromaddr toaddr [toaddr..]".format(name))
        sys.exit(2)
        server, fromaddr, toaddr=sys.argv[1], sys.argv[2],sys.argv[3:]
        message = message_template.format(','.join(toaddr),fromaddr)
        username = input("Enter username:")
        password = getpass("Enter password:")

        try:
            connection = smtplib.SMTP(server)
            try:
                connection.login(username,password)
            except smtplib.SMTPException as e:
                print("Authentication failed:,e")
                sys.exit()

                connection.sendmail(fromaddr,toaddr,message)
            except(socket.gaierror,socket.error, socket.herror,smtplib.SMTPException) as e:
                print("Your message may not have been sent!")
                print(e)
                sys.exit(1)
            else:
                s = '' if len(toaddr)== 1 else 's'
                print("Message sent to {} recepient{}".format(len(toaddr),s))
                connection.quit()

if __name__ == '__main__':
            main()

