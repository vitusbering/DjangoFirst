from django.shortcuts import render
from post. models import Post
from post. models import Author

menu = ["About post", "Add information", "Feedback", "Enter"]

def post_page(request):
    #return HttpResponse('Page of application Post')
    return render(request, 'post/home.html', {'menu': menu, 'Title': 'Main page of post'})

def add(request):
    get_author = Author.objects.get(name='Andrey')
    result = Post(title='My first blog', body='Hello Im doing my first blog',author=get_author)
    result.save()
    return render(request, 'add.html', {'Title': 'Add post', 'Variable_title': result.title, 'Variable_body':
                                        result.body})

def delete(request):
    get_author = Author.objects.get(name='Charles')
    get_author.delete()
    return render(request, 'add.html', {'Title': 'Detete author', 'Variable': get_author.name})