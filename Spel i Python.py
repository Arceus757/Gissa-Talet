
__author__  = "Dmytro Malanchuk"
__version__ = "1.0.0"
__email__   = "dmytro.malanchuk@elev.ga.ntig.se"

#Gissning spel 
from colors import bcolors
import random
print(bcolors.BOLD + "========================================")
print("=== G I S S A   T A L E T    1 - 100 ===")
print("=========Du har 7 försök på dig=========\n")
def gissa_talet():
    rätt_svar = random.randint(1, 100)
    gissningar = 0
    while True:
        try:
            gissning = int(input(bcolors.CYAN + "==Gissa på ett tal mellan 1 och 100==:  "))
            gissningar += 1
            if gissning == rätt_svar:
                print(bcolors.GREEN + "\n G R A T T I S ! Du gissade rätt på", gissningar, "försök.")
                break
            if gissningar == 6:
                print(bcolors.RED + "\n Get out of here")
                break 
            elif gissning < rätt_svar:
                print(bcolors.RED + "För L Å G T! Försök igen.\n")
            else:
                print(bcolors.RED + "För H Ö G T! Försök igen.\n")

        except ValueError:
            print(bcolors.RED + "Ogiltig inmatning! Man får bara skriva i siffror")
            print(f"Du angav: {gissning} förra gången, fortsätt skriva i siffror pls")

gissa_talet()
print(bcolors.DEFAULT + "===============================================")