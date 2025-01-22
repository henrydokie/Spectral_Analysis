# Spectral Analysis and Animation

This repository contains a Python program for performing spectral analysis on a generated dataset and visualizing the results. The application dynamically plots the time-domain signal, its frequency-domain representation, and allows users to interactively select and animate frequency components in the time domain.

## Features

- **Signal Generation**: Generates a sine wave signal with optional noise.
- **Spectral Analysis**: Performs Fast Fourier Transform (FFT) to analyze the signal in the frequency domain.
- **Interactive Frequency Selection**: Allows users to click on frequency points to visualize corresponding time-domain components.
- **Animation**: Animates the combined waveform of selected frequency components dynamically in the time domain.
- **Customizable**: Modify parameters like signal frequency, sampling rate, and duration for experimentation.

## Prerequisites

Ensure you have Python installed, along with the following libraries:

- `numpy`
- `matplotlib`
- `scipy`

You can install these dependencies using:

```bash
pip install numpy matplotlib scipy
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/spectral-analysis.git
   cd spectral-analysis
   ```

2. Run the script:

   ```bash
   python spectral_analysis.py
   ```

3. Interact with the plots:
   - Click on points in the frequency domain plot to select or deselect frequency components.
   - Click the "Play" button to animate the selected components in the time domain.

## File Structure

- **`spectral_analysis.py`**: The main Python script for signal generation, spectral analysis, and visualization.
- **`README.md`**: This file, providing an overview of the project.

## How It Works

1. **Signal Generation**:
   - A sine wave with optional noise is generated based on specified frequency, sampling rate, and duration.

2. **FFT Analysis**:
   - The script calculates the FFT of the signal to identify its frequency components.

3. **Interactive Selection**:
   - Users can click on points in the frequency domain plot to select/deselect components.
   - The corresponding time-domain waveform is displayed in the third plot.

4. **Animation**:
   - The "Play" button animates the combined waveform of selected components, showing oscillation over time.

## Example

When you run the script, you'll see:

- **Original Signal**: The generated sine wave in the time domain.
- **Frequency Spectrum**: The FFT results, showing the magnitude of frequency components.
- **Selected Components**: Visualization of selected frequency components.

![Example Screenshot](example_screenshot.png)  

## Future Improvements

- Add support for loading custom datasets.
- Enhance animation smoothness.
- Add functionality for saving plots and animations.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy analyzing! 🎉

