import os
import random
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio


TOTAL_MONEY = 1000
NUMBER_OF_AGENTS = 1000
MAX_INTERACTIONS = NUMBER_OF_AGENTS // 2
THRESHOLD = 0.0000005
TIME_STEPS = 150

money_distribution = [TOTAL_MONEY / NUMBER_OF_AGENTS for _ in range(NUMBER_OF_AGENTS)]
frames = []
entropy_list = []
print(sum(money_distribution))
def plot_histogram(money_distribution, time_step, entropy):
    plt.hist(money_distribution, bins=50, edgecolor='black')
    plt.title(f"Money Distribution at Time Step {time_step}\nEntropy: {entropy:.4f}")
    plt.xlabel("Amount of Money")
    plt.ylabel("Number of Agents")
    plt.grid(True)

    plt.savefig('frame.png')
    plt.close()

def calculate_entropy(money_distribution, number_of_agents):
    bins = np.histogram_bin_edges(money_distribution, bins='auto')
    frequencies, _ = np.histogram(money_distribution, bins=bins)
    probabilities = frequencies / number_of_agents
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-9))
    return entropy

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


    entropy = calculate_entropy(money_distribution, NUMBER_OF_AGENTS)
    entropy_list.append(entropy)

    plot_histogram(money_distribution, t, entropy)
    frames.append(imageio.imread('frame.png'))
    os.remove('frame.png')

    if t > 0 and abs(entropy_list[t] - entropy_list[t-1]) < THRESHOLD * entropy_list[t-1]:
        print(f"\nSimulation stoped at time step {t} due to entropy stabilization")
        break

imageio.mimsave('money_distribution_evolution.gif', frames, duration=20 / TIME_STEPS)

entropy_frames = []

for t, entropy in enumerate(entropy_list):
    plt.plot(entropy_list[:t+1])
    plt.title(f"Entropy evolution up to Time Step {t}")
    plt.xlabel("Time Step")
    plt.ylabel("Entropy")
    plt.grid(True)

    plt.savefig('entropy_frame.png')
    plt.close()
    entropy_frames.append(imageio.imread('entropy_frame.png'))
    os.remove('entropy_frame.png')

imageio.mimsave('entropy_evolution.gif', entropy_frames, duration=20 / TIME_STEPS)
print(f"Dinero final: {sum(money_distribution)}")
print("\nSimulation completed. GIFs saved as 'money_distribution_evolution.gif' and 'entropy_evolution.gif'.")


