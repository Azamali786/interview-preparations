

# # closure implementation

# def outer_func(msg):
    
#     message = msg
    
#     def inner_function():
#         print(message)
        
#     return inner_function


# resultant_func = outer_func("Hello from ourter function")

# # call inner function
# resultant_func()

# def outer_func(msg):
#     message = msg
    
#     def inner_func():
#         print(message)
        
#     return inner_func

# def power_factory(exponent):
    
#     def power(base):
#         return base**exponent

#     return power

# square = power_factory(2)
# cube = power_factory(3)

# # 
# print(square(4))
# print(cube(4))


###########################
# mutable default values can lead to unexpected behaviour 

# # Potential pitfall with mutable defaults
# def add_item(item, items=[]):
#     items.append(item)
#     return items

# print(add_item(1))  # [1]
# print(add_item(2))  # [1, 2] - items persists between calls!

###########################################################################

# input_dict = {"name": "azam", "age": 29}
# input_list = [1,2,3,4]

# def update_dict():
#     input_dict["age"] = 5
#     print(input_dict)
#     # return  input_dict

# result = update_dict()
# print(result)

#################################################################

# def append_to_list(value, my_list=[]):
#     my_list.append(value)
#     return my_list

def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # Output: [1]
print(add_item(2))  # Output: [1, 2] - Surprise!
print(add_item(3))  # Output: [1, 2] - Surprise!
