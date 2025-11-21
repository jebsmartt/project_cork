# pages/views.py

from django.shortcuts import render


def home_page_view(request):
    """
    Renders the 'pages/home.html' template file.
    The 'render' shortcut automatically finds the template 
    and returns an HttpResponse containing its content.
    """
    # The first argument is the request object.
    # The second argument is the path to the template, relative to the 
    # templates directory defined in the settings.
    return render(request, 'pages/index.html')

def class_options_view(request):
    # This renders the new template (we'll create this next)
    return render(request, 'pages/class_options.html')