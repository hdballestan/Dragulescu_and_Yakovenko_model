import os
import random
import numpy as np
import matplotlib.pyplot as plt
import imageio


TOTAL_MONEY = 1000
NUMBER_OF_AGENTS = 1000
TIME_STEPS = 80

money_distribution = [TOTAL_MONEY / NUMBER_OF_AGENTS for _ in range(NUMBER_OF_AGENTS)]

MAX_INTERACTIONS = NUMBER_OF_AGENTS // 2

frames = []

def plot_histogram(money_distribution, time_step):
    plt.hist(money_distribution, bins=20, edgecolor='black')
    plt.title(f"Money Distribution at Time Step {time_step}")
    plt.xlabel("Amount of Money")
    plt.ylabel("Number of Agents")
    plt.grid(True)

    plt.savefig('frame.png')
    plt.close()


for t in range(TIME_STEPS):

    interaction_per_time_step = random.randint(1, MAX_INTERACTIONS)

    for _ in range(interaction_per_time_step):

        agent_i = random.randint(0, NUMBER_OF_AGENTS - 1)
        agent_j = random.randint(0, NUMBER_OF_AGENTS - 1)

        while agent_i == agent_j:
            agent_j = random.randint(0, NUMBER_OF_AGENTS - 1)

        max_loss_i = money_distribution[agent_i]
        max_loss_j = money_distribution[agent_j]

        loss_i = random.uniform(0, max_loss_i)
        loss_j = random.uniform(0, max_loss_j)

        money_distribution[agent_i] -= loss_i
        money_distribution[agent_j] += loss_i

        money_distribution[agent_j] -= loss_j
        money_distribution[agent_i] += loss_j

    plot_histogram(money_distribution, t)
    frames.append(imageio.imread('frame.png'))
    os.remove('frame.png')

imageio.mimsave('money_distribution_evolution.gif', frames, duration= 20 / TIME_STEPS)

print("\nSimulation completed. GIF saved as 'money_distribution_evolution.gif'.")
