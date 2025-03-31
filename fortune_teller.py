#creating error class
class NotIncludedError(Exception):
    def __init__(self,value):
        self.value = value

# using tree nodes to play the old school paper fortune teller game

class Node:
    def __init__(self,value):
        self.value = value
        self.children = [ ]
   
    def add_child(self,child_node):
        self.children.append(child_node)

# building tree structure starting from smallest level/grandchildren/fortunes
fortune1 = Node("Good thing you don't get paid for thinkin'! ")
fortune2 = Node("Your girlfriend look like my mom!")
fortune3 = Node("Lebron James is your KING!!!")
fortune4 = Node("Your friends all think you're the best!")
fortune5 = Node("I see a hot, rich lifestyle in your future!")
fortune6 = Node("You be with J-Money servin' everybody!")
fortune7 = Node("No one wants to tell you.... but you stink.")
fortune8 = Node("Your mom is HOT!")
# node declarations for middle level/children/numbers
one = Node("1")
one.add_child(fortune1)
two = Node("2")
two.add_child(fortune2)
three = Node("3")
three.add_child(fortune3)
four = Node("4")
four.add_child(fortune4)
five = Node("5")
five.add_child(fortune5)
six = Node("6")
six.add_child(fortune6)
seven = Node("7")
seven.add_child(fortune7)
eight = Node("8")
eight.add_child(fortune8)
# node declatations for top level/parent/colors
pink = Node("pink")
pink.children = [eight,one]
purple = Node("purple")
purple.children = [two,three]
green = Node("green")
green.children = [four,five]
blue = Node("blue")
blue.children = [six,seven]
# root node
root = Node("Welcome")
root.children = [pink,purple,green,blue]


def odd_even(num):
    num = num % 2
    if (num == 0):
        return even_shuffle
    else:
        return odd_shuffle
  


odd_shuffle = [pink.children[0].value,purple.children[0].value,green.children[0].value,blue.children[0].value]
even_shuffle = [pink.children[1].value,purple.children[1].value,green.children[1].value,blue.children[1].value]

# # intro to game
print("\n✨Welcome to your future!✨ \n⚠️ Warning: These fortunes are a bit unhinged and have a tiktok brainrot theme. Have fun! ;)\n")
#listening first round of options
option = []
round1 = []
round2 = []
for child in root.children:
    option.append(child.value)
    print(f'* {child.value}')
# round 1 game
print(option)
while True:
    try:
        color = input("Please choose a color! ")
        if color in option:
            color=len(color)
            round1=odd_even(color)
            break
        
        else:
            raise NotIncludedError("Aht Aht! Please choose a color from the above options, try again!")
    except NotIncludedError as e:
        print(e)
        
    
# round 2 game
while True:
    round2 = str(input("Please choose a number! "))
    try:
        if round2 in round1:
            num = int(round2)
            round2= odd_even(num)
            print(round2)
            break
        else:
            raise NotIncludedError("😳 WOAH! Please choose a number from the above options, try again!")
    except NotIncludedError as e:
        print(e)
    
#dictionary for conversion into node
numbers = {"1": one, "2": two, "3": three, "4": four, "5": five, "6": six, "7": seven, "8": eight}

#round 3 game
while True:
    round3 = str(input("We are almost there! Pick one last number and your fortune will be revealed! 🔮🎱"))
    try:
        if round3  in round2:
             print(f"\nYour fortune is.... 🥁 \n 💫{numbers[round3].children[0].value}💫")
             break
        else:
            raise NotIncludedError("Aht Aht! Please choose a number from the above options, try again! :)")
    except NotIncludedError as e:
        print(e)




print("\nThank you for playing the ✨Fortune Teller✨! I hope your happy :)")






# code to traverse the tree and make sure nodes are properly linked
def print_tree(node, level=0):
    indent = "  " * level
    print(f'{indent} - {node.value}')
    for child in node.children:
        print_tree(child, level + 1)
        
# # print_tree(root)

