# class Restaurant:
#     def __init__(self, menu_items, book_table, customer_order):
#         menu_items = self.menu_items
#         book_table = self.book_table
#         customer_order = self.customer_order

#     def add_item_to_menu_book():
#         ...

#     def book_tables():
#         ...

# ================================================================


# class Employee:
#     def __init__(self, emp_id, emp_name, emp_salary, emp_department):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.emp_salary = emp_salary
#         self.emp_department = emp_department
    
    

#     def calculate_emp_salary(self, hours_worked, emp_salary):
#         overtime = hours_worked - 50
#         overtime_amount = (overtime * (emp_salary / 50))
#         return overtime_amount + self.emp_salary
        

#     def emp_assign_department(self,department):
#         self.emp_department = department
#         return self.emp_department
#     def print_employee_details(self):
#         return f"{self.emp_id}\n{self.emp_name}\n{self.emp_salary}\n{self.emp_department}\n"


# obj = Employee(1,'Rza',1600,'Coders')
# print(obj.calculate_emp_salary(24,1600))
# print(obj.print_employee_details())
# print(obj.emp_assign_department("IT"))




# ======================= Product add, update, get =========================================

# class Inventory:
    
#     def __init__(self):
#         self.inventory = {}

#     def add_item(self,item_id,item_name, stock_count, price):
#         self.inventory[item_id] = {'item_name':item_name, 'stock_count':stock_count, 'price':price }
#         return self.inventory[item_id]

#     def item_update(self,item_id,item_name, stock_count, price):

#         if item_id in self.inventory:
#             self.inventory[item_id]['item_name'] = item_name
#             self.inventory[item_id]['stock_count'] = stock_count
#             self.inventory[item_id]['price'] = price
#         else:
#             return "Item not found in inventory."
        


        

#     def check_item_details(self,item_id):
#         if item_id in self.inventory:
#             item = self.inventory[item_id]
#             return f"Product Name: {item['item_name']}, Stock Count: {item['stock_count']}, Price: {item['price']}"
#         else:
#             return "Item not found in inventory."

# obj = Inventory()
# obj.add_item(1, "Laptop", 100, 500.00)
# obj.add_item(2, "Mobile", 110, 450.00)
# obj.add_item(3, "Desktop", 120, 500.00)
# obj.add_item(4, "Tablet", 90, 550.00)



# obj.item_update(2, "Mobile_tel", 200, 550.00)
# print(obj.check_item_details(2))




# ==================================================================



# class FindTwoSum:
 
#     def __init__(self, given_list, target):
#         self.given_list = given_list
#         self.target = target
 
 
#     def get_result_list(self):
#         result = []
 
#         for i in range(len(self.given_list)):
#             if i != len(self.given_list)-1:
#                 for j in range(i+1, len(self.given_list)):
#                     if self.given_list[i] + self.given_list[j] == self.target:
#                         result.append((i, j))
 
#         return result
 
 
# list1, target1 = [2, 7, 11, 3, 6, 15, 4], 9
# list2, target2 = [3, 2, 4], 6
# list3, target3 = [3, 3], 6
 
 
# print(FindTwoSum(list1, target1).get_result_list())
# print(FindTwoSum(list2, target2).get_result_list())
# print(FindTwoSum(list3, target3).get_result_list())



# ===================================================================



# class FindTarget:
 
#     def __init__(self, given_list, target):
#         self.given_list = given_list
#         self.target = target
 
 
#     def find_target_index(self):
#         self.given_list.sort()
#         # self.given_list = sorted(self.given_list)
 
#         if self.target in self.given_list:
#             return self.given_list.index(self.target)
 
#         for i in range(len(self.given_list)):
#             if i == len(self.given_list) - 1:
#                 return len(self.given_list)
#             if self.target > self.given_list[i] and self.target < self.given_list[i+1]:
#                 return i+1
 
 
 
# list1, target1 = [1,3,5,6], 5
# list2, target2 = [1,3,5,6], 2
# list3, target3 = [1,3,5,6], 7
# print(FindTarget(list1, target1).find_target_index())
# print(FindTarget(list2, target2).find_target_index())
# print(FindTarget(list3, target3).find_target_index())