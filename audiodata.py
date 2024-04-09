import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

def plot_sound_file(filename):

    data, samplerate = sf.read(filename)
    # Reads the sound file using the 'sf.read()' function.
    # 'data' contains the audio samples, and 'samplerate' is the sampling rate.

    time = np.arange(0, len(data)) / samplerate
    # Creates an array 'time' representing the time axis.
    # The length of the array is determined by the number of audio samples.
    # The division by 'samplerate' converts sample indices to time in seconds

    rms = np.sqrt(np.mean(data ** 2))
    # Calculates the root mean square (RMS) of the audio samples.
    # RMS represents the average energy of the signal.
    
    dbfs = 20 * np.log10(rms / 1.0) 
    # Converts the RMS value to decibels relative to full scale (dBFS).
    # dBFS is commonly used to measure audio levels.
    # The reference level here is 1.0 (maximum amplitude).

 
    plt.figure(figsize=(10, 5))
    plt.plot(time, data, color='b')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Sound Waveform')
    plt.grid(True)

 
    plt.text(0.05, 0.95, f'DBFS: {dbfs:.2f} dB', transform=plt.gca().transAxes, ha='left', va='top', color='red')

    plt.show()


filename = "output.wav" 
plot_sound_file(filename)
