from django.shortcuts import render


def content_list(request):
    return render(request, 'content/content_list.html', {})
