# from dpasteapp.forms import LoginForm, SignUpForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.views import View
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
#
#
# def logout_user(request):
#     logout(request)
#     return redirect('login')
#
#
# class SignUpController(View):
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('dpastelists')
#
#         signup_form = SignUpForm()
#         context = {
#             'title' : 'Sign up',
#             'form' : signup_form,
#             'error' : kwargs.get('error')
#         }
#         return render(request, 'signup.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(**form.cleaned_data)
#             user.save()
#             user = authenticate(
#                 request,
#                 username = form.cleaned_data['username'],
#                 password = form.cleaned_data['password']
#             )
#             if user:
#                 login(request, user)
#                 return redirect('dpastelists')
#             else:
#                 messages.error(request, "Error in signing up for dPaste")
#         return redirect('signup.html', **{'error' : True})
#
#
# class LoginController(View):
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('dpastelists')
#
#         login_form = LoginForm()
#         context = {
#             'title' : 'Login Page',
#             'form' : login_form
#         }
#         return render(request, 'login.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#
#         if form.is_valid():
#             user = authenticate(**form.cleaned_data)
#             if user:
#                 login(request, user)
#                 return redirect('dpastelists')
#             else:
#                 messages.error(request, 'Error in Logging into dPaste')
#         return redirect('login', **{'error' : True})








from dpasteapp.forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def logout_user(request):
    logout(request)
    return redirect('login')


class SignUpController(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dpastelists')

        signup_form = SignUpForm()
        context = {
            'title' : 'Sign up',
            'form' : signup_form,
            'error' : kwargs.get('error')
        }
        # return render(request, 'signup.html', context)
        return render(request, 'login_signup.html', context)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('dpastelists')
            else:
                messages.error(request, "Error in signing up for dPaste")
        # return redirect('signup.html', **{'error' : True})
        return render(request, 'login_signup.html', {'form': form})


class LoginController(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dpastelists')

        login_form = LoginForm()
        context = {
            'title' : 'Login Page',
            'form' : login_form
        }
        return render(request, 'login_signup.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)
                return redirect('dpastelists')
            else:
                messages.error(request, 'Error in Logging into dPaste')
        #return redirect('login', **{'error' : True})
        return redirect('login')
        #return render(request, 'login_signup.html')