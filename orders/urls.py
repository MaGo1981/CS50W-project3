from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("orders", views.orders, name="orders"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("food/<int:food_id>", views.food, name="food"),
    path("food/<int:food_id>/order", views.order, name="order"),
    path("food/<int:food_id>/set_Status", views.set_Status, name="status"),
    path("user/<int:user_id>/confirmOrder", views.confirmOrder, name="confirm"),
    path("food/<int:food_id>/addtopping", views.addTopping, name="addTopping"),
    path("user/<int:user_id>/card", views.card, name="card")
]
