continue_or_end = "y"
while continue_or_end == "y":
    quantity = int(input("Nhập số lượng nhân viên: "))
    for i in range(1,quantity+1):
        print(f"Nhân viên {i}")
        name = input("Tên nhân viên: ")
        date = int(input("Số ngày đi làm: "))
        print("Thông tin nhân viên: ")
        print(f"Tên: {name}")
        print(f"Số ngày đi làm: {date}")
        if date < 20 and date >= 1: 
            print("Cần cải thiện chuyên cần")
        else :
            print("Nhân viên chuyên cần tốt")

    continue_or_end = input("Tiếp tục chương trình? (y/n): ")
print("Chương trình kết thúc")