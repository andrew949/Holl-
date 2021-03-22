from django.shortcuts import render
from django.http import HttpResponse

from .models import Hall
# Create your views here.


def show_hall_by_pk_view(request):
    """Returns halls """
    hall = request.POST.get('hall_id')
    hall_pk = hall
    hall_obj = Hall.objects.get(pk=hall_pk)
    con = {'hall': hall_obj}
    return render(request, template_name="refs/hall.html", context=con)
