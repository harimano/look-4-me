from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')

def login_index(request):
    return render(request, 'login/index.html')

def register(request):    
    return redirect(getQuestionnaireForm)

def getQuestionnaireForm(request):
    return render(request, 'login/questionnaire.html')

def login(request):
    return redirect('/../dating/')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['myfile']
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)
        print(uploaded_file.name)
        print(uploaded_file.size)
        print(fs.url(file_name))
    return render(request, 'login/index.html', {"uploaded_file_url": fs.url(file_name)})