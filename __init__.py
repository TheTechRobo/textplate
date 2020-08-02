#This is completely untested!!! Made with github online no test.

#See credits in readme.md

class Enemies:
    class Example:
        name = "Example"
        desc = "Example is a giant with red skin, likely sunburned.\nThere are rumors that he is very very very strong, but it is unknown if he is friendly."
        attackDamage = (10,20)
        health = 55

class Shell:
    attack_msg = "%(heSheIt)s %(methodOfAttack)s %(entityName)s, dealing %(damageCount)i damage."
    playerWin = "%(entityName)s dies and collapses on the ground in front of you. You have %(health)i health remaining."
    enemyWin = "You die and collapse on the ground. %(entityName)s %(verb)s triumphantly. They had %(health)i health remaining."
class Functions:
    pass

class Player:
    class Info:
        health = 50
        inventory = []
        attackStrength = (5,15)

class Program:
    class Metadata:
        version = "0.0 (Original Shell) build XXXXXXXX" #tip: for the build put the git commit hash or the svn revision number
        welcomeMsg = "Hello and welcome to Example version %s! We hope you have a great experience." % self.version
    def Start(debug=False):
        pass

if __name__ == "__main__":
    Program.Start()
