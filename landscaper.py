##############################
##    Variables - Game State 
##############################

game = {"tool": 0, "money": 0, "tip_this_time": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0, "own": 0, "tip_low": 0, "tip_high": 3},
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
    print(f"Landscape can use {tool['name']} to cut grass and make {tool['profit']}")
    game["money"] += tool['profit']
        
import random     
def random_tip():
    tool = tools[game["tool"]]
    game["tip_this_time"] = random.randint(tool['tiplow'], tool['tipmax'])
    game["money"] += tool['tip_this_time']
    
def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have {game['money']} and are using tool{game['tool']}")

    
    
