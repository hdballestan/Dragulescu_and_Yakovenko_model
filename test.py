import random
import numpy as np


TOTAL_MONEY = 100
NUMBER_OF_AGENTS = 10

NUMBER_OF_EXCHANGES = 10


money_distribution = [TOTAL_MONEY / NUMBER_OF_AGENTS for _ in range(NUMBER_OF_AGENTS)]

print(money_distribution)

for _ in range(NUMBER_OF_EXCHANGES):
    index_1 = random.randint(0, NUMBER_OF_AGENTS - 1)
    index_2 = random.randint(0, NUMBER_OF_AGENTS - 1)

    max_loss_1 = min(money_distribution[index_1], money_distribution[index_2])
    max_loss_2 = min(money_distribution[index_2], money_distribution[index_1])

    loss_1 = random.uniform(0, max_loss_1)
    loss_2 = random.uniform(0, max_loss_2)

    money_distribution[index_1] -= loss_1
    money_distribution[index_2] += loss_1

    money_distribution[index_2] -= loss_2
    money_distribution[index_1] += loss_2

print("After", NUMBER_OF_EXCHANGES, "exchanges:")
print(money_distribution)
