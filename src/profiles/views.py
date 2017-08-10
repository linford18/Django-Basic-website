from django.shortcuts import render ,redirect
from django.conf import settings
from forms import profileForm

from django.core.files.storage import FileSystemStorage

from models import Document
from forms import DocumentForm
# Create your views here.
def home(request):
	context = {}
	template ='home.html'
	return render(request,template,context)

def profile(request):
	form =profileForm(request.POST or None)
	context={'form':form}
	if form.is_valid():
		first_name=form.cleaned_data['first_name']
		last_name=form.cleaned_data['last_name']
		done=True
		context={'first_name':first_name,'last_name':last_name,'done':done}
	template='profile.html'



	return render(request,template,context)

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'profile.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'profile.html')