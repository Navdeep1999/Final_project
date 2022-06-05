import json
from sre_constants import BRANCH
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from st_app.models import Degree, Students
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .forms import DegreeForm
from .forms import StudentsForm

    

clicked = 0
def first(request):
    
    return render(request,'first.html')

def game1(request):
    
    return render(request,'game1.html')

def game2(request):
    
    return render(request,'game2.html')

def index(request) :  
    global clicked
    clicked =  clicked + 1;
    degree_values = Degree.objects.all()
    student_values = Students.objects.all()

    my_dict = { 'inject_var' : clicked, "data" : ['apple', 'orange' 'mango', 'grapes', 'lemon'], 'name' : 'Navdeep', 'degree_rows' : degree_values,'student_rows' : student_values}
    
    return render(request,'index.html',context=my_dict)

def help(request):
    
    return render(request,'help.html')
   
def  get_degree(request):
    
    if request.method == 'POST':
        form = DegreeForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            branch = form.cleaned_data['branch']
            
            d = Degree(title=title, branch=branch)
            d.save()
            
            
                
            return HttpResponseRedirect('/nform/')
    else:
        form =  DegreeForm()
        
        return render(request, 'nform.html', {'form': form})


def get_student(request):
    
    if request.method == 'POST':
        form = StudentsForm(request.POST, request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            roll_number=form.cleaned_data['roll_number']
            year=form.cleaned_data['year']
            dob=form.cleaned_data['dob']
            
            s= Students(name=name, roll_number=roll_number, year=year, dob=dob)
            s.save()
            
            
            
                    
            return HttpResponseRedirect('/nform2/')
    else:
        form = StudentsForm()
        
        return render(request, 'nform2.html', {'form1': form})                

def output(request):
    student_values = Students.objects.all()
    
    my_dict = { 'Students_rows' : student_values}
    form=Searchforms()
    form
    return render(request, 'form_search.html', context=my_dict,)


class Searchforms(TemplateView):
    template_name = 'form_search.html'

class SearchResultsView(ListView):
    model = Students
    template_name = 'result_search.html'
    
    def get_queryset(self):
        
        query = self.request.GET.get("q")
        object_list = Students.objects.filter(Q(name__icontains=query) | Q(dob__icontains=query))
        
        return object_list
        