# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import keywords_extraction
import keywords_comparator


def get_corpus():
    text = []

    for i in range(2, 10):
        with open('./text_data/log_audio_source_' + str(i + 1) + '.txt', encoding='utf-8') as fin:
            text.append(fin.read())

    return text


def get_pres_text():
    with open('a_merge.txt', encoding='utf-8') as fin:
        pres_text = fin.read()
    return pres_text


def get_audio_text():
    with open('skiba_transcription', encoding='utf-8') as fin:
        pres_text = fin.read()
    return pres_text


if __name__ == '__main__':
    texts = get_corpus()
    corpus = keywords_extraction.Corpus(texts)

    l_pres = 0.3
    l_voice = 0.4

    all_voice_words = corpus.get_words_with_metrics(get_audio_text())
    all_prez_words = corpus.get_words_with_metrics(get_pres_text())
    print(len(all_voice_words))
    print(len(all_prez_words))

    kw_voice = keywords_extraction.Corpus.choose_keywords(all_voice_words, level=l_voice)
    kw_pres = keywords_extraction.Corpus.choose_keywords(all_prez_words, level=l_pres)

    print(len(kw_pres))

    print('Презентация: ', keywords_extraction.Corpus.normalize(kw_pres).keys())
    print('Транскрипция выступления: ', keywords_extraction.Corpus.normalize(kw_voice).keys())
    print('Транскрипция выступления: ', len(keywords_extraction.Corpus.normalize(kw_voice).keys()))

    simple = keywords_comparator.KeywordsComparator(audio_keywords=kw_voice, presentation_keywords=kw_pres)

    kw = keywords_comparator.KeywordsComparator(all_voice_words, all_prez_words)

    print('Пороговое значение для транскрипции: ', l_voice)
    print('Простое сравнение ', simple.simple_compare_dict())
    print('Алгоритм без стемминга ', kw.compare_dict_without_stemming(level_audio=l_voice, level_prezentation=l_pres))
    print('Алгоритм со стеммингом ', kw.compare_dict(level_audio=l_voice, level_prezentation=l_pres))
