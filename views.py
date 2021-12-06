from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from member.models import Living,Death
from member.form import Living_form
def add_to_living(request):
    if request.method=="POST":
        form=Living_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member:add_to_living')
    form=Living_form()
    context= {'form':form}
    return render(request,'members/add_to_living.html',context)


def add_to_death(request):
    if request.method=="POST":
        death=Death()
        adhar_no=request.POST['aadhar']
        reason=request.POST['reason']
        living=Living.objects.get(adharcard_no=adhar_no)
        death.name=living.name
        death.adharcard_no=living.adharcard_no
        death.email=living.email
        death.adderss=living.adderss
        death.phone_no=living.phone_no
        death.image=living.image
        death.life=False
        death.reason=reason
        living.delete()
        death.save()
        return redirect('member:add_to_death')
        # return HttpResponse("success")
    return render(request,'members/input.html')

def living_list(request):
    living=Living.objects.all()
    context={'living':living}
    return render(request,'members/living_list.html',context)

def death_list(request):
    death=Death.objects.all()
    context={'death':death}
    return render(request,'members/death_list.html',context)

def index(request):
    return render(request,'members/index.html') 

