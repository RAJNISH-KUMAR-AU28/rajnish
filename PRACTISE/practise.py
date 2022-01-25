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
   








####### wifi hacking code ######
'''

import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
input("")

'''

##### TREE CODE #########
'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self 
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent 
        return level         
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 10
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
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


# ####OUTPUT :-######################################### 
# electronics
#           |__laptop
#                     |__hp        
#                     |__thinkpad  
#                     |__All in One
#                     |__IOS       
#           |__mobile
#                     |__vivo      
#                     |__oppo      
#                     |__samsung   
#                     |__xiaomi    
#           |__tv
#                     |__LG        
#                     |__samsung
#                     |__Mi
#                     |__lenovo

'''
        

# from logging import root


# class TreeNode:
#     def __init__(self, data):
#         self.data = data 
#         self.child = []
#         self.parent =  None

#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)

# def build_product_tree():
#     root = TreeNode("CEO")

#     CTO=  TreeNode("CTO")
#     CTO.add_child(TreeNode("Vishwa(Infrastructure Head"))
#     CTO.add.child(TreeNode("Dhaval(cloud manager"))
#     CTO.add_child(TreeNode("Abhit(app manager"))

#     Gels = TreeNode("Gels HR Head")
#     Gels.add_child(TreeNode("peter(recuritment"))
#     Gels.add.child(TreeNode("waqas(policy manager"))
    
#     root.print.tree()

# if __name__ == "__main__":
#     build_product_tree    

    


# A = [8,5,6,3,9,8,3,9,1,8]
# A.sort
# print(A)
# print(sorted(A))



# #bubbl sort
# #  A = [4,3,2,1]

# # n = len(A)
# # for i in range(n):
# #     for j in range(n-1):
# #         if A[j]>A[j+1]:
# #             A[j],A[j+1] = A[j+1],A[j]

# # print(A)




# A = [8,5,6,3,9,8,3,9,1,8]
# B = []
# for i in range(len(A)):#step 4->go to step 1
#     min_ele = A[0]
#     min_ele_indx = 0
#     for indx in range(len(A)):#step 1->finding minimum element
#         if A[indx]<min_ele:
#             min_ele = A[indx]
#             min_ele_indx = indx
#     B.append(A[min_ele_indx])#step 2->put it in it's correct position
#     A.remove(A[min_ele_indx])#step 3-> remove from original list

# print(B)
# print(A)







# def merge(A,start_1, end_1,start_r, end_r):
#     p1 = start_1
#     p2 = start_r
#     c = []

#     while p1<=end_1 and p2<=end_r:
#         if A[p1]<A[p2]:
#             c.append(A[p1])
#             p1+=1
#         else:
#             c.append(A[p2])
#             p2+=1

#     while p1<=end_1:#2nd when elements are left in left side 
#         c.append(A[p1])
#         p1+=1
    
#     while p2<=end_r: #3rd when element are left in right side
#         c.append(A[p2])
#         p2+=1

#     idx = 0 
#     while idx<len(c): # A=c, creating a copy of c in A
#         A[start_1+idx] = c[idx]
#         idx+=1

# def merge_sort(A, low, high): # sort_list A from low to high
#     mid = (low+high)//2
#     if low==high:
#         return
#     merge_sort(A,low, mid )
#     merge_sort(A, mid+1, high)
#     merge(A, low, mid, mid+1, high) 
#     print(A)                          

# A = [8,5,6,3,9,8,3,9,1,8]
# merge_sort(A,0,len(A)-1)
# print(A)    






# def merge(A,B):
#     p1 = 0 
#     p2 = 0
#     m = len(A)
#     n = len(B)
#     c = []
    
#     while p1<m and p2<n:
#         if A[p1]<B[p2]:
#             c.append(A[p1])
#             p1+=1
#         else:
#             c.append(B[p2])
#             p2+=1
            
#     while p1<m:
#         c.append(A[p1])
#         p1+=1
    
#     while p2<n:
#         c.append(B[p2])
#         p2+=1
#     return            
        
# if __name__=="__main__":
    
#     A = [1,2,3,0,0,0] #(n/2)
#     B = [2,5,6]       #(n/2)
#     res = merge(A,B)
#     print(res)



# # merge sorted arrays :
# def mergeSortedArrays(arr1, arr2):
#     i = 0
#     j = 0

#     len1 = len(arr1)
#     len2 = len(arr2)
#     newarray = []

#     while((i<len1) and (j<len2)):
#         if(arr1)[i] < (arr2)[j]:
#             newarray.append(arr1[i])
#             i = i +1
#         else:
#             newarray.append(arr2[j])
#             j = j + 1 
#     while(i < len1):
#         newarray.append(arr1[i])
#         i = i + 1 
#     while(j < len2):
#         newarray.append(arr2[j])
#         j = j + 1
#     return newarray                 


# arr1 = [1,2,3,0,0,0]
# arr2 = [2,5,6]
# newarray = mergeSortedArrays(arr1, arr2)
# print(newarray)








###############################reverse string ,,,,but incomplte code not

# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         left = 0
#         right = len(s)-1
#         while left < right:
#             hold = s[left]
#             s[left] = s[right]
#             s[right] = hold
#             left +=1
#             right -=1
            
# s = ["h","e","l","l",9]  
    


##### TWO SUM TARGET #######

# def twosums(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if target - nums[i] == nums[j]:
#                 return [i,j]
#     return None       
            
# test = [2,7,11,15]
# target = 9

# print(twosums(test,target))
    

    
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



####### WIFI PASSWORD #######################
# import subprocess
# data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
# for i in profiles:
#     results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     try:
#         print ("{:<30}|  {:<}".format(i, results[0]))
#     except IndexError:
#         print ("{:<30}|  {:<}".format(i, ""))
# input("")
 










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
   


##### TREE CODE #########
'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self 
        self.children.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent 
        return level         
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 10
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
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

# ####OUTPUT :-######################################### 
# electronics
#           |__laptop
#                     |__hp        
#                     |__thinkpad  
#                     |__All in One
#                     |__IOS       
#           |__mobile
#                     |__vivo      
#                     |__oppo      
#                     |__samsung   
#                     |__xiaomi    
#           |__tv
#                     |__LG        
#                     |__samsung
#                     |__Mi
#                     |__lenovo
'''
        




