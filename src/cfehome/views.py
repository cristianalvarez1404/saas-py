import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request,*args,**kwargs):
    """ qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My page"
    html_template = "home.html"
    
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent":(page_qs.count() * 100) / qs.count(),
        "total_visit_count":qs.count()
    }

    PageVisit.objects.create(path=request.path)
    
    return render(request,html_template,context=my_context) """
    if request.user.is_authenticated:
        print(request.user.is_authenticated,request.user,request.user.first_name)
    return render(request,*args,**kwargs)


def about_view(request,*args,**kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100) / qs.count(),
    except:
        percent = 0

    my_title = "My page"
    html_template = "home.html"
    
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent":percent,
        "total_visit_count":qs.count()
    }

    PageVisit.objects.create(path=request.path)
    
    return render(request,html_template,context=my_context)


def home_old_page_view(request,*args,**kwargs):
    html_ = ""
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()

    return HttpResponse(html_)
