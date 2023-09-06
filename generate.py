import numpy as np 
from scipy.io import wavfile
import numpy as np
from itertools import permutations

def generate_primes(n):
  primes = [2]
  num = 3
  
  while len(primes) < n:
    is_prime = True
    for p in primes:
      if num % p == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(num)
    num += 2
  
  return primes

def generate_frequencies(base_freq, n_harmonics):
  primes = generate_primes(n_harmonics)
  
  freqs = [base_freq * p for p in primes]
  
  return freqs

base_freq = 440
n_harmonics = 7
frequencies = generate_frequencies(base_freq, n_harmonics)
print(frequencies)

#permutations_list = list(permutations(frequencies))

#print(permutations_list)
permutations_list = [list(permutation) for permutation in permutations(frequencies)]


fs = 44100 # sampling rate


def generate_song(frequencies):
    n_steps = 10  # Number of steps for decreasing amplitudes
    t = np.linspace(0, 1, 30000)  # Time values

    # Generate the waveform
    waveform = np.zeros_like(t)
    for i, freq in enumerate(frequencies):
        start_amplitude = 1.0
        end_amplitude = 0.1
        amplitudes = np.linspace(start_amplitude, end_amplitude, n_steps)
    
        for j, amplitude in enumerate(amplitudes):
            waveform += amplitude * np.sin(2 * np.pi * freq * t)

    name = "_".join(map(str,frequencies))
    wavfile.write(f'samples/harmonics_{name}.wav', fs, waveform)
    #find -name \*.wav -exec python -m  encodec {} --force {}

for frequencies in permutations_list:
    generate_song(frequencies) #print(
