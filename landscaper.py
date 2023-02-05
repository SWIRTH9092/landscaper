##############################
##    Variables - Game State 
##############################

game = {"tool": 0, "money": 0, "tip_this_time": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0, "own": 0, "tip_low": 0, "tip_high": 2},
    {"name": "rusty scissors", "profit": 5, "cost": 5, "own": 0, "tip_low": 0, "tip_high": 6},
    {"name": "old-timey lawn mower", "profit": 50, "cost": 25, "own": 0, "tip_low": 0, "tip_high": 15},    
    {"name": "battery powered lawn mower", "profit": 100, "cost": 250, "own": 0, "tip_low": 0, "tip_high": 25},
    {"name": "team", "profit": 250, "cost": 500, "own": 0, "tip_low": 0, "tip_high": 100}
]

##############################
## Game Option Functions 
##############################

def cut_grass():
    tool = tools[game["tool"]]
    print(f"Landscape can use {tool['name']} to cut grass and make ${tool['profit']}.")
    random_tip(tool['tip_low'],tool['tip_high'])
    game["money"] += tool['profit']
        
import random     
def random_tip(low, high):
    if (random.randint(0,1) > 0):
        game["tip_this_time"] = random.randint(low, high)
        if (game["tip_this_time"] > 0):
            game["money"] += game['tip_this_time']
            print (f"Your hard work paid off.  You earned a tip of: ${game['tip_this_time']}.")   
    
def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have ${game['money']} and are using the tool: {tool['name']}.")

def upgrade():
    if (game["tool"] >= len(tools)):
        print ("no more upgrades avaialable.")
    
    next_tool = tools[game["tool"] + 1 ]
    
    if(next_tool == None):
        print("There is no more tools")
        return 0   ## kill the function
    if(game["money"] < next_tool["cost"]):   
        print(f"Not enough money to buy tool.  Money have: ${game['money']}. Money needed: ${next_tool['cost']}.")  
        return 0 
    game["money"] -= next_tool["cost"]
    print(f"You bought: {next_tool['name']}.  Money you have now: ${game['money']}.")  
    game["tool"] += 1
    
def win_check():
    if (game["tool"] == 4 and game["money"] > 999):
        print(" ")
        print("👏 👏 👏 You Win  👏 👏 👏")
        print(" ")
        return True
    return False

def reset_game():
        user_check = input("Do you want to reset game? Y or N ==> ")
        if (user_check == 'Y' or user_check =='y'):
            game["tool"] = 0
            game["money"] = 0
            game["tip_this_time"] = 0
            print(" ")
            print("Game Reset")
        else:
            print(" ")
            print ("Reset response not equal to 'Y' or 'y'. Reset not completed.")

while (True):
    print (" ")   
    reply_processed = False     
    user_reply = input("[1] Cut Grass [2] Check Stats [3] Upgrade [4] Reset Game [5] Quit ==> ")
    
    if (len(user_reply) == 0):
        print("No option selected.  Try again.")
        reply_processed = True
               
    if (user_reply == "1"):
        cut_grass()
        reply_processed = True
       
    if (user_reply == "2"):
        check_stats()
        reply_processed = True
       
    if (user_reply == "3"):
        upgrade()  
        reply_processed = True
         
    if (user_reply == "4"):
        reset_game() 
        reply_processed = True
   
    if (user_reply == "5"):
        print ("You quit the game 😢 😢 😢  Come back again.")
        print(" ")
        reply_processed = True
        break 
   
    if (reply_processed == False):
        print ("invalid choice") 
       
    if (win_check() == True):
        break