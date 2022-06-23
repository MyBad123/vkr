from django.shortcuts import render


def get_page_about(request):
    """about page"""

    return render(request, 'about.html')
