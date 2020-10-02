from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'first_app/login_reg.html')

# LOGIN, REGISTER, AND LOGOUT
def login(request):
    logged_user = User.objects.filter(username=request.POST['username'])

    if logged_user[0]:
        if logged_user[0].password == request.POST['password']:
            request.session['user'] = logged_user[0].username
            request.session['id'] = logged_user[0].id

            print(logged_user)

            return redirect('/select_dog')
        
    else:
        return redirect('/')

def sign_up(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    if request.POST['password'] == request.POST['confirm_password']:
        new_user = User.objects.create(username=request.POST['username'], email=request.POST['email'], password = request.POST['password'])
        print('User Created')

        request.session['user'] = new_user.username
        request.session['id'] = new_user.id
        print('Session Started')


        return redirect('/add_dog')
    else:
        return redirect('/')
        
def logout(request):
    request.session.flush()
    return redirect('/')

# ADD DOG
def add_dog(request):
    return render(request, 'first_app/add_pet.html')

def add_new_dog(request):
    return render(request, 'first_app/add_new_dog.html')

def dog_added(request):
    if 'user' in request.session:
        dog_owner = User.objects.get(id=request.session['id'])
        errors = Dog.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add_dog')

        else:
            new_dog = Dog.objects.create(dog_name=request.POST['dog_name'], dog_size=request.POST['dog_size'], breed=request.POST['breed'], bio=request.POST['bio'], image=request.FILES['image'], dog_owner=dog_owner)

            request.session['dog'] = new_dog.id

            return redirect('/select_dog')

    else:
        return redirect("/")

def select_dog(request):
    one_user = User.objects.get(id=request.session['id'])
    all_dogs = one_user.my_dogs.all()

    context = {
        'dogs': all_dogs,
    }

    return render(request, 'first_app/select_dog.html', context)

def profile(request, dog_id):
    the_dog = Dog.objects.get(id=dog_id)

    request.session['dog'] = the_dog.id

    context = {
        'the_dog': the_dog
    }

    return redirect('/match')

def edit(request):
    the_user = User.objects.get(id=request.session['id'])
    all_dogs = the_user.my_dogs.all()

    context = {
        'user': the_user,
        'dogs': all_dogs,
    }

    return render(request, 'first_app/edit.html', context)

# UPDATE USERNAME
def update_username(request):
    the_user = User.objects.get(id=request.session['id'])

    context = {
        'user': the_user,
    }

    return render(request, 'first_app/update_username.html', context)

def username_action(request):
    the_user = User.objects.get(id=request.session['id'])
    the_user.username = request.POST['username']
    the_user.save()

    context = {
        'user': the_user,
    }

    return redirect('/edit')

# UPDATE EMAIL
def update_email(request):
    the_user = User.objects.get(id=request.session['id'])

    context = {
        'user': the_user,
    }

    return render(request, 'first_app/update_email.html', context)

def email_action(request):
    the_user = User.objects.get(id=request.session['id'])
    the_user.email = request.POST['email']
    the_user.save()

    context = {
        'user': the_user,
    }

    return redirect('/edit')

# UPDATE PASSWORD
def update_password(request):
    the_user = User.objects.get(id=request.session['id'])

    context = {
        'user': the_user,
    }

    return render(request, 'first_app/update_password.html', context)

def password_action(request):
    the_user = User.objects.get(id=request.session['id'])
    the_user.password = request.POST['password']
    the_user.save()

    context = {
        'user': the_user,
    }

    return redirect('/edit')

# EDIT DOG
def edit_dog(request, dog_id):
    the_dog = Dog.objects.get(id=dog_id)

    context = {
        'dog': the_dog,
    }

    return render(request, 'first_app/edit_dog.html', context)

def dog_updated(request, dog_id):
    the_dog = Dog.objects.get(id=dog_id)

    the_dog.dog_name = request.POST['dog_name']
    the_dog.dog_size = request.POST['dog_size']
    the_dog.breed = request.POST['breed']
    the_dog.bio = request.POST['bio']
    the_dog.image = request.FILES['image']
    the_dog.save()

    return redirect('/edit')


# DELETE DOG
def delete(request, dog_id):
    the_dog = Dog.objects.get(id=dog_id)
    the_dog.delete()

    return redirect('/edit')
