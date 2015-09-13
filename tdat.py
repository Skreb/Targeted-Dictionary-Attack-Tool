# imports

import time

# intro

print(" ___________  ___ _____ ")
print("|_   _|  _  \/ _ \_   _|")
print("  | | | | | / /_\ \| |  ")
print("  | | | | | |  _  || |  ")
print("  | | | |/ /| | | || |  ")
print("  \_/ |___/ \_| |_/\_/  ")
print("Targeted Dictionary Attack Tool")
print("Version 0.01")
print(" ")
print(" ")
print("DISCLAIMER: DO NOT USE THIS TOOL TO DO ANYTHING ILLEGAL!")
print(" ")
print("Created by Spencer")
print("www.punkrocktec.com")
print("Email: spencer@punkrocktec.com")


# Usage Instructions

time.sleep(1)
print(" ")
print(" ")
print("The tool will now ask you a few questions.")
print("Please answer as many as you can to build the best possible word list")
print("Unknown answers can be left blank")
print("")

time.sleep(1)

# Basic Target Information
# This will be the most common information about the target

FirstName = input("Target's first name: ")
LastName = input("Target's last name: ")
TargetYear = input("Target date of birth YEAR: ")
TargetMonth = input("Target date of birth MONTH: ")
TargetDay = input("Target data of birth DAY: ")


def main():

    married = input("Is the target married? Y , N")
    kids = input("Does the target have a kid? Y , N")
    pets = input("Does the target have a pet? Y , N")
    if married == "Y":
        targetspousename = input("Spouse Name: ")
        targetmarrieddate = input("What year was the target married on? ")
    elif married == "N":
        targetspousename = ""
        targetmarrieddate = ""
    else:
        print("Please enter Y or N")

    if kids == "Y":
        targetkidname = input("Child first name: ")
        targetkidage = input("Child year of birth: ")
    elif kids == "N":
        targetkidname = ""
        targetkidage = ""
    else:
        print("Please answer Y or N")

    if pets == "Y":
        targetpetname = input("Pet's name: ")
        targetpettype = input("What kind of pet? ")
    elif pets == "N":
        targetpetname = ""
        targetpettype = ""
    else:
        print("Please answer Y or N")


# Will add option to add additional info later

# Create the word list using the data we obtained
# Will probably clean this up in the future

    print("Creating list of possible passwords...This may take some time")
    file = open(FirstName + 'password.txt', 'w')
    file.write(FirstName)
    file.write("\n")
    file.write (FirstName + LastName)
    file.write("\n")
    file.write(LastName + FirstName)
    file.write("\n")
    file.write(LastName)
    file.write("\n")
    file.write(FirstName + LastName + TargetYear)
    file.write("\n")
    file.write(FirstName + TargetYear)
    file.write("\n")
    file.write(LastName + TargetYear)
    file.write("\n")
    file.write(TargetYear + FirstName + LastName)
    file.write("\n")
    file.write(FirstName + LastName + TargetDay)
    file.write("\n")
    file.write(FirstName + LastName + TargetMonth)
    file.write("\n")
    file.write(FirstName + LastName + TargetDay + TargetMonth + TargetYear)
    file.write("\n")
    file.write(FirstName + targetspousename)
    file.write("\n")
    file.write(targetspousename + LastName)
    file.write("\n")
    file.write(targetspousename + FirstName)
    file.write("\n")
    file.write(targetspousename)
    file.write("\n")
    file.write(targetspousename + LastName)
    file.write("\n")
    file.write(targetspousename + TargetYear)
    file.write("\n")
    file.write(targetspousename + targetmarrieddate)
    file.write("\n")
    file.write(targetspousename + LastName + targetmarrieddate)
    file.write("\n")
    file.write(targetkidname)
    file.write("\n")
    file.write(targetkidname + targetkidage)
    file.write("\n")
    file.write(targetkidage + targetkidname)
    file.write("\n")
    file.write(targetkidname + LastName)
    file.write("\n")
    file.write(targetkidname + LastName + targetkidage)
    file.write("\n")
    file.write(targetpetname)
    file.write("\n")
    file.write(targetpetname + targetpettype)
    file.write("\n")
    file.write(targetpetname + LastName)
    file.write("\n")
    file.write(targetpetname + targetpettype + LastName)
    file.close
    print("DONE! saved as: " + FirstName + "password.txt")

main()
