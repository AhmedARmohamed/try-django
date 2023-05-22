from django.http import HttpResponse
name = "Justin"
HTML_STRING = f"""
<h1>Hello {name}</h1>
"""

def home_view(request):
    return HttpResponse(HTML_STRING)