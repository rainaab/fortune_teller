import random

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
root = Node("Start")
root.children = [pink,purple,green,blue]

# code to traverse the tree and make sure nodes are properly linked
def print_tree(node, level=0):
    indent = "  " * level
    print(f'{indent} - {node.value}')
    for child in node.children:
        print_tree(child, level + 1)

# print("Welcome to your future! Warning: These fortunes are a bit unhinged and have a tiktok brainrot theme. have fun! ;)")

# color = input("Please choose a color! ")

print_tree(root)