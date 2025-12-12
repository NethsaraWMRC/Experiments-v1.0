import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def plot_loss(losses):
    """Plot the training loss over epochs"""
    plt.figure(figsize=(10, 5))
    plt.plot(losses, linewidth=2, color='blue')
    plt.xlabel('Epoch', fontsize=12)
    plt.ylabel('Loss (MSE)', fontsize=12)
    plt.title('Training Loss Over Time', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.yscale('log')  # Log scale for better visualization
    plt.tight_layout()
    plt.show()

def animate_learning(x, y, predictions):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Add padding at the top for title
    fig.subplots_adjust(top=0.92)
    
    ax.plot(x, y, label="True function", linewidth=2.5, color='blue', alpha=0.7)
    line, = ax.plot([], [], label="NN Prediction", color="red", linewidth=2.5)
    ax.legend(fontsize=11)
    
    # Set fixed axis limits to prevent rescaling
    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()
    y_range = y_max - y_min
    ax.set_xlim(x_min - 0.1, x_max + 0.1)
    ax.set_ylim(y_min - 0.5 * y_range, y_max + 0.5 * y_range)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.grid(True, alpha=0.3)

    def update(frame):
        pred = predictions[frame]
        # Clip predictions to prevent extreme values
        pred_clipped = np.clip(pred, y_min - 2*y_range, y_max + 2*y_range)
        line.set_data(x, pred_clipped)
        ax.set_title(f"Training Progress - Epoch {frame + 1}/{len(predictions)}", fontsize=14, fontweight='bold', pad=20)
        return line,

    ani = FuncAnimation(fig, update, frames=len(predictions), interval=100, repeat=True, blit=False)
    plt.show()
