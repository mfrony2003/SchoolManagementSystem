from django_xhtml2pdf.views import PdfMixin

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required






@login_required
def admindashboard(request):   
        return render(request,'admin/admin.html' )  

