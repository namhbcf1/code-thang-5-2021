class circle(object):

    def __init__(self, chieudai, chieurong):
        self.chieudai = int(chieudai)
        self.chieurong = int(chieurong)

    def tinh_chu_vi(self):
        return (self.chieudai + self.chieurong)*2
    
    def tinh_dien_tich(self):
        return (self.chieudai* self.chieurong)

def main():
    HChuNhat = circle(input(),input())
    print("Chieu dai hinh chu nhat: ", HChuNhat.chieudai)
    print("Chieu rong hinh chu nhat: ", HChuNhat.chieurong)
    print("Chu vi hinh chu nhat: ", HChuNhat.tinh_chu_vi())
    print("Dien tich hinh chu nhat: ", HChuNhat.tinh_dien_tich())

if __name__ == "__main__":
    main()