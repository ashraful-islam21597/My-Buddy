
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse

from .models import Profile, status, friend, notification,coverphotos,profilephotos


def signin(request):
    if 'SignUp' in request.POST:
        name = request.POST['name']
        contact = request.POST['contact']
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                u = Profile(name=name, contact=contact, username=username, email=email, password=password)

                u.save()
                f = friend.objects.create(name=name, contact=contact, username=username, email=email)
                f.save()
                print('p')
                q = auth.authenticate(username=username, password=password)
                auth.login(request, q)
                return redirect('/')

            except:

                messages.info(request, "usernametaken")
                return render(request, "account.html")
        else:

            return render(request, 'account.html')
    if 'Login' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        q = auth.authenticate(username=username, password=password)

        if q is not None:
            auth.login(request, q)
            return redirect('/')
        else:

            return render(request, "account.html")

    else:
        return render(request, 'account.html')

def profile(request):
    if request.user is not None and request.user.is_authenticated:
        s1 = []
        p2 = []
        a2 = []
        f1 = []
        q=get_object_or_404(Profile,username=request.user.username)
        p = coverphotos.objects.filter(userpic__id=q.id)
        s = Profile.objects.all()
        q1 = get_object_or_404(friend, pk=q.id)
        x = q1.user.add(q)
        x = q1.user.all()
        stat = status.objects.order_by('-updated_at')
        if x:
            for i in x:
                a = coverphotos.objects.filter(userpic__id=i.id)

                f1.append(i.id)
            s1 = status.objects.filter(user__id__in=f1).order_by('-updated_at')

        if 'editprofile' in request.POST:
            return HttpResponseRedirect(reverse('blog:editprofile', args=(id,)))

        elif 'profile' in request.POST:
            return render(request, 'profile.html', {'q': q})
        elif 'Logout' in request.POST:
            auth.logout(request)
            return redirect("/signin/")

        elif 'add' in request.POST:
            posts = request.POST['post']
            pro = status(user_id=q.id,post=posts)
            pro.save()
            return redirect('/')
        elif 'uploadtimelinephoto' in request.POST:
            caption = request.POST['caption']
            timelinepic = request.FILES['timelineimage'];
            pro = status(user_id=q.id,caption=caption,timeline_pic=timelinepic)
            pro.save()
            return redirect('/')

        elif 'friend' in request.POST:
            return HttpResponseRedirect(reverse('blog:addfriend', args=(q.id,)))

        elif  'save' in request.POST:
            job=request.POST['job']
            present_address=request.POST['presentaddress']
            permanent_address=request.POST['permanentaddress']
            q.job=job
            q.present_address=present_address
            q.permanent_address=permanent_address
            q.save()
            return redirect('/')

        elif 'search' in request.POST:
            print('h')
            search = request.POST['s']
            s = Profile.objects.filter(name__icontains=search).first()
            s1 = Profile.objects.get(username=s)
            print(s1.name)

            return HttpResponseRedirect(reverse('blog:friendprofile', args=(s1.username,)))

        elif 'upload' in request.POST:

            pic = request.FILES['image'];
            sta = status(user_id=q.id,profile_pic=pic)
            sta.save()
            u = profilephotos(userpic_id=q.id,profile_pic=pic)
            q.profilepicture=pic
            q.save()

            u.save()
            print(pic)
            return redirect('/')

        else:

                return render(request, 'home.html', context={
                        'q': q,
                        's': s,
                        'stat': stat,
                        'x': x,
                        's1':s1,
                        })
    else:
        return HttpResponseRedirect('/signin/')
def friendprofile(request,username):
    if request.user is not None and request.user.is_authenticated:
        q=Profile.objects.get(username=username)
        return render(request, 'profile.html', {'q': q})
    else:
        return HttpResponseRedirect('/signin/')
def home(self):
    return redirect('/')

def logout(request):
    q=Profile.objects.get(username=request.user.username)
    if q is not None and request.user.is_authenticated:
        auth.logout(request)
        return HttpResponseRedirect('/signin/')
    else:
        return HttpResponseRedirect('/signin/')

def addfriend(request):
    if request.user is not None and request.user.is_authenticated:
        stat = status.objects.all

        q=Profile.objects.get(username=request.user.username)
        p = get_object_or_404(friend, pk=q.id)
        x=p.user.all()

        s = Profile.objects.all()

        print('authenticated')
        if 'back' in request.POST:
            return redirect('/')
        if request.method == 'POST':
            q1 = Profile.objects.get(username=request.POST['k'])
            q2 = get_object_or_404(Profile, pk=q1.id)
            p.user.add(q2)
            x = p.user.all()

            message = "sent you a friend request"
            q3 = notification(fr_id=q1.id, ins=q.username, message=message)
            q3.save()
            return render(request, 'friends.html', context={'s': s,'q':q,'x':x})

        else:
            return render(request, 'friends.html', context={'s': s,'q':q,'x':x})
    else:
        return redirect('/signin/')

def note(request):
    if request.user is not None and request.user.is_authenticated:
        q=Profile.objects.get(username=request.user.username)
        p = get_object_or_404(friend, pk=q.id)
        x1=p.user.all()
        j=0
        for i in x1:
            j+=1
        print(j)
        if request.method == "POST":
            q1 = Profile.objects.get(username=request.POST['i'])
            q2 = get_object_or_404(Profile, pk=q1.id)
            p.user.add(q2)
            x = p.user.all()

            message = "accepted your friend request"
            q3 = notification(fr_id=q1.id, ins=q.name, message=message)
            q3.save()
            j -= 1

            return redirect('/')
        else:
            return render(request, 'notification.html', {'q': q})
    else:

        return redirect('/signin/')





