import pandas as pd

def calculate_monthly_payment_details(loan_amount, rate, months):
    monthly_principal = loan_amount / months
    details = []
    for i in range(months):
        interest_payment = (loan_amount - i * monthly_principal) * (rate / 100 / 12)
        total_payment = monthly_principal + interest_payment
        details.append({
            "Month": i + 1,
            "Principal": monthly_principal,
            "Interest": interest_payment,
            "Total Payment": total_payment
        })
    return details

def compare_interest_rates(loan_amount, original_rate, new_rate, months):
    original_details = calculate_monthly_payment_details(loan_amount, original_rate, months)
    new_details = calculate_monthly_payment_details(loan_amount, new_rate, months)
    
    comparison = []
    for original, new in zip(original_details, new_details):
        comparison.append({
            "Month": original["Month"],
            "Original Total Payment": original["Total Payment"],
            "New Total Payment": new["Total Payment"],
            "Savings": original["Total Payment"] - new["Total Payment"]
        })
    return comparison

# 设置贷款参数
loan_amount = 1550000  # 155万
months = 20 * 12  # 20年

# 原利率和新利率
original_rate = 4.2  # 4.2%
new_rate = 3.7  # 3.7%

# 计算利率比较
payment_comparison = compare_interest_rates(loan_amount, original_rate, new_rate, months)

# 输入指定的还款期数区间
start_month = 42  # 开始月份
end_month = 50    # 结束月份

# 输出指定区间的数据
df_payment_comparison = pd.DataFrame(payment_comparison)
df_selected_range = df_payment_comparison[(df_payment_comparison['Month'] >= start_month) & (df_payment_comparison['Month'] <= end_month)]

# 打印指定区间的比较结果
print(df_selected_range)
