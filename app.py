import tempfile
from pydub import AudioSegment
import json

PDF_HEX_START = ['25', '50', '44', '46']
SECONDS_PER_MINUTE = 60
BYTES_PER_MEGABYTE = 1024 * 1024


# def file_has_pdf_beginning(file):
#     for i in range(len(PDF_HEX_START)):
#         if file.read(1).hex() != PDF_HEX_START[i]:
#             file.seek(0)
#             return False
#     file.seek(0)
#     return True


def convert_from_mp3_to_wav(audio, frame_rate=8000, channels=1):
    sound = AudioSegment.from_mp3(audio) \
        .set_frame_rate(frame_rate) \
        .set_channels(channels)
    temp_file = tempfile.NamedTemporaryFile()
    sound.export(temp_file.name, format="wav")
    return temp_file


class RecognizedAudio:
    def __init__(self, recognized_words):
        self.recognized_words = recognized_words

    def __repr__(self):
        return json.dumps({
            'recognized_words': [repr(recognized_word) for recognized_word in self.recognized_words]
        }, ensure_ascii=False)

    @staticmethod
    def from_json_file(json_file):
        json_obj = json.load(json_file)
        json_recognized_words = json_obj['recognized_words']
        recognized_words = [
            RecognizedWord.from_json_string(json_recognized_word) for json_recognized_word in json_recognized_words
        ]
        return RecognizedAudio(recognized_words)


class RecognizedWord:
    def __init__(self, word, begin_timestamp, end_timestamp, probability):
        self.word = word
        self.begin_timestamp = begin_timestamp
        self.end_timestamp = end_timestamp
        self.probability = probability

    def __repr__(self):
        return json.dumps({
            'word': repr(self.word),
            'begin_timestamp': self.begin_timestamp,
            'end_timestamp': self.end_timestamp,
            'probability': self.probability
        }, ensure_ascii=False)

    @staticmethod
    def from_json_string(json_string):
        json_obj = json.loads(json_string)
        return RecognizedWord(
            Word.from_json_string(json_obj['word']),
            float(json_obj['begin_timestamp']),
            float(json_obj['end_timestamp']),
            float(json_obj['probability']),
        )


class Word:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return json.dumps({
            'value': self.value
        }, ensure_ascii=False)

    @staticmethod
    def from_json_string(json_string):
        json_obj = json.loads(json_string)
        return Word(value=json_obj['value'])
