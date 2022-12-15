

print("Welcome to the secret auction program.")

players=[]   #creating a list to store the dictionaries containing player and bid

play='yes'
while play=="yes":
    names = input("What is your name?\n")  #gets name
    bids = input("What's your bid?\n")  #gets bid
    def auction(name,bid):     #function to add name and bid to as dictionary to players list
        players.append({"name":name,"bid":bid})
    auction(names,bids)
    play=input("Are there any other bidders?\n")


win=""   #to store winner
max=0    #to store highest bid
for i in range(0,len(players)):
    if int(players[i]["bid"])>max:
        max=int(players[i]["bid"])    #checks for highest bid
        win=players[i]["name"]        #stores the winner



print(f"The winner is {win} with a bid of {max}")









