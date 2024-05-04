class p9e2:
    @staticmethod
    def methodTambah(x, y):
        if type(x) == int and type(y) == int:
            return x + y
        elif type(x) == float and type(y) == float:
            return x + y
        else:
            return "Tipe data tidak valid"

myNum1 = p9e2.methodTambah(8, 5)
myNum2 = p9e2.methodTambah(4.5, 6.5) 
print("int:", myNum1)
print("float:", myNum2)
