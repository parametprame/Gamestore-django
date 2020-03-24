from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from nonregister.models import Game, Image, Game_type, User_Game
from builtins import filter
from contextlib import redirect_stderr
from struct import error
from urllib import request
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
import random

# Create your views here

def homepage(request):
    game = Game.objects.all()
    gamety = Game_type.objects.all()
    img = Image.objects.all()

    return render (request, 'nonregister/homepage.html', context={'game': game, 'gamety' : gamety, 'img': img})

def my_login(request):
    context = {}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            # if user.is_superuser:
            #     print(user)
            #     return redirect('home')
            login(request, user)
            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:    
                return redirect('home')
        
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = "Wrong username or password!!!!!"
            return render(request, 'nonregister/login.html', context=context)
        pass
    else:
        return render(request, 'nonregister/login.html', context=context)

def register(request):
    context = {}
    if request.method == 'POST':
        # if User.objects.get(username=request.POST.get('username')):
        #     context = {
        #         'error': "กรุณาตั้ง username ใหม่",
        #         'sign_page': "sign_page"
        #     }
        #     return render(request, 'nonregister/register.html', context=context)
        # else:
        try:
            user = User.objects.create_user(
            first_name=request.POST.get('firstname'),
            last_name=request.POST.get('lastname'),
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('email')
            )
            group = Group.objects.get(name='User')
            user.groups.add(group)
            user.save()
            return redirect('login')
        except Exception as e:
            context['error'] = str(e)
        
    
    
    return render(request, 'nonregister/register.html')


def my_logout(request):
    logout(request)
    return redirect('home')

def gamedetail(request, num):

    game_pk = Game.objects.get(pk=num)
    img_pk = Image.objects.get(game_id=num)
    print(img_pk)
    context = {'game_pk' : game_pk,
                'img_pk' : img_pk
            }
    return render(request, 'user/gamedtail.html', context=context)

# def gamedetailuser(request, num):

#     game_pk = Game.objects.get(pk=num)
#     img_pk = Image.objects.get(game_id=num)
#     usergm = User_Game.objects.all()
#     print(img_pk)
#     context = {'game_pk' : game_pk,
#                 'img_pk' : img_pk,
#                 'usergm' :
#             }
#     return render(request, 'user/gamedtail.html', context=context)


def game_search(request):
    context = {}
    search = request.GET.get('search', '')
    game = Game.objects.filter(Q(name__icontains=search) | Q(developer__icontains=search))
    gamety = Game_type.objects.all()
    image = Image.objects.all()
    context = {'game': game, 'image': image, 'search': search, 'gamety' : gamety}
    return render(request, 'nonregister/homepage.html', context=context)

# def usersearch(request):
#     context = {}
#     search = request.GET.get('usersearch', '')
#     game = Game.objects.filter(Q(name__icontains=search) | Q(developer__icontains=search))
#     gamety = Game_type.objects.all()
#     image = Image.objects.all()
#     context = {'game': game, 'image': image, 'search': search, 'gamety' : gamety}
#     return render(request, 'user/usergame.html', context=context)

def game_filter(request):
    context = {}
    context['img'] = Image.objects.all()
    game_type = Game_type.objects.all()
    filters = {}
    for gt in game_type:
        filters.update({gt.id: request.GET.get(gt.type_name)})
        print(gt)
        print(filters)

    for ft in filters:
        game_type_id = filters.get(ft)
        if game_type_id == "on":
            context['gamety'] = Game_type.objects.filter(id=ft)
            context['game'] = Game.objects.filter(game_type_id_id=ft)
            context['gameall'] = Game_type.objects.all()
    return render(request, 'nonregister/filter.html', context=context)

def profile(request):
    return render(request, 'user/profileuser.html')

def game_modify(request):
    return HttpResponse('แก้ไขเกม')

def add_game(request):
    return HttpResponse('แอดเกม')

def drop_game(request, num):
    game = Game.objects.get(id=num)
    game.delete()
    return redirect('home')

def payment(request, num):
    game_pk = Game.objects.get(pk=num)
    img_pk = Image.objects.get(game_id=num)
    print(img_pk)
    context = {'game_pk' : game_pk,
                'img_pk' : img_pk
            }
    print(context)
    return render(request, 'user/payment.html', context=context)

def usergame(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        user = request.user.id
        game_search = User_games.objects.filter(
            user_id=user, game_id_id__name__icontains=search)
        image_search = Image.objects.all()

        context = {'games': game_search, 'images': image_search}
        return render(request, 'user/usergame.html', context=context)
    gamety = Game_type.objects.all()
    user = request.user.id
    game = User_Game.objects.filter(user_id=user)
    image = Image.objects.all()
    print("A: %s" %game)
    print("B: %s" %image)
    return render(request,
                  'user/usergame.html',
                  context={
                      'game': game,
                      'image': image,
                      'gamety': gamety
                  })

def afterpayment(request, num):
    user = request.user
    buy_game = Game.objects.get(pk=num)
    post = User_Game(user_id=user, game_id=buy_game ,serial='%32x' % random.getrandbits(16 * 8))
    print(post)
    post.save()
    return redirect('usergame')

# def game_filter(request):
#     if request.method == "POST":
#         click  = request.POST.get('allfilters')
#         alltype = Game_type.objects.all()
#         allgame = Game.objects.all()
#         allimage = Image.objects.all()
#         game7_adventure = Game.objects.filter(game_type_id=1)
#         image7_adventure = Image.objects.filter(game_id__game_type_id=1)
#         game6_action = Game.objects.filter(game_type_id=2)
#         image6_action = Image.objects.filter(game_id__game_type_id=2)
#         game5_simulation = Game.objects.filter(game_type_id=3)
#         image5_simulation = Image.objects.filter(game_id__game_type_id=3)
#         game4_rpg = Game.objects.filter(game_type_id=4)
#         image4_rpg = Image.objects.filter(game_id__game_type_id=4)
        
#         result = zip(allgame, allimage)
#         result7 = zip(game7_adventure, image7_adventure)
#         result6 = zip(game6_action, image6_action)
#         result5 = zip(game5_simulation, image5_simulation)
#         result4 = zip(game4_rpg, image4_rpg)

#         context = {
#                 'click':click,
#                 'result':result,
#                 'result7':result7,
#                 'result6':result6,
#                 'result5':result5,
#                 'result4':result4,
#                 'alltype':alltype

#         }
#         return render(request, 'nonregister/filter.html', context)

#     return render(request, 'nonregister/filter.html')
