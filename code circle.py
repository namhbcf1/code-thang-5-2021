class Circle(object):
    def __init__(self, dai):
        self.chieudai = dai
    def __init__(self, b):
        self.chieurong = b
    def dientich(self):
        dt = self.chieudai * b
        return dt

    def chuvi(self):
        return self.a
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