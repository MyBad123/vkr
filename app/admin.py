from django.contrib import admin
from .models import (
    ProductModel, ProductPhotoModel, 
    QuestionModel, MailModel, –°ommunicationModel
)

admin.site.register(ProductModel)
admin.site.register(ProductPhotoModel)
admin.site.register(QuestionModel)
admin.site.register(MailModel)
admin.site.register(–°ommunicationModel)
