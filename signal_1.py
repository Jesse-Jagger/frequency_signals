import numpy as np
import matplotlib.pyplot as plt

# this function is to generate the signal based on the given formula
def generate_signal(vc, fc, fs, m, t):
    term1 = vc * np.sin(2 * np.pi * fc * t)
    term2 = (m / 2) * vc * np.cos(2 * np.pi * (fc - fs) * t)
    term3 = -(m / 2) * vc * np.cos(2 * np.pi * (fc + fs) * t)
    return term1 + term2 + term3

# Main function for user input and visualization
def main():
    vc = float(input("Enter carrier voltage (Vc) in volts: "))
    fc = float(input("Enter carrier frequency (Fc) in Hz: "))
    fs = float(input("Enter signal frequency (Fs) in Hz: "))
    m = float(input("Enter modulation index (m): "))

    # Time array for plotting
    t = np.linspace(0, 0.01, 1000)  # 0.01 seconds duration

    # Generate the signal
    v = generate_signal(vc, fc, fs, m, t)

    # Plot the signal
    plt.figure(figsize=(12, 6))
    plt.plot(t, v, label="Generated Signal")
    plt.title("Generated Signal Based on Given Formula")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()