import numpy as np
from scipy.io import wavfile
from scipy import signal

duration = 12 
sample_rate = 44100
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Гармоническая част
f1 = 440  
f2 = 880  
harmonic_part = 0.5 * np.sin(2 * np.pi * f1 * t) + \
               0.3 * np.sin(2 * np.pi * f2 * t)

# Перкуссионная часть
percussion_part = np.zeros_like(t)
for _ in range(32):
    idx = np.random.randint(0, len(t))
    impulse = signal.windows.gaussian(200, std=50)
    start = max(0, idx - 100)
    end = min(len(t), idx + 100)
    impulse = impulse[:end-start]
    percussion_part[start:end] += 0.7 * impulse

audio_signal = harmonic_part + percussion_part
audio_signal = audio_signal / np.max(np.abs(audio_signal))
wavfile.write(r'Lab1\random_noise.wav', sample_rate, (audio_signal * 32767).astype(np.int16))