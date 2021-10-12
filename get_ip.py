import socket
# written by Albara'a Alhamidi
print("      ####################################")
print("      #   Thank you for work my script ❤ #")
print("      #       instgram :  xx9b1r         #")
print("      ####################################")

def get_ip(website):
    try:
        ips=socket.gethostbyname(website)
    except IOError:
         print("Error URL failed, Try again ")
         get_ip(website=input("Enter website again : "))
    else:
        print("IP website is {}".format(ips))
get_ip(website=input("Enter website only https or http : "))



