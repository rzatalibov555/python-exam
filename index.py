# ================== QUESTION 1 =============================
    
# def check_dictionary():
#     inp = input("Daxil edin: ")
#     dict_1 = {"name": "Fuad", "keyword":"Coders", "position":"teacher"}
    

#     if inp in dict_1.values() or inp in dict_1.keys():
#         return "Var"
    
#     else:
#         return "Does not exist"
    
# print(check_dictionary())  
# ===========================================================

# ===========================================================

# def tup():
#     upper_ = 0
#     lower_ = 0
#     inp = input("Nese daxil et: ")
    
#     for x in inp:
      
#         if x.isupper():
#             upper_ += 1
            
#         if x.islower():
#             lower_ += 1
               
#     return "big count:" ,upper_, "small count:", lower_


# print(tup())

# ===========================================================


# ================== QUESTION 6 =============================


# def print_key_and_values():
    
#     dict_1 = {
#         "name": "Fuad", 
#         "keyword":"Coders", 
#         "position":"teacher"
#     }
    
#     for key, value in dict_1.items():
        
#         print(key, value)
    
# print_key_and_values()

# ===========================================================


# dict_1 = {
#     "name": "Fuad", 
#     "keyword":"Coders", 
#     "position":"teacher"
# }

# print(*dict_1.keys(), *dict_1.values())


# dict_1 = {
#     "name": "Fuad", 
#     "keyword":"Coders", 
#     "position":"teacher"
# }
    
# for key, value in dict_1.items():
        
#     print(key, value)

# ===========================================================







# ===========================================================
# ===================== QUESTION 4 ==========================

# name_    = input("Value 1 daxil edin: ")
# surname = input("Value 2 daxil edin: ")

# n = name_.replace(name_[0],surname[0])
# s = surname.replace(surname[0],name_[0])

# print(n,s)

# ===========================================================


# ===================== QUESTION 14 ==========================

# name_    = input("Value 1 daxil edin: ")
# surname = input("Value 2 daxil edin: ")

# n = name_.replace(name_,surname)
# s = surname.replace(surname,name_)

# print(n,s)

# ===========================================================
# =====================QUESTION 18===========================

# name_    = input("Value 1 daxil edin: ")
# ilk = name_[0]
# son = name_[-1]
     
# netice = son + name_[1:-1] + ilk
# print(netice)





# ====================QUESTION 19============================

    
# search = input("Search: ")
# word   = input("Enter text: ")

# search = search.lower()
# word = word.lower()
# # for x in word:
# if search in word:
#     print("var")
# else:
#     print("yoxdur")


# ====================QUESTION 15============================
thislist = ["apple", "banana", "cherry"]
thislist2 = ["Fuad", "Rza", "Sebuhi"]


# 1ci variant
# print(thislist+thislist2)


# 2ci variant
# for x in thislist2:
#   thislist.append(x)
# print(thislist)


# 3cu variant
# thislist.extend(thislist2)
# print(thislist)


# ===========================================================
# ===========================================================


# mydict = {
# 	"author" : {
# 		"name": "Fuad",
# 		"point": 66
#     }
# }

# print(mydict["author"]["point"])


# ===========================================================
# ========================QUESTION 9=========================

# print(sum(sorted([9,1,3,4,5,7,0,8])[-2:]))

# ===========================================================

l = [1, 2, 5, 2, 7, 3, 8, 9, 5]

largest = min(l)
l.remove(largest)
largest2 = min(l)
l.remove(largest2)
print(largest+largest2)