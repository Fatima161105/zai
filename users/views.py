from django.shortcuts import render


def profile(request):
    context={
        'title': 'Home-Кабинет'
    }
    return render(request,'users/profile.html', context)

