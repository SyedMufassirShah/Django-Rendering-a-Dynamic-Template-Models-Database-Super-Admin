from django.shortcuts import render
from .models import schools

# Create your views here.
def list(request):
    all_school_data = schools.objects.all()
    return render(request, "schools/school_list.html", {"schools" : all_school_data})