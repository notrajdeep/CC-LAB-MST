import string    
import random  
S = 10 
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
print("The randomly generated string is : " + str(ran)) 
