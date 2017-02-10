#def decrypt():
    #a=raw_input("Give me the word to decrypt:")
    #number=input("What was it shifted by?")
    #b=list(a)
    #str(b)
    #c=[ord(x)for x in(b)]
    #d=[]
    #for i in c:
   #     d.append(i-number)
  #  e=[chr(i) for i in (d)]
 #   e="".join(e)
#    print "Decryption Successful, your word is",e,"!"

def encrypt():
    a=raw_input("Give me a word:")
    number=input("Give me a number:")
    b=list(a)
    str(b)
    c=[ord(x)for x in(b)]
    d=[]
    for i in c:
        d.append(i+number)
    e=[chr(i) for i in (d)]
    e="".join(e)
    print "Your Caesar shifted result (ascii code) is:",e,"!"
    print "Your key is", number, ",remember that!"

def menu():
    print "\n\n\nWelcome to the Caesar Shifter."
    print "What would you like to do?"
    print "Option 1:Encrypt Word"
    print "Option 2:Decrypt Word"
    print "If you would like to quit, press 0."
    choice=input("Pick your selection:")
    if choice==1:
        run=encrypt()
        run
        menu()
    elif choice==2:
        derun=decrypt()
        derun
        menu()
    elif choice==0:
        quit
    else:
        print"That is not a correct selection, please pick either 1, or 2."

menu()