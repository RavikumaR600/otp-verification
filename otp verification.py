import os 
import math
import random 
import smtplib

digits = "01233456789"
OTP=""
for i in range(6):
    OTP+= digits[math.floor(random.random()*10)]
otp = OTP +" is your OTP"
msg = otp
s= smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("your Gmail Account", "your app password")
emailid = input("enter your email :")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("enter your OTP : ")
if a==OTP:
    print("Verified")
else:
    print("you have entered a wrong OTP")

#     ''' By enabling your gmail account security setting -> Allow less secure app, I was able to send a simple email from one gmail to another gmail account.

# WARNING: Allowing low security for apps accessing your Google account is not recommended by google. It can be a security threat. Turn it OFF after the experiment.'''