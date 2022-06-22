from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User
from first_app.forms import NewUserForm, FormName
# Create your views here.

def index(request):
  webpages_list = AccessRecord.objects.order_by('date')
  date_dict = {"access_records": webpages_list}
  return render(request, 'first_app/index.html', context = date_dict)

def help(request):
  return render(request, 'first_app/help.html')

def home(request):
  data = {"data": "this is shivam", "number":234.45, "date": "2022-10-23"}
  return render(request, 'first_app/home.html', context = data)

def form_name_view(request):
  form = FormName()
  if request.method == 'POST':
    form = forms.FormName(request.POST)
    if form.is_valid():
      print("validation success")
      print(form.cleaned_data['name'])
      print(form.cleaned_data['email'])
      print(form.cleaned_data['text'])
  return render(request, 'first_app/form_page.html', {'form':form})

def users(request):
  form = NewUserForm()
  if request.method == "POST":
    print("dnffbjk")
    form = NewUserForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return home(request)
    else:
      print("Error Form invalid")
  return render(request, 'first_app/users.html', {'form': form})
