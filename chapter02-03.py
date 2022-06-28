import tensorflow as tf
import numpy as np

a = tf.constant(1) # scalar 정의하는 방식
b = tf.constant(2)

print(a)
print(b)

# scalar = rank 0 tensor
# vector = rank 1 tensor
# [12, 34] 오른쪽 방향

# [12,
# 34] 방향 아래로 가짐



# 벡터를 생성 방법 두가지 =
# 1. 파이썬 기본 자료형인 리스트를 tf.constant에 넣어 벡터 생성
py_list = [10., 20., 30.,]  # . 붙여 float32로
vec1 = tf.constant(py_list, dtype=tf.float32)

print(tf.rank(vec1))  # 1, dtype=int32 뜨는 이유는 Rank = 1이고, 랭크에 대한 타입임.

# 2. Numpy 이용하여 생성
np_list = np.array([10., 20., 30.])
vec2 = tf.constant(np_list, dtype=tf.float32)
print(vec2)
print(tf.rank(vec2))

#행렬 생성
list_of_list = [[10, 20, 30], [40, 50, 60]]
mat1 = tf.constant(list_of_list)

print(mat1)
print(tf.rank(mat1))  # 출력에서 shape=() 인 이유는 랭크(2, scalar)에 대한 shape기 때문
