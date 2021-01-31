import os, sys

print("")
print("")
print("Wellcome to JRNL scripting tool")
print("")
print("")
print("************************************************")
print("******************MENU**************************")
print("************************************************")
print("")
print("")
print("OPTIONS:")
print("")
print("1)..................................Local Jornal")
print("2)................................Network Jornal")
print("2)..........................................Exit")
print("")
print("")
menuOption = input("Please enter something, default option will be Exit ")
if menuOption == "":
    menuOption = 3

if menuOption== 1:
    print("local")
if menuOption==2:
    print("network")

if menuOption == 3:
    os.system("clear")
    sys.exit(0)





