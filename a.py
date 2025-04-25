import re

# 1. Kiểm tra chuỗi chữ cái thường bắt đầu bằng 'a'
def kiem_tra_chuoi_bat_dau_bang_a(chuoi):
  pattern = r"^a[a-z]*$"
  if re.match(pattern, chuoi):
    return True
  else:
    return False

# Các ví dụ kiểm tra cho trường hợp 1
print(kiem_tra_chuoi_bat_dau_bang_a("apple"))   # Output: True
print(kiem_tra_chuoi_bat_dau_bang_a("apricot")) # Output: True
print(kiem_tra_chuoi_bat_dau_bang_a("a"))       # Output: True
print(kiem_tra_chuoi_bat_dau_bang_a("banana"))  # Output: False
print(kiem_tra_chuoi_bat_dau_bang_a("Apple"))   # Output: False (chữ 'A' hoa)
print(kiem_tra_chuoi_bat_dau_bang_a("a123"))    # Output: False (có số)

print("-" * 30)

# 2. Kiểm tra chuỗi bắt đầu bằng một từ và kết thúc bằng một số nguyên
def kiem_tra_tu_dau_so_cuoi(chuoi):
  pattern = r"^\w+\d+$"
  if re.match(pattern, chuoi):
    return True
  else:
    return False

# Các ví dụ kiểm tra cho trường hợp 2
print(kiem_tra_tu_dau_so_cuoi("word123"))     # Output: True
print(kiem_tra_tu_dau_so_cuoi("data_5"))      # Output: True (gạch dưới được coi là một phần của từ)
print(kiem_tra_tu_dau_so_cuoi("info2024"))    # Output: True
print(kiem_tra_tu_dau_so_cuoi("123word"))     # Output: False (bắt đầu bằng số)
print(kiem_tra_tu_dau_so_cuoi("word"))        # Output: False (không có số ở cuối)
print(kiem_tra_tu_dau_so_cuoi("123"))         # Output: False (không có chữ ở đầu)
print(kiem_tra_tu_dau_so_cuoi("word 123"))    # Output: False (có khoảng trắng)
print(kiem_tra_tu_dau_so_cuoi("word-123"))    # Output: False (dấu gạch ngang không phải là \w)