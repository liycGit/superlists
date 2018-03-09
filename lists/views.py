from django.shortcuts import redirect,render
from django.http import HttpResponse
from lists.models import Item,List


# Create your views here.
# home_page = None
"""
def home_page():
    pass
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')

def home_page(request):
    return render(request, 'home.html')
	
def home_page(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])       

    return render(request, 'home.html')

def home_page(request):
    return render(request, 'home.html',{
		'new_item_text':request.POST.get('item_text',''),
	})

#5.7节
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    return render(request, 'home.html')

#5.8节
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

#6.5节
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')
"""
#6.6.3节
def home_page(request):
    return render(request, 'home.html')

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
	#return redirect('/lists/the-only-list-in-the-world/')
    #return render(request, 'home.html')
	
def view_list(request,list_id):
	list_ = List.objects.get(id=list_id)
	items = Item.objects.filter(list=list_)
	return render(request, 'list.html', {'list': list_,'items': items})
	
def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))


