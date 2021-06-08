# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import keywords_extraction
import keywords_comparator

def get_corpus():
    text = []

    for i in range(2, 10):
        with open('./text_data/log_audio_source_' + str(i+1) + '.txt', encoding='utf-8') as fin:
            text.append(fin.read())

    return text

def get_pres_text():
    with open('test_prez', encoding='utf-8') as fin:
        pres_text = fin.read()
    return pres_text

def get_audio_text():
    with open('test_noize_audio', encoding='utf-8') as fin:
        pres_text = fin.read()
    return pres_text

if __name__ == '__main__':
    texts = get_corpus()
    corpus = keywords_extraction.Corpus(texts)

    all_voice_words = corpus.get_words_with_metrics(get_audio_text())
    all_prez_words  = corpus.get_words_with_metrics(get_pres_text())

    print('Транскрипция выступления: ', keywords_extraction.Corpus.normalize(all_voice_words))
    print('Презентация: ', keywords_extraction.Corpus.normalize(all_prez_words))

    kw = keywords_comparator.KeywordsComparator(all_voice_words, all_prez_words)
    print(kw.simple_compare_dict())

    print(kw.compare_dict(0.4, 0.3))

