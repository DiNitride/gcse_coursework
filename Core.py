#import modules
import time

#Startup Message
print("CONSOLE:")
print("Number plate speeding system V2\n")

clear=input("Would you like to clear the data files? y/n: ")
if clear.split()[0]=="y":
    file=open("log.txt",'w')
    file.close
    file=open("Details.txt",'w')
    file.close
    file=open("SpeedingPlates.txt",'w')
    file.close

input("\nPress enter to continue...\n")

#Runs the process x amount of times
for x in range(5):
    #Defines function start
    def start():
        
        #Default variable setting
        CorrectFormat=False
        Write=False
        
        #Imports needed modules from separate file and runs module
        from Camera_AI import gendata
        gendata()
        
        #Opens file with registration plate data
        r=open("registrationplatedata.txt")
        #Reads data
        registration=r.read()
        #Validates it is the correct format
        if registration[0].isalpha() and registration[1].isalpha() and registration[2].isdigit() and registration[3].isdigit() and registration[5].isalpha() and registration[6].isalpha() and registration[7].isalpha():
            #Sets variables depending on outcome
            CorrectFormat=True
            Write=False
            
        #Opens files containing data
        #Reads data
        d=open("distance.txt")
        distance=int(d.read())
        t=open("time.txt")
        time=int(t.read())
        de=open("Details.txt")
        for li in de:
            if (li.split(":")[0].lower()==registration.lower()):
                details=str(li.split(":")[1])
        
        #Calculates final speed
        speed=distance/time
        
        #Checks if the car was over the speed limit
        if speed>30:
            #Sets variable Write to true, only for aesthetics
            Write=True
            #Opens file and writes data
            file=open("SpeedingPlates.txt",'a')
            file.write("{0}".format(registration+": "+details))
            file.close()

        #Checks if the registration was valid
        if CorrectFormat==False:
            #Sets variable Write to true, only for aesthetics
            Write=True
            #Opens file and writes data
            file=open("InvalidPlates.txt",'a')
            file.write("{0}\n".format(registration+": "+details))
            file.close()

        #Writes copy of console to file log.txt
        file=open("Log.txt",'a')
        file.write("Entry: {0}\n".format(x+1))
        file.write("Registration: {0}\n".format(registration))
        file.write("Valid Plate: {0}\n".format(CorrectFormat))
        file.write("Speed: {0}\n".format(speed))
        file.write("Write to file: {0}\n".format(Write))
        file.write("Details: {0}\n\n".format(details))
            
        #Prints the entry number, registration, speed and whether it writes to a file, for the console
        print("Entry:",x+1)
        print("Registration:",registration)
        print("Valid Plate:",CorrectFormat)
        print("Speed:",speed)
        print("Write to file:",Write)
        print("Details:",details)
        
    #Boots program        
    start()
