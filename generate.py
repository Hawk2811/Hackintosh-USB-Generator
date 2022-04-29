#
#       generate.py
# Copyright (c) 2022 Hawk2811
#
#

#import libraries
import os

def wininstall(): # Windows Generator
    if os.path.isdir(".\usb"):
        print("Where Install EFI")
        drive = input("Disk Letter: ")
        os.mkdir(drive + "\\com.apple.recovery.boot")
        os.system("xcopy /e /y .\usb\\EFI " + drive + "\\EFI")
        os.system("copy ")# Incomplete

def unixinstall(): # UNIX-Platforms(macOS, Linux, BSDs, etc) Generator
    pass # Incomplete

def main():
    print("*** Hackintosh USB Generator ***")
    print("loading....")
    if os.name == "nt": # Check OS
        wininstall()
    else:
        unixinstall()

main()