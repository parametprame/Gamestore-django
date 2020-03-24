from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.my_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.my_logout, name='logout'),
    path('gamedetail/<int:num>/', views.gamedetail, name='gamedetail'),
    path('search/', views.game_search, name='search'),
    # path('usersearch/', views.usersearch, name='usersearch'),
    path('filter/', views.game_filter, name='filter'),
    path('profile/', views.profile, name='profile'),
    path('admin/nonregister/game/<int:num>/change/', views.game_modify, name="game_modify"),
    path('admin/nonregister/game/add/', views.add_game, name="add_game"),
    path('drop_game/<int:num>', views.drop_game, name="drop_game"),
    path('payment/<int:num>', views.payment, name="payment"),
    path('usergame/', views.usergame, name="usergame"),
    # path('gamedetailuser/<int:num>/', views.gamedetailuser, name='gamedetailuser'),
    path('afterpayment/<int:num>', views.afterpayment, name="afterpayment")
]
