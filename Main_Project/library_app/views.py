from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect, HttpResponse
from .models import Books

import logging
# Create your views here.
logging.basicConfig(filename = "loggerfile_library.log", level = logging.DEBUG,
                    format = "%(asctime)s:  %(message)s:  %(levelname)s: %(funcName)s :%(name)s")


def login_page(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_superuser:
                auth.login(request, user)
                request.session["username"] = user.username
                logging.debug('User is added into the system')
                return render(request, 'library_app/Homepage.html')
            else:
                request.session["username"] = user.username
                logging.debug('User is present into the system')
                return render(request, 'library_app/Homepage.html')
        else:
            messages.info(request, 'Invalid User')
            logging.debug('Invalid User')
            return render(request,'library_app/login_page.html')
    else:
        return render(request, 'library_app/login_page.html')


def log_out(request):
    del request.session['username']
    auth.logout(request)
    logging.debug('User has logout from the system')
    return render(request, 'library_app/login_page.html')

def home(request):
    return render(request, 'library_app/Homepage.html')

def add_book(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        book_author = request.POST['book_author']
        book_type = request.POST['book_type']
        book_price = request.POST['book_price']
        print(book_name ,book_author,book_price,book_type)
        book = Books(book_name = book_name, book_author = book_author, book_type = book_type, book_price = book_price)
        book.save()
        messages.info(request, 'Book is Add into the list')
        logging.debug('addeded to the list')
        return render(request, 'library_app/Homepage.html')

    else:
        return render(request, 'library_app/Add_book.html')

def update_book(request):
    if request.method == 'POST':
        b_name = request.POST['book_name']
        info = request.POST['info']
        values = request.POST['book']
        if Books.objects.filter(book_name=b_name).exists():
            books = Books.objects.get(book_name=b_name)
            if 'bookname' in values:
                books.book_name = info
                books.save()
                messages.info(request, 'Book Updated')
                return render(request, 'library_app/Homepage.html')
            elif 'bookauthor' in values:
                books.book_author = info
                books.save()
                messages.info(request, 'Book Updated')
                return render(request, 'library_app/Homepage.html')
            elif 'booktype' in values:
                books.book_type = info
                books.save()
                messages.info(request, 'Book Updated')
                return render(request, 'library_app/Update_book.html')
            elif 'bookprice' in values:
                books.book_price = info
                books.save()
                messages.info(request, 'Book Updated')
                return render(request, 'library_app/Update_book.html')
            else:
                messages.info(request, 'Book Not Updated')
                return render(request, 'library_app/Update_book.html')
        else:
            messages.info(request, 'Book Not Present for update')
            return render(request, 'library_app/Homepage.html')
    else:
        return render(request, 'library_app/Update_book.html')

def search_book(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        if Books.objects.filter(book_name=book_name).exists() :
           allbooks = Books.objects.filter(book_name=book_name)
           logging.debug('Book is present the list')
           return render(request, 'library_app/Search_book.html', {'res':allbooks})
        else:
            messages.info(request, 'Book is Not Available in the library_app')
            logging.debug('Book is not in the list')
            return render(request, 'library_app/Homepage.html')
    else:
        return render(request, 'library_app/Search_book.html')


def delete_book(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        if Books.objects.filter(book_name = book_name).exists():
            allbooks = Books.objects.filter(book_name = book_name)
            allbooks.delete()
            messages.info(request, 'Book is Deleted')
            logging.debug('Book is deleted from list')
            return render(request, 'library_app/Delete_book.html')
        else:
            messages.info(request, 'Book is Not Available')
            logging.debug('Book is not present in the list')
            return render(request, 'library_app/Homepage.html')
    else:
        return render(request, 'library_app/Delete_book.html')

def view_book(request):
    books = Books.objects.all()
    logging.debug('list of books')
    return render(request, 'library_app/View_book.html', {'Books': books})


def register(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['user']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken.')
                logging.debug('User is registered')
                return render(request, 'library_app/Register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken.')
                logging.debug('User mail is added into the system')
                return render(request, 'library_app/Register.html')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=fname, last_name=lname)
                user.save()
                print('User created')
                logging.debug('User is Created')
                return render(request, 'library_app/login_page.html')
        else:
            messages.info(request, "Password not matching")
            logging.debug('User is password is incorrect')
            return render(request, 'library_app/Register.html')
    else:
        return render(request, 'library_app/Register.html')
