#This is completely untested!!! Made with github online no test. (Actually, scratch that.)

#See credits in readme.md

class Enemies:
    class Example:
        name = "Example"
        desc = "Example is a giant with red skin, likely sunburned.\nThere are rumors that he is very very very strong, but it is unknown if he is friendly."
        attackDamage = (10,20)
        health = 55

class Messages:
    attack = "%(heSheIt)s %(methodOfAttack)s %(entityName)s, dealing %(damageCount)i damage."
    playerWin = "%(entityName)s dies and collapses on the ground in front of you. You have %(health)i health remaining."
    enemyWin = "You die and collapse on the ground. %(entityName)s %(verb)s triumphantly. They had %(health)i health remaining."
    gameOver = "- GAME OVER -\nThanks for playing!"
    versionMsg = "0.0 (Original Shell) build XXXXXXXX" #tip: for the build put the git commit hash or the svn revision number
    welcomeMsg = "Hello and welcome to Example version %s! We hope you have a great experience." % versionMsg

class Functions:
    def random(range):
        a, b = range
        import random
        return random.randint(a, b)
    def askYesNo(question):
        answer = input("%s [y/n]")

class Rooms:
    class StartingRoom:
        commands = ["attack", "quit"]

class Player:
    class Info:
        health = 50
        inventory = []
        attackStrength = (5,15)

class Program:
    class Metadata:
        version = 0.0
        createdBy = "TheTechRobo"
        url = "https://github.com/thetechrobo/textplate"
    def __init__(self, debug=False):
        def debugLog(msg):
            if debug:
                print("DEBUG: %s" % msg)
        print(Messages.welcomeMsg)
        from theGame import i
        i(Enemies, Messages, Functions, Rooms, Player, Program, debugLog)
        del i
        import theGame
        theGame.theGame(debug)
        print(Messages.gameOver)

if __name__ == "__main__":
    Program()
