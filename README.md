Signal Generation and Visualization
====================================

This project demonstrates a Python program to generate a modulated signal based on a mathematical formula and visualize it using a time-domain plot. The generated signal incorporates a carrier voltage, a carrier frequency, a signal frequency, and a modulation index. The program uses NumPy for signal calculations and Matplotlib for visualizations.

### Features

Signal Generation: The signal is generated based on the input values for carrier voltage, carrier frequency, signal frequency, and modulation index.
Signal Plotting: The generated signal is plotted against time for visualization purposes.

### Requirements

Python (version >= 3.6 recommended)
NumPy for efficient mathematical operations
Matplotlib for plotting the generated signal
You can install these libraries using pip:
pip install numpy matplotlib

Run the program by executing:

python signal.py
Input the required parameters when prompted:
Carrier Voltage (Vc) in volts
Carrier Frequency (Fc) in Hz
Signal Frequency (Fs) in Hz
Modulation Index (m)

Enter carrier voltage (Vc) in volts: 5
Enter carrier frequency (Fc) in Hz: 1000
Enter signal frequency (Fs) in Hz: 50
Enter modulation index (m): 0.7
Code Explanation
generate_signal(vc, fc, fs, m, t)
This function generates the modulated signal by calculating three main components:


![alt text](<WhatsApp Image 2024-11-04 at 9.31.18 AM-1.jpeg>)

term1: Represents the primary carrier signal
term2: Represents the lower sideband due to modulation
term3: Represents the upper sideband due to modulation
The final signal is the sum of these three terms:

signal = term1 + term2 + term3
main()
The main function:

Collects user inputs for Vc, Fc, Fs, and m
Defines a time array t for 0.01 seconds with 1000 samples
Generates the signal using generate_signal
Plots the generated signal against time
Sample Output
After entering your values, the program will display a plot with the modulated signal. The x-axis represents time in seconds, and the y-axis shows the signal's amplitude.

### License
This project is licensed under the MIT License.