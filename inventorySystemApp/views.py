from django.shortcuts import render, HttpResponse


def login(request):

    return render(request, "inventorySystemApp/login.html")


def home(request):

    return render(request, "inventorySystemApp/home.html")


def receiving_items(request):

    return render(request, "inventorySystemApp/receivinf.html")


def inventory_management(request):

    return render(request, "inventorySystemApp/inventory.html")


def send_items(request):

    return render(request, "inventorySystemApp/outbound.html")

def dashboard(request):

    return render(request, "inventorySystemApp/dashboard_info.html")