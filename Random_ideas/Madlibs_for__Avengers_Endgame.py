#https://script-pdf.s3-us-west-2.amazonaws.com/avengers-endgame-script-pdf.pdf
#https://script-pdf.s3-us-west-2.amazonaws.com/avengers-endgame-script-pdf.pdf
class Whatever:
    def __init__(self):
        self.curse_word = ''
        self.weekday = ''
        self.verb_ing = ''
        self.country = ''
        self.character1 = ''
        self.your_name = ''
        self.adjective = ''


    def __str__(self):
        return (f'SAM WILSON: What the {self.curse_word} is this?' \
               f'\nTONY: {self.weekday}, what are they {self.verb_ing} at?'
               f'\n{self.weekday}: Something just entered the {self.country}.'
               f'\n{self.character1}: I am {self.character1}.'
               f'\nROCKET: Just wait for it.'
               f'\nROCKET: Oh, yeah!'
               f'\n{self.your_name}! We are gonna need a {self.country} here!!!'
               f'\n{self.your_name}: Rogers... Rogers...'
               f'\n*5 MINUTES LATER*'
               f'\nTHANOS: I am... {self.adjective}. *SNAPS*'
               f'\n{self.your_name}: And I... am {self.your_name}!!!')

new_script = Whatever()
new_script.curse_word = str(input("Enter curse word:"))
new_script.weekday = str(input("Enter weekday:"))
new_script.verb_ing = str(input("Enter a word that ends with ___ing:"))
new_script.country = str(input("Enter a name of a country:"))
new_script.character1 = str(input("Enter a name of a character:"))
new_script.your_name = str(input("Enter your name:"))
new_script.adjective = str(input("Enter an adjective:"))

print(f'\n{new_script}')

#bitch
#thursday
#shitting
#Norway
#Harry Potter
#Cristin
#pretty