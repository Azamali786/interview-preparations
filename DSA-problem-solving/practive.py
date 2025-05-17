
## reversing a string ##

input_string = "abcdefghi"
"""
res = input_string[::-1]    ## slicing returns the reversed string

print(res)

"""

# in place reversal 


# left, right = 0, len(input_string)-1

# input_string = list(input_string)

# while left < right:
    
#     input_string[left], input_string[right] = input_string[right], input_string[left]
    
#     left += 1
#     right -= 1

# for i in range(0, right+1):
#     input_string[left], input_string[right] = input_string[right], input_string[left]
    
#     left += 1
#     right -= 1
    
# print("".join(input_string))


### Backward traversal ####

# res = ""

# for i in range(len(input_string)-1, -1, -1):  ## traver from index 8 (n-1) to 0
    
#     res += input_string[i]
    
# print(res)


##### palindrome 

stirng = "madam"

# rev_string = stirng[::-1]

# res = stirng == rev_string

# print(stirng)
# print(rev_string)
# print(res)

## check if half left is equal to half right

# def is_palindrome(string):
    
#     left, right = 0, len(stirng)-1

#     while left < right:
#         if stirng[left] != stirng[right]:
#             return False
#         left += 1
#         right -= 1
#         return True
    
# res = is_palindrome(stirng)
# print(res)

#### find duplicated in a string

# from collections import Counter

# input_string = "programming"

# freq = Counter(input_string)

# print(dict(freq))

########## finding the duplicatess #############
from collections import defaultdict
input_string = "test string"


# count = {}

# for i in range(len(input_string)):
#     if input_string[i] in count:
        
#         count[input_string[i]] += 1
        
#     else:
#         count[input_string[i]] = 1
        
# print(input_string)
# print(count)


# freqs = defaultdict(int)

# for i in range(len(input_string)):
#     freqs[input_string[i]] += 1
    
# print(input_string)
# print(dict(freqs))

############## check one is rotation of second one #############

# s1 = "abcde"
# s2 = "edcba"

# for i in range(len(s1)):
#     print(s1)
#     if s1 == s2:
#         print("yes")
#         break
#     s1 = s1[-1] + s1[:-1]


############################################################
""" 
create linked list object with head = None (so class inint will have head = None)
"""

# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList():
    
#     def __init__(self):
#         self.head = None
        
#     def insert_at_begining(self, data):
#         if self.head is None:
#             node = Node(data)
            

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the beginning
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head   # next will point to head
        self.head = new_node        # head will point to new node
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head       # point ned_node next to the only existing head
        self.head = new_node

    # # 2. Insert at the end
    # def insert_at_end(self, data):
    #     new_node = Node(data)
    #     if not self.head:
    #         self.head = new_node
    #         return
    #     last = self.head
    #     while last.next:
    #         last = last.next
    #     last.next = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # # 3. Delete a node by value
    def delete_node(self, key):
        
        # Start traversal from the head of the linked list
        temp = self.head
        
        # Case 1: Check if the node to delete is the head node
        if temp and temp.data == key:
            self.head = temp.next  # Update head to the next node
            temp = None            # Free memory of the deleted node (optional in Python)
            return                 # Exit after deletion

        # Case 2: Traverse the list to find the node to delete
        prev = None  # Pointer to keep track of the previous node
        while temp and temp.data != key:
            prev = temp       # Move 'prev' to current node
            temp = temp.next  # Move 'temp' to next node

        # Case 3: If the key wasn't found (temp reached end of list)
        if not temp:
            return  # Exit if key doesn't exist

        # Case 4: Unlink the node to delete
        prev.next = temp.next  # Bypass the target node
        temp = None            # Free memory (optional in Python)
        
        
    # 4. Search for a value
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def search_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # # 5. Get length
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # # 6. Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next    # save the next node before setting its link to pre
            current.next = prev     # link the current node next to pre node
            prev = current          # now move the pre node to current node and current_node to next node
            current = next_node
        self.head = prev    # as shoon as current_node is None set the pre to as Head node
        
    def reverse(self):
        current_node = self.head
        pre = None
        while current_node:
            next_node = current_node.next
            current_node.next = pre
            pre = current_node
            current_node = next_node
            
        self.head = pre

    # # 7. Print the list
    
    # def print_linkdlist(self):
    #     while self.head:
    #         print(self.head.data, end=" -> ")
    #         self.head = self.head.next
    #     print("None")
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example Usage
if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_end(5)
    llist.insert_at_end(10)
    llist.insert_at_end(20)
    # llist.insert_at_beginning(5)
    # llist.insert_at_begin(5)
    # llist.insert_at_end(30)
    
    print("Original List:")
    llist.print_list()  # Output: 5 -> 10 -> 20 -> 30 -> None
    
    # print("\nAfter deleting 20:")
    # llist.delete_node(20)
    # llist.print_list()  # Output: 5 -> 10 -> 30 -> None
    
    # print("\nIs 10 in the list?", llist.search(10))  # Output: True
    # print("Length:", llist.get_length())  # Output: 3
    
    # print("\nReversed List:")
    llist.reverse()
    llist.print_list()  # Output: 30 -> 10 -> 5 -> None
    
    
        
        


