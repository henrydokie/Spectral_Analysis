import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.fft import fft, ifft, fftfreq

# Function to generate a dataset (a simple sine wave with noise)
def generate_dataset(freq=5, sampling_rate=100, duration=2):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)  # Time axis
    signal = np.sin(2 * np.pi * freq * t) + 0.5 * np.random.normal(size=t.shape)  # Sine wave with noise
    return t, signal

# Function to perform spectral analysis
def spectral_analysis(signal, sampling_rate):
    N = len(signal)  # Number of samples
    yf = fft(signal)  # Compute the FFT
    xf = fftfreq(N, 1 / sampling_rate)[:N // 2]  # Frequency axis

    # Take the absolute value to get the magnitude
    magnitude = np.abs(yf[:N // 2])
    return xf, magnitude, yf

# Function to reconstruct individual frequency components
def reconstruct_components(yf, selected_indices, N):
    components = []
    for i in selected_indices:
        single_component = np.zeros(len(yf), dtype=complex)
        single_component[i] = yf[i]
        single_component[-i] = yf[-i]  # Conjugate for symmetry
        components.append(ifft(single_component).real)
    return components

# Function to handle clicks on the frequency domain
def on_click(event, xf, yf, t, components_ax, highlight_points, selected_indices):
    if event.inaxes:
        x_mouse = event.xdata
        if x_mouse is not None:
            # Find the nearest point
            idx = (np.abs(xf - x_mouse)).argmin()

            if idx in selected_indices:
                # Remove the point if already selected
                selected_indices.remove(idx)
            else:
                # Add the point if not already selected
                selected_indices.append(idx)

            # Reconstruct the selected frequency components
            selected_components = reconstruct_components(yf, selected_indices, len(t))

            # Update the components plot
            components_ax.clear()
            for i, component in enumerate(selected_components):
                components_ax.plot(t, component, label=f"Freq {xf[selected_indices[i]]:.2f} Hz")
            components_ax.set_title("Selected Components")
            components_ax.set_xlabel("Time (s)")
            components_ax.set_ylabel("Amplitude")
            components_ax.legend()

            # Update the highlighted points
            highlight_points.set_offsets([[xf[i], np.abs(yf[i])] for i in selected_indices])
            highlight_points.set_visible(len(selected_indices) > 0)
            event.canvas.draw_idle()

# Function to animate the selected components in the time domain
def animate_components(t, components_ax, selected_indices, yf):
    combined_wave = sum(reconstruct_components(yf, selected_indices, len(t))) if selected_indices else np.zeros_like(t)

    def update(frame):
        components_ax.clear()
        # Oscillate the wave dynamically by shifting its phase
        phase_shift = 2 * np.pi * frame / len(t)
        oscillating_wave = combined_wave * np.cos(phase_shift)
        components_ax.plot(t, oscillating_wave, label="Animated Wave", color="yellow")
        components_ax.set_title("Animated Components")
        components_ax.set_xlabel("Time (s)")
        components_ax.set_ylabel("Amplitude")
        components_ax.legend()
        return components_ax.lines

    return update

# Main function
if __name__ == "__main__":
    # Parameters
    freq = 5  # Frequency of the sine wave in Hz
    sampling_rate = 100  # Sampling rate in Hz
    duration = 2  # Duration in seconds

    # Generate dataset
    t, signal = generate_dataset(freq=freq, sampling_rate=sampling_rate, duration=duration)

    # Perform spectral analysis
    xf, magnitude, yf = spectral_analysis(signal, sampling_rate)

    # Set up dark background
    plt.style.use('dark_background')

    # Plot the original signal
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    axes[0].plot(t, signal, label="Original Signal", color="cyan")
    axes[0].set_title("Generated Signal")
    axes[0].set_xlabel("Time (s)")
    axes[0].set_ylabel("Amplitude")
    axes[0].legend()

    # Plot the spectral analysis as a dot plot
    scatter = axes[1].scatter(xf, magnitude, label="Magnitude", color="red")
    axes[1].set_title("Spectral Analysis")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Magnitude")
    axes[1].legend()

    # Set up the components plot
    axes[2].set_title("Selected Components")
    axes[2].set_xlabel("Time (s)")
    axes[2].set_ylabel("Amplitude")

    # Initialize selected indices and highlight points
    selected_indices = []
    highlight_points = axes[1].scatter([], [], color="yellow", s=100, zorder=3, visible=False)

    # Connect the click event
    fig.canvas.mpl_connect("button_press_event", lambda event: on_click(event, xf, yf, t, axes[2], highlight_points, selected_indices))

    # Add a play button for animation
    from matplotlib.widgets import Button

    def start_animation(event):
        if selected_indices:
            ani = FuncAnimation(fig, animate_components(t, axes[2], selected_indices, yf), frames=200, interval=50, blit=False)
            plt.show()

    play_ax = plt.axes([0.8, 0.02, 0.1, 0.04])  # Position for the play button
    play_button = Button(play_ax, "Play")
    play_button.on_clicked(start_animation)

    plt.tight_layout()
    plt.show()
