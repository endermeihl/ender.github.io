# 先验概率
p_disease = 0.01 #疾病的概率
p_no_disease = 1 - p_disease #没有患病的概率

# 测试的准确率
p_pos_given_disease = 0.99 #测试结果为阳性的情况下，这个人真正患有这种疾病的概率
p_pos_given_no_disease = 0.01 #测试结果为阳性的情况下，这个人没有患有这种疾病的概率

# 计算 P(阳性)
# 边缘概率 = 有疾病的概率 * 测试阳性给定有疾病的概率 + 没有疾病的概率 * 测试阳性给定没有疾病的概率
p_pos = p_pos_given_disease * p_disease + p_pos_given_no_disease * p_no_disease 

# 使用贝叶斯公式计算 P(疾病|阳性)
# P(疾病|阳性) = P(阳性|疾病) * P(疾病) / P(阳性)
p_disease_given_pos = p_pos_given_disease * p_disease / p_pos

print('在测试结果为阳性的情况下，这个人真正患有这种疾病的概率是：', p_disease_given_pos)