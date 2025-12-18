from django.shortcuts import render


def about(request):
    """Функция, которая выводит страницу "О проекте"."""
    return render(request, 'pages/about.html')


def rules(request):
    """Функция, которая выводит страницу "Правила"."""
    return render(request, 'pages/rules.html')
