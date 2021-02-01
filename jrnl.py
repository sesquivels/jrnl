#!/usr/bin/python3
import os, subprocess, datetime,sys

class osInteract:
    #atributes
    version = ""
    hostname = ""
    osdate = datetime.date
    menuOption = ""
    environmentOption = ""


    #methods
    #initialized class
    def __init__(self):
      return

    def __del__(self):
      return

    def timeOS(self):
        self.osdate = os.popen('date ').read()
        print(self.osdate)

    def menu(self):
        os.system("clear")
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
        if self.menuOption == "":
            self.osdatemenuOption = 3
            print("pressed Enter will closed")
        if self.menuOption == "1":
            print("local")
        if self.menuOption == "2":
            print("network")

        if self.menuOption == 3:
            os.system("clear")
            sys.exit(0)

    def evironment(self):
        print("Wellcome to jrnl app")
        self.environmentOption = input("please set which pc is this, laptop, pi, workstation or  nas: ")
        print("you choose:nas " + self.environmentOption)


m1 = osInteract()
m1.evironment()





