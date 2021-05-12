class Sohoc(object):
    def __init__(self, num1, num2):
        self.__num1 = int(num1)
        self.__num2 = int(num2)

    def cong(self):
        print(self.__num1+self.__num2)

    def tru(self):
        print(self.__num1-self.__num2)

    def nhan(self):
        print(self.__num1*self.__num2)

    def chia(self):
            print(self.__num1 / self.__num2)

def main():
    print("moi nhap vao num1 và num 2: ")
    sohocmain = Sohoc(input(),input())
    print("phép tính cộng là: ")
    sohocmain.cong()
    print("phép tính trừ là: ")
    sohocmain.tru()
    print("phép tính nhân là: ")
    sohocmain.nhan()
    print("phép tính chia là: ")
    sohocmain.chia()


if __name__ == "__main__":
    main()