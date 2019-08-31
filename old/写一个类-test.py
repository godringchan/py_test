class Custemer(object):
    def __init__(self, money):
        self.__money = money
    def buy(self, price):
        if price > self.__money:
            print("钱不够啊")
        else:
            self.__money -= price
            print("花了%d块钱，还剩%d" % (price, self.__money))

if __name__ == "__main__":
    c1 = Custemer(1000)
    c1.buy(500)
    c1.buy(600)
