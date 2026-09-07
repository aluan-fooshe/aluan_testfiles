#https://mythgyaan.com/doctor-strange-quotes-dialogues/#:~:text=15%20Thought-Provoking%20Doctor%20Strange%20Quotes%20%26%20Dialogues%201,15%20I%20can%20lose%20again%20and%20again%2C%20forever.
def main():
    x = int(input())
    if x == 0:
        print("Strange: Dormmanu I've come to bargain.")
    while x <= 1:
            print("         Dormmanu I've come to bargain.")
            x = x+2
    while x == 2:
        print("Dormmanu I've come to bargain.")
    while x == 3:
        print("Strange: I can lose again and again, forever.")
        x = x+1
    while x == 4:
        print("Wong: Choose your weapon wisely.")
        x = x-1
    while x == 5:
        print("Karl Mordo: Forget everything that you think you know.")
        break
    else:
        print("Who are you in this vast multiverse, Mr. Strange?")
main()