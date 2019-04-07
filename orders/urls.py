from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("orders", views.orders, name="orders"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("<int:food_id>", views.food, name="food"),
    path("<int:food_id>/order", views.order, name="order"),
    path("<int:food_id>/set_Status", views.set_Status, name="status"),
    path("<int:user_id>/confirmOrder", views.confirmOrder, name="confirm"),
    path("<int:user_id>/card", views.card, name="card")
]
