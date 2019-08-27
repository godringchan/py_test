class Test_1():
    def __init__(self, name):
        self.__name = name

    def set_name(self, new_name):
        if len(new_name) < 5:
            print("名字长度少于5")
        else:
            self.__name = new_name
            print("新名字%s" % self.__name)

    def get_name(self):
        print(self.__name)
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    
test_1 = Test_1("maliujia")
test_1.get_name()
# test_1.set_name("banama")
test_1.get_name()
print(test_1.name)
test_1.name = "mmmmm"
print(test_1.name)