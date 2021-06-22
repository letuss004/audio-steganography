import os
import wave
import argparse


def ex_msg(af):
    print("Please wait...")
    waveaudio = wave.open(af, mode='rb')
    frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
    msg = string.split("###")[0]
    print("Your Secret Message is: \033[1;91m" + msg + "\033[0m")
    waveaudio.close()

af = "output1.wav"
ex_msg(af)
