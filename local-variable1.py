comment_out="Aggressive"  #this one was global variable

def commentfun():
    comment_out_1="ok"       #this one was a local vraible
    print("python is so "+comment_out_1)
    
    
commentfun()

#print('''python is'''+comment_out_1) this line provide an error due to local variable initiallize
print('''python is'''+comment_out)  # but this one the global variable