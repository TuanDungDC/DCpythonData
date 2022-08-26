import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
#symbols = "{}[]()#@,*_-."
symbols = "!@#$%&?"
all = lower + upper + numbers + symbols # Tổng hợp hết các ký tự xuất hiện trong password
length = 20 # Độ dài của password 
password = "".join(random.sample(all, length)) 
print("Your password is : " , password)

# Với tổng 69 ký tự có thể tạo ra 5983865382382622672294674517005559601 ( password có 20 lý tự ) khác nhau .