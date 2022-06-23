from django.shortcuts import render, redirect

from app.models import СommunicationModel


class Serializer:
    """control data"""

    def __init__(self, data: dict) -> None:
        self.data = data

    def control_types(self):
        """control type of data"""

        if type(self.data) != dict:
            return False

        # work with name
        if self.data.get('name', None) == None:
            return False

        if self.data.get('name') == '':
            return False

        # work with mail
        if self.data.get('mail', None) == None:
            return False

        if self.data.get('mail') == '':
            return False

        # work with phone
        if self.data.get('phone', None) == None:
            return False

        if self.data.get('phone') == '':
            return False

        # work with text
        if self.data.get('text', None) == None:
            return False

        if self.data.get('text') == '':
            return False

        return True

    def get_data(self):
        """get dict with mail, phone, text, name"""

        return {
            'name': str(self.data.get('name')),
            'phone': str(self.data.get('phone')),
            'mail': str(self.data.get('mail')),
            'text': str(self.data.get('text'))
        }


def get_page_connection(request):
    """get page with form"""

    return render(request, 'connection.html')


def set_data(request):
    """set mail"""

    # control data
    ser_obj = Serializer(dict(request.POST))
    if not ser_obj.control_types():
        return redirect('/app/connection')

    # get data
    data = ser_obj.get_data()
    СommunicationModel.objects.create(
        name=data.get('name'), 
        phone=data.get('phone'), 
        mail=data.get('mail'), 
        text=data.get('text')
    )

    return redirect('/app/connection')
