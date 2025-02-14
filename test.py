from info import display_resource_monitor, log_metrics, display_metrics
from info.rl import log_episode, display_episodes
import time
import random
import math
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def test_rl_info():
    reward_bias = 0
    max_steps = 100_000
    step = 0
    while step < max_steps:
        ep_len = 0
        for i in range(4096):
            step+=1
            ep_len += 1
            if random.random() < 0.01:
                log_episode(random.random() + reward_bias, ep_len, step=(step, max_steps))
                ep_len = 0
            reward_bias += 0.01 * random.random()
    display_episodes()

def test_train_info():
    loss = 10.0
    epochs = 3
    batches = 300

    for it in range(1):
        for epoch in range(epochs):
            for batch in range(batches):
                loss_ =  math.log2(abs(loss))
                acc = loss + random.random()
                log_metrics(
                    name=("loss", "acc"),
                    value=(loss_, acc),
                    epoch_idx=(epoch, epochs),
                    batch_idx=(batch, batches)
                )
                loss -= 1e-2
                time.sleep(0.001)
        print('\n\n\n')
            
    display_metrics(True)

def test_graph_plotting():
    values = [10, 15, 17, 18, 18.3]
    values2 = [9, 14, 17.5, 19, 20.1]
    values3 = [10, 14.2, 17.7, 19.2, 20.3]
    from info import plot_graph
    plot_graph((values, values2, values3), marker=".")


display_resource_monitor()
