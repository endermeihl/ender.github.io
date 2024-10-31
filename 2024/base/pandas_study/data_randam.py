import csv
import random

# 职业列表
jobs = ["Engineer", "Teacher", "Doctor", "Lawyer", "Nurse", "Scientist", "Artist", "Programmer", "Chef", "Mechanic"]

# 生成随机数据
data = [{"Job": random.choice(jobs), "Salary": random.randint(30000, 120000)} for _ in range(10)]

# 写入 CSV 文件
with open("villains.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Job", "Salary"])
    writer.writeheader()
    writer.writerows(data)

print("CSV 文件已生成：random_jobs.csv")
