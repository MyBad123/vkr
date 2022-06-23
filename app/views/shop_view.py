from django.shortcuts import render
from app.models import ProductModel, ProductPhotoModel


def get_page_shop(request):
    """get page with shop"""

    # get all items
    items = []
    for i in ProductModel.objects.all():
        photos = ProductPhotoModel.objects.filter(product=i)

        if len(photos) != 0:
            items.append({
                'name': i.name,
                'price': i.price, 
                'number': i.number,
                'about': i.about,
                'id': i.id,
                'photo': str(photos[0].photo)
            })

    print(items)

    return render(request, 'shop.html', context={
        'items': items
    })
