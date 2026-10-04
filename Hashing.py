import hashlib

def hashing():
    
    print("\n Welocme to Hashing")
    
    real_pass = "Munish"
    
    real_pass_hash = hashlib.sha256(real_pass.encode()).hexdigest()
    
    user_input = input("\nEnter Password:")
    
    user_hash = hashlib.sha256(user_input.encode()).hexdigest()
    
    print("\nThe Hashed Password is:", user_hash)
    
    if real_pass_hash == user_hash:
        print("\nAccess Granted!")
        
    else:
        print("\nWrong Password!")
    
    return 
hashing()    