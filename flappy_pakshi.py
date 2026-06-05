import gymnasium as gym
import flappy_bird_gymnasium
import pygame

# Creating env
env = gym.make("FlappyBird-v0", render_mode="human")

state, info = env.reset()

pygame.init()

done = False

while not done:

    action = 0  # 0 = no flap, 1 = flap

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                action = 1

    state, reward, terminated, truncated, info = env.step(action)

    done = terminated or truncated

    env.render()

env.close()
pygame.quit()