# class TreeNode:
#     def __init__(self, data):
#         self.data = data 
#         self.children = []
#         self.parent =  None

#     def get_level(self):
#         level = 0 
#         p = self.parent
#         while p :
#             level += 1
#             p = p.parent 
#         return level

#     def print_tree(self):
#         spaces = ' ' * self.get_level()
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()

#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)

# def build_product_tree():
#     root = TreeNode("Nilupul  (CEO)")

#     CTO =  TreeNode("Chinmay  (CTO)")
#     CTO.add_child(TreeNode("Vishwa  (Infrastructure Head)"))
#     CTO.add_child(TreeNode("Dhaval  (cloud manager)"))
#     CTO.add_child(TreeNode("Abhijit  (App manager)"))
#     CTO.add_child(TreeNode("Aamir  (Application head)"))

#     Gels = TreeNode("Gels  (Hr Head)")
#     Gels.add_child(TreeNode("peter  (recuritment)"))
#     Gels.add_child(TreeNode("waqas  (policy manager)"))
    
#     root.add_child(CTO)
#     root.add_child(Gels)

#     root.print_tree()

# if __name__ == "__main__":
#     build_product_tree()  


'''

class TreeNOde:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self 
        self.children.append(child)

    

    def get_level(self):
        level = 0 
        p = self.parent
        while p :
            level += 1
            p = p.parent 
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "$__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()



def build_product_tree():
    root = TreeNOde("Dhirubhai ambani")

    Anil_ambani = TreeNOde("Anil ambani")
    Anil_ambani.add_child(TreeNOde("Shyam"))
    Anil_ambani.add_child(TreeNOde("Sahil"))
    Anil_ambani.add_child(TreeNOde("SOhan"))

    Mukesh_ambani = TreeNOde("Mukesh ambani")
    Mukesh_ambani.add_child(TreeNOde("Rajesh"))
    Mukesh_ambani.add_child(TreeNOde("Rahul"))
    Mukesh_ambani.add_child(TreeNOde("Rohan"))


    root.add_child(Anil_ambani)
    root.add_child(Mukesh_ambani)
   
    root.print_tree()

if __name__ == "__main__":
    build_product_tree()

## OUTPUT######

Dhirubhai ambani
    $__Anil ambani
        $__Shyam
        $__Sahil
        $__SOhan
    $__Mukesh ambani
        $__Rajesh
        $__Rahul
        $__Rohan
'''






'''

class Node : 

    def __init__(self,data) :
        self.data = data
        self.next = None

    def printlist(head):
        cur = head
        while cur != None :
            print(cur.data)
            cur = cur.next


def merge(head1, head2):

    p1 = head1
    p2 = head2

    head3 = None
    cur = None

    while p1 != None and p2 != None :
        if p1.data < p2.data :
            if head3 == None :
                head3 = Node(p1.data)
                cur = head3
            else:
                cur.next = Node(p1.data)
                cur =  cur.next
            p1 = p1.data
        else:
            if head3 is None :
                head3 = Node(p2.data) 
                cur   = head3
            else:
                cur.next = Node(p2.data)
                cur = head3
            p2 = p2.data
    while p1 != None :
        cur.next = Node(p1.data)
        cur = cur.next
        p1 = p1.data
    
    while p2 != None :
        cur.next = Node(p2.data)                     
        cur = cur.next
        p2 = p2.data
    
    return head3

head1 = Node(5)
head1.next = Node(6)
head1.next.next = Node(7)
head1.next.next.next = Node(8)
head1.next.next.next.next = Node(9)

head2 = Node(15)
head2.next = Node(16)
head2.next.next = Node(17)
head2.next.next.next = Node(18)
head2.next.next.next.next = Node(19)

ans = merge(head1, head2)
print(ans)
print()

'''

        