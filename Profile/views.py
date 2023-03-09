from django.shortcuts import render
from Profile.models import Information, Education

# Create your views here.
def home(request):
    Information_obj = Information.objects.get(pk = 1)
    Education_obj = Education.objects.all()
    context = {
        "Info" : Information_obj,
        "Educ" : Education_obj
    }
    return render(request,'home.html',context = context)