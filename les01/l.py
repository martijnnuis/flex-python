import time
import sys

def slow_chat(text):
    for char in text:        
        sys.stdout.write(char) 
        sys.stdout.flush()    
        time.sleep(.1) 

slow_chat("Hello world\n")
slow_chat("Dit is de tweede regel\n") 
slow_chat("Silvan vertelt een verhaal")