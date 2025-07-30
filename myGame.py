print("Welcome to my first game!")

def askingName():
    name = input("What is your name? ").capitalize().strip()
    print(f"    Nice to meet you {name}😊 ")
    return name
    

def askingAge(userName):
    age = int(input(f"{userName}, what is your age "))

    calc = int(18 - age)
    
    if age >= 18:
        print(f"{userName} you are old enough to play👌")
        return True

    elif age < 18:
        print(f"\nOops {userName}😥, You are not old enough to play. \n In the next {calc} years you will be eligible to play👨‍🦱")
        return False


def doYou(userName):
    du = input("Do you want to play? (yes/no) ").lower()
    if "y" in du:
        print("You are starting with 10 hearts \n       💖💝💝💝💝💝💝💝💝💝 \n         LET'S PLAY🎉")
        game(userName)
    elif 'n' in du:
        print("Thanks for the attempt {userName} ")
    
        
        

def game(userName):
    question = input("\n         First choice ... Left or Right (left/right)? ").lower()
    
    if question == "right":
        print("             Oops You fell down and lost...😫")
        cont(userName)
        
    elif question == "left":
        acrossAround = input("Nice 👍, you follow the path and reach a lake... \n \n Do you swim across or go around (across/around)? ").lower()
        
        if  'ac' in acrossAround :
            print("You managed to get across 🙌, but were bitten by a fish and lost 5 healths \n            💖💖💖💖💖")
            riverHouse = input("\n You notice a house 🏡 and a river ⌨. \n   Which do you like to go to (river/house)? ")
            
            if riverHouse == "river":
                print("Oops 😫 \n You fell in the river and lost🤦‍♂️... ")
                cont(userName)
            elif riverHouse == "house":
                input("Its time to enter into the house 🚂 and have some fun💋💖✨ ")
                
        elif "ar" in acrossAround:
            print("Wise choice😏 \n      You met with an old friend of your's and he requessted to spend the night")
            print("             Have a nice sleepover with your pal😋")
            yes / n
def cont(userName):
    contd = input("\n        Do you wish to restart the game? (o) \n \n").lower()
    if contd == "yes":
        print(f"{userName}")
        game(userName)
    elif contd == "no":
        print("\n       Thanks for playing😍")
        
    
    
def run():
    userName = askingName()
    eligible = askingAge(userName)
    if eligible:
        doYou(userName)
       
        
run() 
            