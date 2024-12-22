# Nhập chiều cao của An, Minh và Lan
an_height = float(input("Nhập chiều cao của An (m): "))
minh_height = float(input("Nhập chiều cao của Minh (m): "))
lan_height = float(input("Nhập chiều cao của Lan (m): "))

# So sánh chiều cao
if an_height > minh_height and an_height > lan_height:
    tallest = "An"
elif minh_height > an_height and minh_height > lan_height:
    tallest = "Minh"
else:
    tallest = "Lan"

# Xuất kết quả
print(f"Người cao nhất là: {tallest}")