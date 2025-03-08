from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404,render
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def profile_list_view(request):
    context= {
        "object_list":User.objects.filter(active=True)
    }
    return render(request,"profiles/list.html",context)

@login_required
def profile_view(request,username=None,*args,**kwargs):
    user = request.user
    #profile_user_obj =  User.objects.get(username=username)
    profile_user_obj = get_list_or_404(User,username=username)
    is_me = profile_user_obj == user
    if is_me:
        if user.has_permision('visits.view_pagevisit'):
            #qs = PageVisit.object.all()
            pass
    return HttpResponse(f"Hello there {username} - {profile_user_obj.id} - {user.id} - {is_me}")

