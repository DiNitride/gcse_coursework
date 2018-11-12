#Defines function
def gendata():
    
    #Imports required modules
    import random
    import string
    
    #Generates each letter of the number plate into separate variable
    numplate0=random.choice(string.ascii_letters)
    numplate1=random.choice(string.ascii_letters)
    numplate2=random.randrange(10)
    numplate3=random.randrange(10)
    numplate4=random.choice(string.ascii_letters)
    numplate5=random.choice(string.ascii_letters)
    numplate6=random.choice(string.ascii_letters)
    
    #Adds these variables together
    numplate=str(numplate0) +  str(numplate1) +  str(numplate2) +  str(numplate3) + " " + str(numplate4) + str(numplate5) + str(numplate6)

    #Writes the final variable to a file
    file=open("Registrationplatedata.txt",'w')
    file.write("{0}".format(numplate))
    file.close()
    
    #Generates random integer
    distance=random.randrange(20,100)
    #Writes to file
    file=open("Distance.txt",'w')
    file.write("{0}".format(distance))
    file.close()
    
    #Generates random integer
    time=random.randrange(1,10)
    #Writes to file
    file=open("Time.txt",'w')
    file.write("{0}".format(time))
    file.close()

    #Generates name and address
    surnames=["Smith","Johnson","Williams","Brown","Jones","Miller","Davis","Garcia","Rodriguez","Wilson","Martinez","Anderson","Taylor","Thomas","Hernandez","Moore","Martin","Jackson","Thompson","White","Lopez","Lee","Gonzalez","Harris","Clark","Lewis","Robinson","Walker","Perez","Hall","Young","Allen","Sanchez","Wright","King","Scott","Green","Baker","Adams","Nelson","Hill","Ramirez","Campbell","Mitchell","Roberts","Carter","Phillips","Evans","Turner","Torres","Parker","Collins","Edwards","Stewart","Flores","Morris"]
    forenames=["Tom","Syndicate","Tucker","Jericho","Sonja","Jordan","Dan","Phil","Tyler","Felix","Troye","Joe","Finn","Bellamy","Clarke","Raven","Lincon"]
    citys=["Leicester","Manchester","London","Birmingham","New York","York","Bath","Bradford","Bristol","Cambridge","Canterbury"]
    streets=["Small lane","Average sized lane","Large lane","Big lane","Notsobig lane","Lane","High street","Low Street","Medium Street","Party Street"]
    surname=surnames[random.randint(1,54)]
    forename=forenames[random.randint(1,13)]
    name=forename+" "+surname
    address=str(random.randint(1,200))+" "+streets[random.randint(1,9)]+", "+citys[random.randint(1,10)]

    #Adds different details together into one line
    details=numplate+":"+name+" "+address

    #Writes details to a file
    file=open("Details.txt",'a')
    file.write("{0}\n".format(details))

gendata()
