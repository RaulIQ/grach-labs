import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000  # частота дискретизации
seconds = 5  # длительность записи
print("Начинаем запись...")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='float32')
sd.wait()
write('my_audio.wav', fs, myrecording)
print("Запись сохранена как my_audio.wav")