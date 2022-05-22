from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import UserInfo
from .forms import RegistrationForm, UserRegistrationInfoForm, UserInfoForm, UserForm


def register(request):
    if request.method == 'POST':  # 判断是发送表单还是载入页面
        user_form = RegistrationForm(request.POST)
        userinfo_form = UserRegistrationInfoForm(request.POST)
        if user_form.is_valid() and userinfo_form.is_valid():  # 判断是否能注册
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])  # 获取密码
            new_user.save()  # 保存☞数据库
            new_userinfo = userinfo_form.save(commit=False)
            new_userinfo.user = new_user
            new_userinfo.save()  # 保存☞数据库
            return HttpResponseRedirect(reverse('account:login'))
        else:
            return HttpResponse('抱歉，注册失败')
    else:
        user_form = RegistrationForm()
        userinfo_form = UserRegistrationInfoForm()
        return render(request, 'account/register.html', {'form': user_form, 'info': userinfo_form})  # 返回前端页面


@login_required()
def my_information(request):
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user,
                                                                  'userinfo') else UserInfo.objects.create(
        user=request.user)
    return render(request, 'account/my-information.html', {'user': request.user, 'userinfo': userinfo})


@login_required()
def edit_my_information(request):
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user,
                                                                  'userinfo') else UserInfo.objects.create(
        user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() and userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            request.user.email = user_cd['email']
            userinfo.birth = userinfo_cd['birth']
            userinfo.phone = userinfo_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.about_me = userinfo_cd['about_me']
            request.user.save()
            userinfo.save()
            return HttpResponseRedirect('/account/my-information')
    else:
        user_form = UserForm(instance=request.user)
        userinfo_form = UserInfoForm(
            initial={'birth': userinfo.birth, 'phone': userinfo.phone, 'school': userinfo.school,
                     'company': userinfo.company, 'profession': userinfo.profession, 'address': userinfo.address,
                     'about_me': userinfo.about_me})
        return render(request, 'account/edit_my_information.html',
                      {'user_form': user_form, 'userinfo_form': userinfo_form})

# Create your views here.
