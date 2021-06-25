import random,math,os
import pywhatkit as kit
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP to verify your identity"
msg= otp

emailid = input("Enter your email: ")

kit.send_mail("mv1nayak231@gmail.com","mmmnewv2#51","New Email from pywhatkit Auomation by Vinayak",f"{msg}",f"{emailid}")
print("An OTP is sent to Your email please check your inbox")
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Your OTP Successfully Verified !!!")
    kit.send_mail("mv1nayak231@gmail.com","mmmnewv2#51","Email Verification","Your Email is Succesfully verified!!" ,f"{emailid}")
else:
    print("Incorrect OTP!!! \nPlease Check your OTP and try again")
