import numpy as np 
from scipy.io import wavfile
import numpy as np
from itertools import permutations
import pprint
import random

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
n_harmonics = 3
frequencies = generate_frequencies(base_freq, n_harmonics)
#print(frequencies)

#permutations_list = list(permutations(frequencies))

#print(permutations_list)
permutations_list = [list(permutation) for permutation in permutations(frequencies)]


fs = 44100 # sampling rate

def generate_song(frequencies, n_steps=10):

    seconds = 30
    t = np.linspace(0, 10, seconds * fs)  # 10 seconds of audio
    waveform = np.zeros_like(t)
    
    for sec in range(seconds):
        freq = random.choice(frequencies)  + random.choice(frequencies)  + random.choice(frequencies)  
        amplitude = 1.0
        
        waveform_sec = amplitude * np.sin(2 * np.pi * freq * t[sec * fs : (sec + 1) * fs])
        #print(waveform_sec )
        waveform[sec * fs : (sec + 1) * fs] = waveform_sec
    
    name = "_".join(map(str, frequencies))
    wavfile.write(
      f'samples/2harmonics_{name}.wav',
      fs,
      waveform)
    with open( f"samples/2harmonics_{name}.debug","w") as fo:
      fo.write(str(waveform))
    
# Generate songs with stacked components
for frequencies in permutations_list:
    generate_song(frequencies)
