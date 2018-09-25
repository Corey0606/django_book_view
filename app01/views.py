from django.shortcuts import render,HttpResponse,redirect
from app01.models import Author,Book,Publish
from django.http import JsonResponse

# Create your views here.
def research(request):
    if request.is_ajax():
        publish = request.POST.get('publish_session')
        book_list = Book.objects.filter(publish__name=publish)
        w = {}
        w['book_list']=book_list
        return JsonResponse(w)


def add_book(request):
    if request.method == 'POST':
        print(request)
        # print('1')
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get("publish_id")
        print('publish_id',publish_id)
        authors_id_list = request.POST.getlist("authors_id_list")
        book_obj = Book.objects.create(title=title,price=price,publishDate=pub_date,publish_id=publish_id)
        book_obj.author.add(*authors_id_list)
        return HttpResponse('success')
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    # print(1122121)
    return render(request, 'addbook.html',locals())


def search_book(request):
    if request.method == 'POST':
        publish_id = request.POST.get('publish_id', None)
        print('publish_id1', publish_id)
        if publish_id:
            print('publish_id2',publish_id)
            book_list = Book.objects.filter(publish=publish_id)
            return render(request,'search.html',locals())
        author_id = request.POST.get('author_id', None)
        print(author_id,'author_id1')
        if author_id:
            book_list = Book.objects.filter(author__nid=author_id)
            return render(request,'search.html',locals())
        return redirect('/books/search/')

    else:
        # print(1)
        book_list = Book.objects.all()
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request, 'book.html', locals())










def books(request):
    book_list = Book.objects.all()
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request, 'books.html',locals())


def delete_book(request,del_book_id):
    book_obj = Book.objects.filter(pk=del_book_id).delete()

    return redirect('/books/')


def change_book(request, change_book_id):
    edit_book_obj = Book.objects.filter(pk=change_book_id).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get("publish_id")
        authors_id_list = request.POST.getlist("authors_id_list")
        book_obj = Book.objects.filter(pk=change_book_id).update(title=title,price=price,publishDate=pub_date,publish_id=publish_id)
        edit_book_obj.author.set(authors_id_list)
        return redirect('/books/')
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()

    return render(request,'editbook.html',locals())
