import wave


def em_audio(af, string, output):
    print("Please wait...")
    waveaudio = wave.open(af, mode='rb')
    frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
    string = string + int((len(frame_bytes) - (len(string) * 8 * 8)) / 8) * '#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)
    with wave.open(output, 'wb') as fd:
        fd.setparams(waveaudio.getparams())
        fd.writeframes(frame_modified)
    waveaudio.close()
    print("Done...")


af = "Demo.wav"
string = "hello"
output = "output1.wav"
em_audio(af, string, output)
