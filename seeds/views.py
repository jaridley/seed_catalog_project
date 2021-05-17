from django.shortcuts import render


def enter_seeds(request):
    return render(request, 'enter_seeds.html', {})
