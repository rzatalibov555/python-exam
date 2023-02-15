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

# l = [1, 2, 5, 2, 7, 3, 8, 9, 5]

# largest = min(l)
# l.remove(largest)
# largest2 = min(l)
# l.remove(largest2)
# print(largest+largest2)

# =================================================================


# l = [1, 2, 5, 2, 7, 3, 8, 9, 5]

# largest = max(l)
# l.remove(largest)
# largest2 = max(l)
# l.remove(largest2)
# print(largest+largest2)


# ======================QUESTION 7===========================================

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = {}
# for key1, value1 in d1.items():
#     for key2, value2 in d2.items():
#         if not key1 in d2.keys():
#             d3[key1] = value1
#             continue
#         if key2 in d1.keys():
#             if key1 == key2:
#                 d3[key1] = value1 + value2
#         else:
#             d3[key2] = value2 
# print(d3)


# ======================QUESTION 8===========================================
            # VERSION1
            
# a = ['PY01', 'PY02', 'PY03', 'PY04']
# b = ['Baki', 'Sumqayit', 'Qubadlı', 'Lənkəran']
# c = [90, 50, 39, 42]

# d = list()

# for index in range(len(a)):
#     extra = dict()
#     extra[a[index]]  = {b[index]: c[index]}
#     d.append(extra)
# print(d)

            # VERSION2
            
# a = ['PY01', 'PY02', 'PY03', 'PY04']
# b = ['Baki', 'Sumqayit', 'Qubadlı', 'Lənkəran']
# c = [90, 50, 39, 42]

# dict_1 = dict(zip(b,c))
# dict_2 = dict().fromkeys(a,dict_1)
# print(dict_2)

# ======================QUESTION 11===========================================

# list_ = [1,2,3,4,5]

# for index, val in enumerate(list_):
#     list_[index] = index **2
# print(list_)

# ======================QUESTION 13===========================================

# myDict = {
#     "name": "fuad",
#     "point": 66
# }
# d = dict()
# for key, val in myDict.items():
#     d[val] = key
# print(d)


# ======================QUESTION 13===========================================

# a = input("ilk sozu daxil et: ")
# b = input("ikinci sozu daxil et: ")

# a, b = b, a

# print(a, b , sep="\n")

# ======================QUESTION 16===========================================

# a = int(input("a: "))
# b = int(input("b: "))

# count = 0

# for i in range(a, b):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         count+=1
# if a == 1:
#     print(count-1)
# else:
#     print(count)


# ======================QUESTION 17===========================================

# word = input("deyer daxil et: ").lower()

# print(word[0] + word[1:].replace(word[0],'$'))

# ======================QUESTION 18===========================================

# word = input("deyer daxil et: ")

# print(word[-1] + word[1:-1] + word[0])


# ======================QUESTION 19===========================================

# search = input("Search: ").lower()
# word   = input("Enter text: ").lower()

# if search in word:
#     print("var",word.count(search))
# else:
#     print("yoxdur")


# ======================QUESTION 20===========================================

# myList = [1, 2, 3, 1, 4, 2, 5, 3, 7, 8, 9, 8, 1 ,9]

# for index, val in enumerate(myList):
#     if not val in myList[index+1:]:
#         print(val)
#         break


# ======================  DECORATORS =========================

# def test():
#     def wrapper():
#         return func().split()
#     return wrapper

# @test

# def say_hello():
#     return "Hello world"

# print(say_hello())


# ========================= DECORATORS (param)==============================



# def italic(func):
#     def wrapper(a,b,c):
#         return "<i>"+func(a,b,c)+"</i>"
#     return wrapper

# def bold(func):
#     def wrapper():
#         return "<b>"+func()+"</b>"
#     return wrapper

# def underline(func):
#     def wrapper():
#         return "<u>"+func()+"</u>"
#     return wrapper

# # @underline
# # @bold
# @italic
# def say_hello(a,b,c):
#     return a +"-"+ b + "-" + c


# print(say_hello("1","hello","2"))

# ========================= DECORATORS ==============================


# list_1 = ['2','Ad', 'Soyad']


# def lenght_of_list(func):
#     def wrapper(a):
#         return len(func(a))*3
#     return wrapper

# @lenght_of_list

# def result(a):
#     return a

# print(result(list_1))


# ========================= DECORATORS ==============================


# list_1 = [1, 2, '3','Ad', 'Soyad','4',5]
# list_2 = []

# def sum_of_list(func):
#     def wrapper(a):
#         sum_ = 0
#         for items in func(a):
#             if str(items).isdigit():
#                 sum_ += int(items)
#         return sum_
        
#     return wrapper

# @sum_of_list



# def result(a):
#     return a

# print(result(list_1))


# ========================= DECORATORS ==============================



# inp = int(input("reqem daxil edin: "))

# def sum_of_list(func):
#     def wrapper(a):
#         sum_ = 0         # abs  () menfi ile verilen reqemleri musbet edir (-1991) -> (1991)
#         for items in str(abs(func(a))):  #str() integerle 1991-i boldu "1","9","9","1"
#             sum_ += int(items)
#         return sum_
        
#     return wrapper

# @sum_of_list



# def result(a):
#     return a

# print(result(inp))


# ========================= CLASS ==============================

# class Calculator:

#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def toplama(self):
#         return self.num1 + self.num2
    
#     def cixma(self):
#         return self.num1 - self.num2
    
#     def vurma(self):
#         return self.num1 * self.num2
        
#     def bolme(self, a):
#         return self.num1 / self.num2 * a
    
    
#     def display(self,):
#         return self.toplama(), self.cixma(), self.vurma(), self.bolme(5)
    
    
# obj = Calculator(num1 = 10, num2 = 2)
# print(*obj.display())     ## burdaki * funksiyanin icindeki tuple-lari yox edir


# ========================= CLASS (varislik) ==============================

# class Rectangle:

#     def __init__(self, uzunluq, eni):
#         self.uzunluq = uzunluq
#         self.eni = eni
    
#     def Area(self):
#         return self.uzunluq * self.eni

# class Paraliliped(Rectangle):

#     def __init__(self, uzunluq, eni, hundurluk):
#         super().__init__(uzunluq, eni)
#         self.hundurluk = hundurluk

#     def Volume(self):
#         return self.Area() * self.hundurluk

# obj = Paraliliped(2, 3, 5)

# print(obj.Volume())


# ========================= EXERCISE  ============================== Palindrome


# class Triangle:

#     def __init__(self, angle1, angle2, angle3):
#         self.angle1 = angle1
#         self.angle2 = angle2
#         self.angle3 = angle3

#     number_of_sides = 3

#     def check_angles(self):
        
#         total_ = self.angle1+self.angle2+self.angle3
#         if total_ == 180:
#             return total_
#         else:
#             return False
        


# my_triangle = Triangle(90,30,60)

# print(my_triangle.number_of_sides)
# print(my_triangle.check_angles())


# ========================= EXERCISE  ============================== 

# friends = {}
# i = 0
# for i in range(3):
#     name = input("Ad daxil edin")
#     phone = input("Telefon nömrəsi daxil edin")
#     friends[name] = phone
# print(friends)