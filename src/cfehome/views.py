import pathlib
from django.shortcuts import render
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request,*args,**kwargs):
    my_title = "My page"
    my_context = {
        "page_title": my_title
    }
    html_template = "home.html"
    return render(request,html_template,context=my_context)


def home_old_page_view(request,*args,**kwargs):
    html_ = ""
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()

    return HttpResponse(html_)
