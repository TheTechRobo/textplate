#This is completely untested!!! Made with github online no test. (Actually, scratch that.)

#See credits in readme.md

import random

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
    versionMsg = "0.0 (Original Shell) build XXXXXXXX" #tip: for the build put the git commit hash or the svn revision number, only if you want though
    welcomeMsg = "Hello and welcome to Example version %s! We hope you have a great experience." % versionMsg
    cheater = "Detected cheating."

class Functions:
    def random(range):
        """
        Usage:
        >>> random((firstNumber, secondNumber))
        Returns the result.
        """
        a, b = range
        return random.randint(a, b)
    def ask(question):
        """
        Usage:
        >>> if ask("question"):
        ...    print("The player said yes.")
        ... else:
        ...    print("The player said no.")
        """
        answer = input(question + " [y/n]")
        return answer[0].lower() == "y"

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
        from theGame import theGame
        theGame(Enemies, Messages, Functions, Rooms, Player, Program, debugLog, debug)
        print(Messages.gameOver)

if __name__ == "__main__":
    Program()
