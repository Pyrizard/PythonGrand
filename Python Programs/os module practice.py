'''This are multiple attributes written in a single file. '''


import os

x=os.getcwd()
print(x)

y=os.cpu_count()
print(y)

f=os.getlogin()
print(f)

foo=os.listdir()
print(foo)


#see here there is an additional backslash to avoid confusing python sine \t= tab and \\regular raw input
os.removedirs("C:\\TOAD")
os.rename("D:\Brother.txt","D:\\NiceBrother.txt")


#Below Helps to execute any Os program with link in
os.system("C:\Windows\system32\calc.exe")


#Ping the google’s website by sending 10 ICMP echo request packets.
os.system("ping -n 10 www.google.com")


#Name of operating system. For windows it will say 'nt'. if you want output as windows for your windows os use another module (import platform)
name_of_os = os.name
print(name_of_os)


#A string value that contains information about the current environment variables.Lol thats too much data much of which i dont understand
print(os.environ)



#This will change dir. Please note this is dir of ide terminal and not the directory of this .py file. To understand this better check cmd dir first[not in cmd but using os.getcwd() command].
#Then execute this code with new directory link. preferably use forward slash
print(os.getcwd())
os.chdir("C:/Users/Admin/Documents")
print(os.getcwd())
os.chdir("C:/Users/Admin/Contacts")
print(os.getcwd())
os.chdir("C:/Users/Admin/Documents/GitHub/PCube-PythonProgramsPyrizard")
print(os.getcwd())



#Only for Unix Like systems : Returns information about the operating system version, hostname, and the kernel version of this system.
ccxcc = os.uname()
print(ccxcc)


#Check system date
os.system("date")
