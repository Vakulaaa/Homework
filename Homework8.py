import random

rand_nums = random.randint(3, 10)
rand_list = [random.randint(1, 10) for _ in range(rand_nums)]
new_list = rand_list[0], rand_list[1], rand_list[-2]
print(new_list)
