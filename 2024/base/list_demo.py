# 索引，切片，相加，相乘，长度，最大值，最小值，排序，反转
# 列表是可变的，元组是不可变的
# 列表是有序的，元组是无序的
# 列表是可重复的，元组是不可重复的

# 列表的索引

months = ['month','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
endings = ['day']+['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
print(endings)

year = input('Year: ')
month = input('Month(1-12): ')
day = input('Day(1-31): ')

month_number = int(month)
print(month_number)
print(months[1:month_number:-1])
day_number = int(day)
print(day_number)

month_name = months[month_number]
ordinal = day + endings[day_number]

print(month_name + ' ' + ordinal + ', ' + year)