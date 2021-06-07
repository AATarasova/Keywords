# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import keywords_extraction
import keywords_comparator

def get_corpus():
    text = []

    for i in range(0, 10):
        with open('./text_data/log_audio_source_' + str(i+1) + '.txt', encoding='utf-8') as fin:
            text.append(fin.read())

    return text

def get_pres_text():
    with open('./parsed_pdf_data/' + str(1) + '_merge.txt', encoding='utf-8') as fin:
        pres_text = fin.read()
    return pres_text


if __name__ == '__main__':
    texts = get_corpus()
    corpus = keywords_extraction.Corpus(texts)

    all_voice_words = corpus.get_words_with_metrics()
    all_prez_words  = corpus.get_words_with_metrics()

    print(all_voice_words, all_prez_words, sep='\n' )
    kw = keywords_comparator.KeywordsComparator(all_voice_words, all_prez_words)
    print(kw.simple_compare_dict())

    print(kw.compare_dict(level_audio=0.3, level_prezentation=0.21))

