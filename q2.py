def convert_seconds(total_seconds):
    minutes= total_seconds//60
    rem_sec= total_seconds % 60
    return  f"{minutes}m {rem_sec}s"
    
sec= int(input("Enter Seconds:"))
if (sec>=0 and sec<=86400):
    ts = convert_seconds(sec)
    print("Total converted Seconds:",ts)
else:
    print("Exceeding seconds in a day...")
         
