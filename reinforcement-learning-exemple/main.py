import numpy as np
from environment import Maze
from agent import Agent
import matplotlib.pyplot as plt


if __name__ == '__main__':
    maze = Maze()
    robot = Agent(maze.maze, alpha=0.1, random_factor=0.25)
    moveHistory = []

    for i in range(5000):
        if i % 1000 == 0:
            print(i)

        while not maze.is_game_over():
            state, _ = maze.get_state_and_reward()
            action = robot.choose_action(state, maze.allowed_states[state])
            maze.update_maze(action)
            state, reward = maze.get_state_and_reward()
            robot.update_state_history(state, reward)
            if maze.steps > 1000:
                maze.robot_position = (5, 5)
        
        robot.learn() 
        moveHistory.append(maze.steps) 
        maze = Maze()

plt.semilogy(moveHistory, "b--")
plt.show()