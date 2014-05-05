__author__ = 'pedro'

from easygui import passwordbox
import smtplib

class EmailSender:
    def __init__(self, user, password, server):
        self.user = user
        self.server = server
        self.password = password
        self.server = smtplib.SMTP(server)
        self.server.starttls()
        self.server.login(self.user, self.password)

    def send(self, toaddrs, msg):
        x = self.server.sendmail(self.user, toaddrs, msg)
        print x

    def quit(self):
        self.server.quit()





if __name__ == '__main__':
    username = raw_input("Your Gmail:")
    password = passwordbox("What is your password ?")
    sendto = raw_input("Send email to:")
    emailtest = EmailSender(username, password, "smtp.gmail.com:587")
    emailtest.send(sendto, "This is a test email!!")
    emailtest.quit()



