import random 
names_list = ["joe schmoe", "doug", "timmy", "timothy", "Eggward", "Garry", "Gwood", "Frederick Faz", "Chuckles", "Kludzy", "Larry", "" ]
for name in names_list :
    

    current_hp = random.randint(0, 100)
    if current_hp is 0:
        status = "dead"
    else:
        status = "alive"
    
    clutz = random.randint(1,2)
    clumsy = (clutz == 2) 
    speed = random.randint(0, 100)
    print(f"Name: {name}, Status: {status}, Speed : {speed}, Clumsy : {clumsy}, health: {current_hp}, ")