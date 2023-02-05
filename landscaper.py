##############################
##    Variables - Game State 
##############################

game = {"tool": 0, "money": 0, "tip_this_time": 0, "highest_purchase_option":0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0, "tool_count": 1, "tip_low": 0, "tip_high": 2},
    {"name": "rusty scissors", "profit": 5, "cost": 5, "tool_count": 0, "tip_low": 0, "tip_high": 6},
    {"name": "old-timey lawn mower", "profit": 50, "cost": 25, "tool_count": 0, "tip_low": 0, "tip_high": 15},    
    {"name": "battery powered lawn mower", "profit": 100, "cost": 250, "tool_count": 0, "tip_low": 0, "tip_high": 25},
    {"name": "team", "profit": 250, "cost": 500, "tool_count": 0, "tip_low": 0, "tip_high": 100}
]

user_reply_purchase = ""

##############################
## Game Option Functions 
##############################

def cut_grass():
    money = 0
    work_tips = 0
    tips = 0   
    
    ## if game tool > 0, don't count teeth - otherwise count it. 
    i = 0  
    if (game['tool'] > 0):
        i = 1
    
    while (i < len(tools)):
        if (tools[i]['tool_count'] > 0):
            money = money + (tools[i]['tool_count'] * tools[i]['profit'])
            tips = tips + random_tip(tools[i]['tip_low'], tools[i]['tip_high'])
        i += 1
                  
    print(f"Landscaper uses tools to cut grass and make profit of ${money} and tips of ${tips} for total of ${money + tips}.")
    game["tip_this_time"] = tips
    game["money"] += money + tips
        
import random     
def random_tip(low, high):
    work_tip = 0
    if (random.randint(0,1) > 0):
        work_tip = random.randint(low, high)
        return work_tip
    return 0
    
def check_stats():
    print(" ") 
    print(f"You currently have ${game['money']} and the following tools:")
    print(f"  {tools[1]['tool_count']} - {tools[1]['name']}")      
    print(f"  {tools[2]['tool_count']} - {tools[2]['name']}")  
    print(f"  {tools[3]['tool_count']} - {tools[3]['name']}") 
    print(f"  {tools[4]['tool_count']} - {tools[4]['name']}") 
    print(" ")  
    
def upgrade():
    while (True):
        if (tools[1]['cost'] > game['money']):
            print(" ")
            print(f"Not enough money to buy a tool.  Money you have is: ${game['money']}. Money needed for tool: '{tools[1]['name']}' is ${tools[1]['cost']}.")
            return 0
        else:     
            user_reply_purchase = input(build_upgrade_msg())
        
        if (len(user_reply_purchase) == 0):
            print("No purchase Option Selected.")
            return 0
        
        if (user_reply_purchase == "N" or user_reply_purchase == "n"):
            print("No purchase made.")
            return 0    
               
        if (user_reply_purchase.isnumeric() == True and int(user_reply_purchase) <= len(tools)):
            user_reply_purchase = int(user_reply_purchase)
            if (user_reply_purchase > game['highest_purchase_option']):
                print(f"Invalid Purchase Option Input: {user_reply_purchase}.") 
                return 0  
            else:               
                game["money"] -= tools[user_reply_purchase]["cost"]
                tools[user_reply_purchase]["tool_count"] += 1
                print(f"Purchased tool: {tools[user_reply_purchase]['name']} for ${tools[user_reply_purchase]['cost']}.  Money left: ${game['money']}")
                if (user_reply_purchase > game['tool']):
                    game['tool'] = user_reply_purchase
                return 0   
        else:
            print(f"Invalid Purchase Option Input: {user_reply_purchase}.") 
            return 0           

def build_upgrade_msg():    
    print(f"Money available: ${game['money']}. Purchase options below:")
    tool_name = ""
    tool_cost = ""
    i = 1
    while (i <= (game['tool'] + 1)): 
        tool_name = tools[i]['name']
        tool_cost = tools[i]['cost']
        if (game['money'] >= tool_cost):
            print(f"  [{i}] Buy {tool_name} for ${tool_cost}") 
            game['highest_purchase_option'] = i
        i += 1 
                  
    print("  [N] No purchase") 
            
    return ("Select option ==> ")
    
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
            game["highest_purchase_option"] = 0
            print(" ")
            print("Game Reset")
        else:
            print(" ")
            print ("Reset response not equal to 'Y' or 'y'. Reset not completed.")

while (True):
    print (" ")   
    reply_processed = False     
    user_reply = input("[1] Cut Grass [2] Check Stats [3] Upgrade [4] Reset Game [Q] Quit ==> ")
    
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
   
    if (user_reply == "Q" or user_reply == "q"):
        print ("You quit the game 😢 😢 😢  Come back again.")
        print(" ")
        reply_processed = True
        break 
   
    if (reply_processed == False):
        print ("Invalid choice. Try again.") 
       
    if (win_check() == True):
        break