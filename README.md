# Implementing-Reinforcement-learning-over-flappy-bird-game
A Deep Q-Network (DQN) based Reinforcement Learning agent trained to play Flappy Bird autonomously using PyTorch and Gymnasium. The agent learns through trial and error, leveraging Experience Replay and Target Networks to optimize its gameplay strategy.
# 🐦 Flappy Bird AI using Deep Q-Network (DQN)

A Reinforcement Learning project that trains an AI agent to play Flappy Bird using the Deep Q-Network (DQN) algorithm. The agent learns through trial and error by interacting with the environment and maximizing cumulative rewards over time.

---

## 🚀 Project Overview

This project demonstrates the application of **Deep Reinforcement Learning** to a classic game environment. The AI agent starts with no prior knowledge of the game and gradually learns how to avoid obstacles and achieve higher scores by optimizing its policy through experience.

The implementation uses:

* Deep Q-Networks (DQN)
* Experience Replay
* Target Network Synchronization
* Epsilon-Greedy Exploration Strategy
* PyTorch for Deep Learning
* Gymnasium-based Flappy Bird Environment

---

## 🎯 Features

✅ Deep Q-Network (DQN) implementation

✅ Experience Replay Memory

✅ Target Network updates

✅ Epsilon-Greedy exploration

✅ Model checkpoint saving and loading

✅ YAML-based hyperparameter configuration

✅ Training and testing modes

✅ GPU support with CUDA

---

## 🛠️ Tech Stack

* Python
* PyTorch
* Gymnasium
* Flappy Bird Gymnasium
* NumPy
* YAML

---

## 📂 Project Structure

```text
FlappyBird-DQN/
│
├── Ag.py                    # Main training and testing script
├── doQN.py                  # DQN neural network architecture
├── experience_replay.py     # Replay memory implementation
├── parameter.yaml           # Hyperparameter configuration
│
├── runs/
│   ├── FlappyBirdv0.pt      # Saved model weights
│   └── FlappyBirdv0.log     # Training logs
│
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/saksham966/FlappyBird-DQN.git
cd FlappyBird-DQN
```

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install torch gymnasium flappy-bird-gymnasium pyyaml numpy
```

---

## 🏋️ Training the Agent

Run:

```bash
python Ag.py FlappyBirdv0 --train
```

During training:

* Experiences are stored in replay memory.
* Mini-batches are sampled for learning.
* The target network is periodically synchronized.
* Best-performing models are saved automatically.

Saved model:

```text
runs/FlappyBirdv0.pt
```

---

## 🎮 Testing the Trained Agent

After training is complete:

```bash
python Ag.py FlappyBirdv0
```

The trained agent will play Flappy Bird using the learned policy.

---

## 📊 Hyperparameters

Example configuration from `parameter.yaml`:

```yaml
FlappyBirdv0:
  env_id: "FlappyBird-v0"
  epsilon_init: 1.0
  epsilon_decay: 0.995
  epsilon_min: 0.005
  replay_memory_size: 10000
  mini_batch_size: 32
  network_sync_rate: 10
  alpha: 0.001
  gamma: 0.99
  reward_threshold: 1000
```

---

## 🧠 Reinforcement Learning Concepts Used

### Deep Q-Network (DQN)

A neural network approximates the Q-value function:

Q(s,a)

allowing the agent to estimate the expected future reward for taking an action in a given state.

### Experience Replay

Past experiences are stored and randomly sampled during training, reducing correlation between consecutive samples.

### Target Network

A separate network is used to compute stable target Q-values, improving convergence.

### Epsilon-Greedy Strategy

The agent balances:

* Exploration → trying new actions
* Exploitation → using learned knowledge

---

## 📈 Future Improvements

* Double DQN
* Dueling DQN
* Prioritized Experience Replay
* PPO (Proximal Policy Optimization)
* Training Metrics Dashboard
* TensorBoard Integration

---

## 📸 Demo

Add screenshots or gameplay videos here.

Example:

```markdown
![Gameplay Demo](demo.gif)
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 👨‍💻 Author

**Saksham Badal**

GitHub: https://github.com/saksham966



---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.
