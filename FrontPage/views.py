from django.shortcuts import render


# Create your views here.
def about_us(request):
    return render(request, 'FrontPage/AboutUs.html')


def terms_and_conditions(request):
    return render(request, 'FrontPage/TermsAndConditions.html')


def front_page(request):
    return render(request, 'FrontPage/FrontPage.html')
