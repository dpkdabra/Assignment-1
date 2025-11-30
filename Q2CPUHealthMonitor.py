import psutil
import time

print("Monitoring CPU usage...")

while(True):
    
    try:
        usage = psutil.cpu_percent(1)
        
        if usage > 1:
            print("Alert! CPU usage exceeds threshold: " + str(usage) + "%")
            
    except:
        print("Error checking cpu")
        break