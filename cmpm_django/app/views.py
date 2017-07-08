from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
'''from .models import Post'''

class index(TemplateView):
	template_name = 'app/index.html'
	
class items(TemplateView):
	template_name = 'app/items.html'	
	context = 'app/items.html'
	context_instance = 'app/items.html'

'''return render_to_response(template='items.html', context, context_instance)'''

'''def index(request):
	return render(request, 'index.html', {})'''