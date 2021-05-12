class Circle(object):
    def __init__(self, r):
        self.radius = r
    def dientich(self):
        return self.radius**2*3.14

    def chuvi(self):
        return self.radius*2*3.14
def main():
    print("mời nhập vào bán kính: ")
    bankinh = int(input())

    classCircle = Circle(bankinh)
    print("Diện tích của hình tròn là: ")
    print (classCircle.dientich())  
    print("Chu vi của hình tròn là: ")
    print(classCircle.chuvi())
if __name__=="__main__":
    main()