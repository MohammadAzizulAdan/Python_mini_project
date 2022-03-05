def integer_validation(value):
    try:
        return int(value)
    except ValueError:
        return -1;


progressionOutcome = []
passValue = []
deferValue = []
failValue = []

wantToView = "y";
Progress = 0
Trailer = 0
Retriever = 0
Excluded = 0
while wantToView=="y" or wantToView=="Y":
    #variables for storing credit at pass,defer,fail
    creditsAtPass=input("Please enter your credits at pass: ")
    creditsAtPass=integer_validation(creditsAtPass)
    
    #integer_validation
    if(creditsAtPass==-1):
        print("Integer required.")
        continue
    
    
    #out of range validation
    if(creditsAtPass>120):
        print("Out of range.")
        continue
    
    
    creditsAtDefer=input("Please enter your credits at defer: ")
    creditsAtDefer=integer_validation(creditsAtDefer)
    
    #integer_validation
    if(creditsAtDefer==-1):
        print("Integer required.")
        continue;
    
    #out of range validation
    if(creditsAtDefer>120):
        print("Out of range.")
        continue
    
    creditsAtFail=input("Please enter your credits at fail: ")
    creditsAtFail=integer_validation(creditsAtFail)
    
    #integer_validation
    if(creditsAtFail==-1):
        print("Integer required.")
        continue;
    
    #out of range validation
    if(creditsAtFail>120):
        print("Out of range.")
        continue
    
    total = creditsAtPass + creditsAtDefer + creditsAtFail;
    
    #Incorrect total validation
    if total !=120:
        print("Total incorrect.")
        continue
    
    if(creditsAtPass == 120):
        print("Progress.")
        Progress+=1
        progressionOutcome.append("Progress")
        passValue.append(creditsAtPass)
        failValue.append(creditsAtFail)
        deferValue.append(creditsAtDefer)
    elif(creditsAtPass == 100):
        print("Progress(module trailer).")
        Trailer+=1
        progressionOutcome.append("Progress(module trailer)")
        passValue.append(creditsAtPass)
        failValue.append(creditsAtFail)
        deferValue.append(creditsAtDefer)
    elif(creditsAtFail>=80):
        print("Exclude.")
        Excluded+=1
        progressionOutcome.append("Exclude")
        passValue.append(creditsAtPass)
        failValue.append(creditsAtFail)
        deferValue.append(creditsAtDefer)
    else:
        print("Module retriever.")
        Retriever+=1
        progressionOutcome.append("Module retriever")
        passValue.append(creditsAtPass)
        failValue.append(creditsAtFail)
        deferValue.append(creditsAtDefer)
    
    wantToView=input("Please enter 'y' if you want to veiw resuts or any other key if you want to quit :")
    

print("===========================================================")
print("Horizontal Histogram")
print(f'"Progress" {Progress}  : '+ "*"*Progress)
print(f'"Trailer" {Trailer}   : '+ "*"*Trailer)
print(f'"Retriever" {Retriever} : '+ "*"*Retriever)
print(f'"Excluded" {Excluded}  : '+ "*"*Excluded)
print("===========================================================")

print()
print("Vertical Histogram")
print("Progress Trailing Retriever Excluded")
maximumCount=max(Progress,Trailer,Retriever,Excluded)
count =0
while count<maximumCount:
    if Progress>0:
        print("   *   ",end="")
        Progress-=1
    else:
        print("       ",end="")
    
    if Trailer>0:
        print("     *    ",end="")
        Trailer-=1
    else:
        print("          ",end="")
    if Retriever>0:
        print("     *    ",end="")
        Retriever-=1
    else:
        print("          ",end="")
    if Excluded>0:
        print("    *   ")
        Excluded-=1
    else:
        print("        ")
    count+=1

print()
count=len(progressionOutcome)
index=0
while index<count:
    print(f'{progressionOutcome[index]} - {passValue[index]}, {deferValue[index]}, {failValue[index]}')
    index+=1

    

    





