from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        context = {
            'all_dogs': Dog.objects.all(),
        }
        return render(request, 'second_app/match.html', context)

# def dislike(request, dog_id):
#     return redirect('/match')

# def like(request, dog_id):
#     Like.objects.create(dog_liked=Dog.objects.get(id=dog_id), liker=Dog.objects.get(id=request.session['dog']))
#     print('Yay you made a pal!')

#     if len(Like.objects.filter(liker = Dog.objects.get(id=dog_id))) > 0:
#         print('Success')
#         return render(request, 'second_app/message.html')
#     else:
#         return redirect('/match')


# MESSAGE A DOG
def message(request, dog_id):
    the_user = User.objects.get(id = request.session['id'])

    my_dog = Dog.objects.get(id = request.session['dog'])
    the_dog = Dog.objects.get(id = dog_id)

    context = {
        'the_dog': the_dog,
        'my_dog': my_dog
    }

    return render(request, 'second_app/message.html', context)

def message_action(request):
    if 'user' in request.session:
        user_message = User.objects.get(id=request.session['id'])
        errors = Message.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/message")

        else: 
            new_message = Message.objects.create(message = request.POST['message'], user_message=user_message)
            
            context = {
                'message': new_message,
            }

            return redirect('/message', context)
    else:
        return redirect('/message')

