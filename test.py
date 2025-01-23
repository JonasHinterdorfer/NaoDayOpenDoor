from STT import STT

def main():
    stt = STT()
    transcription = stt.transcribe_audio()
    print("Transcription:", transcription)

if __name__ == "__main__":
    main()