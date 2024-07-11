pr=int(input("enter your pr :"))
if(pr>70 and pr<=100): 
    print ("you are pass with first division ")
elif(pr>50 and pr<=70): 
    print ("you are pass with second division ")
elif(pr>30 and pr<=50): 
    print ("you are pass with third division ")
elif(pr>=0 and pr<=30): 
    print ("you are failed ")
else:
    print("please enter your percentage in the range of 0 to 100 ")


