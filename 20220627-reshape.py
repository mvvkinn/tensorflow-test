import tensorflow as tf

tensor = tf.constant(range(0, 24))
print(tensor)
print(tf.rank(tensor))

tensor1 = tf.reshape(tensor, [3, 8]) # shape=(3,4) 형태로 변환
print(tensor1)

tensor2 = tf.reshape(tensor, [-1, 4])  # -1 => 4열에 대한 변환만 명시되어 나머지는 자동으로 변환됨, 반대로 입력하면 반대도 마찬가지
print(tensor2)

tensor3 = tf.reshape(tensor2, [-1])  # 원래 벡터로 다시 변환됨
print(tensor3)

tensor4 = tf.reshape(tensor, [-1, 3, 4])  # (_, 3, 4) 형태로 변환 => lv3
print(tensor4)