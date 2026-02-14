'''
Josephus(N, 2) ：约瑟夫环的特殊情况（有闭式解）
N = 2^m + L
答案 = 2L + 1（把最高位的1移到第1位）
'''
N = int(input())

# 最大的 2 的幂
highest_power = 1 << (N.bit_length() - 1)
print(N.bit_length())
L = N - highest_power
print(2 * L + 1)

