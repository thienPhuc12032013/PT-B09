# Nhập vào số kẹo và số em bé
a = int(input("Nhập vào số chiếc kẹo (a): "))
b = int(input("Nhập vào số em bé (b): "))

# Kiểm tra xem a có chia đều cho b hay không
if a % b == 0:
    print("Có")
else:
    print("không")