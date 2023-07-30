"""""
1)	Assume that you have a message like "hello", your message was encrypted to be like "khoor"
write programming code to decrepit the following message to get the original one.
Message = "|rx#duh#juhdwh"
"""

msg=input("Enter the message: ")
for i in msg:
    ascii=int(ord(i)-3)
    print(chr(ascii),end="")