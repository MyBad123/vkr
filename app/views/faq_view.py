from django.shortcuts import render

from app.models import QuestionModel


def get_page_faq(request):
    """get page with questions"""

    # get data from QuestionModel model
    data = []
    for i in QuestionModel.objects.all():
        data.append({
            'req': i.question,
            'res': i.responce
        })

    return render(request, 'faq.html', context={
        'data': data
    })
