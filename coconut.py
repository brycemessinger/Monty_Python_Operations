import math


swallow_weight = 60
swallow_carrying_capacity = swallow_weight / 3
# print(swallow_carrying_capacity)


coconut_weight = 1450
swallow_to_coconut_ratio = coconut_weight / (swallow_weight / swallow_carrying_capacity)
# print(swallow_to_coconut_ratio)

def swallow_to_anything_ratio(item):
    # print(item)
    # print(swallow_carrying_capacity)
    print(math.ceil(item / swallow_carrying_capacity))

swallow_to_anything_ratio(coconut_weight)
