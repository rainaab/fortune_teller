# using tree nodes to play the old school paper fortune teller game

class Node:
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

# building tree structure starting from smallest level/grandchildren/fortunes
fortune1 = Node("Good thing you don't get paid for thinkin'! ", None, None)
fortune2 = Node("Your girlfriend look like my mom!", None, None)
fortune3 = Node("Lebron James is your KING!!!", None, None)
fortune4 = Node("Your friends all think you're the best!", None, None)
fortune5 = Node("I see a hot, rich lifestyle in your future!", None, None)
fortune6 = Node("You be with J-Money servin' everybody!", None, None)
fortune7 = Node("No one wants to tell you.... but you stink.", None, None)
fortune8 = Node("Your mom is HOT!", None, None)
# node declarations for middle level/children/numbers
one = Node(1,None, fortune1)
two = Node(2,fortune2, None)
three = Node(3, None ,fortune3)
four = Node(4,fortune4,None)
five = Node(5,fortune5,None)
six = Node(6,None, fortune6)
seven = Node(7,fortune7, None)
eight = Node(8,None, fortune8)
# node declatations for top level/parent/colors
pink = Node("pink", eight, one)
purple = Node("purple", two, three)
green = Node("green", four, five)
blue = Node("blue", six, seven)

# code to traverse the tree and make sure nodes are properly linked
def traversePreOrder(node):
    if Node is None:
        return
    print(node.value, end=" "),
    if node.left != None:
        traversePreOrder(node.left)
    if node.right !=None:
        traversePreOrder(node.right)
