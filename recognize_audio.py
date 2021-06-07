import asyncio
import json
import wave

import websockets

import app
from playground.noise_reduction.denoiser import Denoiser


class VoskAudioRecognizer(app.AudioRecognizer):
    def __init__(self, host):
        self.host = host

    def parse_recognizer_result(self, recognizer_result):
        return app.RecognizedWord(
            word=app.Word(recognizer_result['word']),
            begin_timestamp=recognizer_result['start'],
            end_timestamp=recognizer_result['end'],
            probability=recognizer_result['conf'],
        )

    def recognize_wav(self, audio):
        recognizer_results = asyncio.get_event_loop().run_until_complete(
            self.send_audio_to_recognizer(audio.name)
        )
        recognized_words = list(map(self.parse_recognizer_result, recognizer_results))
        return app.RecognizedAudio(recognized_words)

    def recognize(self, audio):
        temp_wav_file = app.convert_from_mp3_to_wav(audio)
        Denoiser.process_wav_to_wav(temp_wav_file, temp_wav_file, noise_length=3)
        return self.recognize_wav(temp_wav_file)
