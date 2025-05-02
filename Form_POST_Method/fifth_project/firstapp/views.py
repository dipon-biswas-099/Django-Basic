from django.shortcuts import render

# Create your views here.
def home(request):
    name =''
    email=''
    if request.method == 'POST':
        name = request.POST.get('userName')
        email = request.POST.get('userEmail')
        rating = request.POST.get('rating')
        return render(request,'first_app/home.html' ,{'name':name , 'email':email , 'rating':rating})
    else:
        return render(request,'first_app/home.html' )

def submit_form(request):
    return render(request, 'first_app/form.html')

