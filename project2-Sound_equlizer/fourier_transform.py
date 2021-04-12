from scipy.fft import rfft, rfftfreq , irfft
import numpy as np

def fourier(data ,gain) :
    signal = np.array(10 * [None])
    new_signal = []
    data = np.array(data)
    ft = rfft(data)
    yf = np.abs(ft)
    k, m = divmod(len(yf), 10)
    for i in range(10):
            signal[i] = yf[i * k + min(i, m):(i + 1) * k + min(i + 1, m)]
            signal[i] = signal[i] * gain[i]
            new_signal = new_signal + list(signal[i])
    new_signal = np.array(new_signal)
    modified= np.multiply(new_signal, np.exp(1j*np.angle(ft)))    
    output_signal = irfft(modified)
    return output_signal , yf
