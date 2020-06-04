from django.shortcuts import render

# Create your views here.
def index(request):
    index_dict = {
        'index':'Inserted in Index Page by Django'
    }
    return render(request,'basic_app/index.html',context=index_dict)

def other(request):
    other_dict = {
        'other':'Inserted in Other page by Django'
    }
    return render(request,'basic_app/other.html',context=other_dict)

def relative(request):
    relative_dict = {
        'relative':'Inserted in Relative page by Django'
    }
    return render(request,'basic_app/relative.html',context=relative_dict)