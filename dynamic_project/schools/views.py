from django.shortcuts import render
from .models import schools
from django.http import Http404

# Create your views here.
def list(request):
    all_school_data = schools.objects.all()
    return render(request, "schools/school_list.html", {"schools" : all_school_data})

def schoolDetails(request, pk):
    try:
        school_details = schools.objects.get(pk = pk)
    except schools.DoesNotExist:
        raise Http404("Note Does Not Exists")
    return render(request, 'schools/school_details.html', {'schoolDetails' : school_details})