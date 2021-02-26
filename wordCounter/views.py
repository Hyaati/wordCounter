from django.http import HttpResponse
from django.shortcuts import render
import operator


def index(request):
    context = {
        'name': 'umar'
    }
    return render(request, 'index.html', context)


def count(request):
    text = request.GET['text']
    text_words = text.split()
    word_appearance = {}
    for text_word in text_words:
        if text_word in word_appearance:
            word_appearance[text_word] += 1
        else:
            word_appearance[text_word] = 1

    sorted_count = sorted(word_appearance.items(), key=operator.itemgetter(1), reverse=True)
    context = {
        'words_count': len(text_words),
        'text': text,
        'sorted_count': sorted_count
    }
    return render(request, 'count.html', context)
