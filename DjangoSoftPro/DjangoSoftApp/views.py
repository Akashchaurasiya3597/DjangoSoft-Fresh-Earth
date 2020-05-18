from sched import scheduler

from django.shortcuts import render
from .models import FeedbackDatabase,ContactDatabase,VegetableDatabase,FruitsDatabase
from .forms import FeedbackForm,ContactForm
from django.http.response import HttpResponse
from django.contrib import messages


def index_View(request):
    return render(request, 'HtmlPages/index.html')

def Contact_View(request):
    if request.method == 'POST':
        Cform = ContactForm(request.POST)
        if Cform.is_valid():
            Name = Cform.cleaned_data.get('Name')
            Mobile_Number = Cform.cleaned_data.get('Mobile_Number')
            Email = Cform.cleaned_data.get('Email')
            courses = Cform.cleaned_data.get('courses')
            trainers = Cform.cleaned_data.get('trainers')
            locations = Cform.cleaned_data.get('locations')
            shifts = Cform.cleaned_data.get('shifts')
            gender = Cform.cleaned_data.get('gender')
            start_date = Cform.cleaned_data.get('start_date')
            data = ContactDatabase(
                Name=Name,
                Mobile_Number=Mobile_Number,
                Email=Email,
                courses=courses,
                trainers=trainers,
                locations=locations,
                shifts=shifts,
                gender=gender,
                start_date=start_date,
            )
            data.save()
            Cform = ContactForm()
            messages.success(request,'data saved')
            context = {'Cform': Cform}
            return render(request, 'HtmlPages/contact-us.html', context)

        else:
            messages.warning(request, 'Enter valid data')
    else:
        Cform = ContactForm()
    context = {'Cform':Cform}
    return render(request, 'HtmlPages/contact-us.html', context)

def Shop_Vegetable_View(request):
    Vegetable = VegetableDatabase.objects.all()
    Total_Vegetables = len(Vegetable)
    columns ='3'
    context = {'Vegetable':Vegetable,'Total_Vegetables':Total_Vegetables,'columns':columns}
    return render(request, 'HtmlPages/Shop-Vegetable.html', context)

def Shop_Fruit_View(request):
    Fruit = FruitsDatabase.objects.all()
    Total_fruits = len(Fruit)
    columns='3'
    context = {'Fruit':Fruit,'Total_fruits':Total_fruits,'columns':columns}
    return render(request, 'HtmlPages/Shop-Fruit.html', context)


def Feedback_View(request):
    if request.method == 'POST':
        Fform = FeedbackForm(request.POST)
        if Fform.is_valid():
            name = request.POST.get('name')
            ratting = request.POST.get('ratting')
            Feedback = request.POST.get('Feedback')
            data = FeedbackDatabase(
                name=name,
                ratting=ratting,
                Feedback=Feedback

            )
            data.save()
            messages.success(request,'data saved')
            Fform = FeedbackForm()
            Ffeedback = FeedbackDatabase.objects.all()
            context = {'Fform': Fform, 'Ffeedback': Ffeedback}
            return render(request, 'HtmlPages/Feedback.html', context)
        else:
            messages.warning(request, 'Invalid data')

    else:
        Fform = FeedbackForm()
        Ffeedback = FeedbackDatabase.objects.all()
        context = {'Fform': Fform , 'Ffeedback':Ffeedback}
        return render(request, 'HtmlPages/Feedback.html', context)


def Gallery_View(request):
    return render(request, 'HtmlPages/Gallery.html')

def My_account_View(request):
    return render(request, 'HtmlPages/my-account.html')


def Popularity_vegetable_view(request):
    Vegetable = VegetableDatabase.objects.filter(Category__istartswith='P')
    Total_Vegetables = len(Vegetable)
    columns = '3'
    context ={'Vegetable':Vegetable,'Total_Vegetables':Total_Vegetables,'columns':columns,}
    return render(request, 'HtmlPages/Shop-Vegetable.html', context)
def High_Low_vegetable_view(request):
    Vegetable = VegetableDatabase.objects.order_by('-Price')
    Total_Vegetables = len(Vegetable)
    columns = '3'
    context = {'Vegetable': Vegetable, 'Total_Vegetables': Total_Vegetables, 'columns': columns, }
    return render(request, 'HtmlPages/Shop-Vegetable.html', context)
def Low_High_vegetable_view(request):
    Vegetable = VegetableDatabase.objects.order_by('Price')
    Total_Vegetables = len(Vegetable)
    columns = '3'
    context = {'Vegetable': Vegetable, 'Total_Vegetables': Total_Vegetables, 'columns': columns, }
    return render(request, 'HtmlPages/Shop-Vegetable.html', context)
def BestSelling_vegetable_view(request):
    Vegetable = VegetableDatabase.objects.filter(Category__istartswith='B')
    Total_Vegetables = len(Vegetable)
    columns = '3'
    context = {'Vegetable': Vegetable, 'Total_Vegetables': Total_Vegetables, 'columns': columns, }
    return render(request, 'HtmlPages/Shop-Vegetable.html', context)

def Popularity_fruit_view(request):
    Fruit = FruitsDatabase.objects.filter(Category__istartswith='P')
    Total_fruits = len(Fruit)
    columns = '3'
    context ={'Fruit':Fruit,'Total_fruits':Total_fruits,'columns':columns,}
    return render(request, 'HtmlPages/Shop-Fruit.html', context)
def High_Low_fruit_view(request):
    Fruit = FruitsDatabase.objects.order_by('-Price')
    Total_fruits = len(Fruit)
    columns = '3'
    context = {'Fruit':Fruit,'Total_fruits':Total_fruits, 'columns': columns, }
    return render(request, 'HtmlPages/Shop-Fruit.html', context)
def Low_High_fruit_view(request):
    Fruit = FruitsDatabase.objects.order_by('Price')
    Total_fruits = len(Fruit)
    columns = '3'
    context = {'Fruit':Fruit,'Total_fruits':Total_fruits, 'columns': columns, }
    return render(request, 'HtmlPages/Shop-Fruit.html', context)
def BestSelling_fruit_view(request):
    Fruit = FruitsDatabase.objects.filter(Category__istartswith='B')
    Total_fruits = len(Fruit)
    columns = '3'
    context = {'Fruit':Fruit,'Total_fruits':Total_fruits, 'columns': columns, }
    return render(request, 'HtmlPages/Shop-Fruit.html', context)



def vegetables_detail_View(request,pk):
    vegetablesid = VegetableDatabase.objects.get(id=pk)
    Vegetable = VegetableDatabase.objects.all()
    context = {'vegetablesid':vegetablesid,'Vegetable':Vegetable}
    return render(request,'HtmlPages/vegetables-detail.html',context)

def fruits_detail_View(request,pk):
    fruitsid = FruitsDatabase.objects.get(id=pk)
    Fruit = FruitsDatabase.objects.all()
    context = {'fruitsid': fruitsid, 'Fruit': Fruit}

    return render(request,'HtmlPages/fruits-details.html',context)


def milks_detail_View(request):
    return render(request, 'HtmlPages/milks-details.html')

def about_us_View(request):
    return render(request, 'HtmlPages/about-us.html')


def Wish_list_View(request):
    return render(request, 'HtmlPages/Wishlist.html')


def Cart_view(request):
    return render(request, 'HtmlPages/cart.html')


def Checkout_view(request):
    return render(request, 'HtmlPages/checkout.html')


