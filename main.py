import speedtest
import time
spe = speedtest.Speedtest()

print("Getting server information.......")
time.sleep(2)
while True : 
    print("1. Use Closest server")
    time.sleep(0.5)
    print("2. Use Best Server")
    b = int(input("Choose between the options (type the number) : "))
    time.sleep(1)
    if b == 1 : 
        print("Choosing the closest server......")
        close = spe.get_closest_servers()
        closest_host = close[0]["host"]
        closest = close[0]["name"]
        url = close[0]["url"]
        time.sleep(1)
        print(f"Found the closest server in {closest} by {closest_host}!")
        time.sleep(1)
        print("Setting Up......")
        time.sleep(1)
        break
    elif b == 2 : 
        print("Choosing the best server") 
        time.sleep(1)
        best = spe.get_best_server()
        bestest = best["country"]
        print("Choosing the best server for you..........")
        time.sleep(2)
        print(f"Found the best server in {bestest}!")
        time.sleep(1)
        break
    else : 
        print("Wrong Input Sir! Closing the program....")
        time.sleep(2)
        exit()
    
print("All set!")

while True : 
    print("Check - ")
    time.sleep(0.5)
    print("1. Download Speed")
    time.sleep(0.5)
    print("2. Upload Speed")
    time.sleep(0.5)
    print("3. Exit")
    time.sleep(1)
    a = int(input("Enter number of the option :\n"))
    time.sleep(1)
    if a == 1 : 
        print("Performing tasks. Wait for few minutes")
        kb = spe.download()
        mb = kb/1048576
        print(f"{mb} Mbps")
    elif a == 2 : 
        print("Performing tasks. Wait for few minutes")
        kb = spe.download()
        mb = kb/1048576
        print(f"{mb} Mbps")
    elif a == 3 : 
        print("Performing exit......")
        time.sleep(2)
        exit()
    else : 
        print("Wrong Input. Run the program again with the correct option number!")