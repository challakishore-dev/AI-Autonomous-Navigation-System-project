import matplotlib.pyplot as plt
import numpy as np
import os
import imageio

def show_path(grid, path, start, goal):
    os.makedirs("images", exist_ok=True)

    data = np.array(grid.grid)

    fig, ax = plt.subplots()
    ax.imshow(data, cmap='gray_r')

    px = [p[1] for p in path]
    py = [p[0] for p in path]

    ax.scatter(start[1], start[0], color='green')
    ax.scatter(goal[1], goal[0], color='red')

    frames = []

    for i in range(len(path)):
        ax.plot(px[:i+1], py[:i+1], color='blue')

        fig.canvas.draw()

        img = np.array(fig.canvas.renderer.buffer_rgba())
        img = img[:, :, :3]

        frames.append(img)

    # Save static image
    plt.savefig("images/02_output_path.png")

    # Save GIF animation
    imageio.mimsave("images/03_animated_path.gif", frames, fps=5)

    plt.close()