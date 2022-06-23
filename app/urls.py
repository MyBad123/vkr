from django.urls import path

from app.views_main import get_main, set_mail
from app.views.shop_view import get_page_shop
from app.views.connection_view import get_page_connection, set_data
from app.views.faq_view import get_page_faq
from app.views.about_views import get_page_about

urlpatterns = [
    # main page
    path('main/', get_main),
    path('mail/', set_mail),

    # shop page
    path('shop/', get_page_shop),

    # about
    path('about/', get_page_about),

    # faq page
    path('faq/', get_page_faq),

    # connection page
    path('connection/', get_page_connection),
    path('connection-post/', set_data)
]


