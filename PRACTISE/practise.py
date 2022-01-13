# f = open('test.txt', 'r')
# f.write("hello we are happy to glad yopu to inform you that you are seleted ")
# f.close()


# with open('test.txt', 'w' ) as f :
#     a = f.write("hellow  fgd")
#     if 
# print(a)




# changing another highscore
# def game():
#     return 64


# score =  game()

# with open("hiscore.txt")as f :
#     hiscore = int(f.read())
    
# if hiscore < score :
#     with open("hiscore.txt", "w") as f :
#         f. write(str(score))



# create a multiplication table from 2 to 20:
# for i in range(2 ,21):
#     with open(f"tables/multiplication_of_{i}", "w") as f:
#         for j in range(1, 11):
#             f.write(f"{i}X{j}={i*j}")
#     break



# # replace word by with open:

# with open("replace.txt") as f :
#     content = f.read()

# content = content.replace("hero", "$#%#$@" )

# with open("replace.txt", "w") as f :
#     content = f.write(content)




# # to check content is present in file or not by the ("with open") 
# #--->>
# content = True
# i = 1 # for checking for multiple time content in different lines:
# with open("log.txt") as  f :
#     while content:
#         content = f.readline()
#         if 'rajnish' in content.lower():
#             print(content)
#             print(f"yes it's present \n{i}" )
#         i+= 1 # for checking for multiple time content in different lines:
   


##### TREE #########

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self 
        self.children.append(child)
    
    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()
        
def build_product_tree():
    root = TreeNode("electronics")
    
    laptop =  TreeNode("laptop")
    laptop.add_child(TreeNode("hp"))
    laptop.add_child(TreeNode("thinkpad"))
    laptop.add_child(TreeNode("All in One"))
    laptop.add_child(TreeNode("IOS"))
    
    mobile = TreeNode("mobile")
    mobile.add_child(TreeNode("vivo"))
    mobile.add_child(TreeNode("oppo"))
    mobile.add_child(TreeNode("samsung"))
    mobile.add_child(TreeNode("xiaomi"))

    tv = TreeNode("tv")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("samsung"))
    tv.add_child(TreeNode("Mi"))
    tv.add_child(TreeNode("lenovo"))


    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    root.print_tree()

if __name__ == "__main__":
    build_product_tree()




        






        