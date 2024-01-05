def bayes(p_a, p_b_given_a, p_b_given_not_a):
    """
    计算贝叶斯概率 P(A|B)

    参数:
    p_a -- P(A) 的概率
    p_b_given_a -- P(B|A) 的概率
    p_b_given_not_a -- P(B|~A) 的概率

    返回:
    P(A|B) 的概率
    """
    p_not_a = 1 - p_a
    # P(B) = P(B|A) * P(A) + P(B|~A) * P(~A)
    # 阳性的概率 = 有疾病的概率 * 测试阳性给定有疾病的概率 + 没有疾病的概率 * 测试阳性给定没有疾病的概率
    p_b = p_b_given_a * p_a + p_b_given_not_a * p_not_a
    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b

# 有疾病的概率
p_disease = 0.01

# 测试阳性给定有疾病的概率
p_pos_given_disease = 0.9

# 测试阳性给定没有疾病的概率
p_pos_given_no_disease = 0.1

# 计算有疾病给定测试阳性的概率
p_disease_given_pos = bayes(p_disease, p_pos_given_disease, p_pos_given_no_disease)

print('有疾病给定测试阳性的概率:', p_disease_given_pos)