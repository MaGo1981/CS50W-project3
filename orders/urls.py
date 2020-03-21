from django.urls import path

from . import views1, views2, apiViews1

urlpatterns = [
    path("", views1.index, name="index"),
    path("v1/menu", views1.menu, name="menu"),
    path("orders", views1.orders, name="orders"),
    path("register", views1.register_view, name="register"),
    path("login", views1.login_view, name="login"),
    path("logout", views1.logout_view, name="logout"),
    path("food/<int:food_id>", views1.food, name="food"),
    path("food/<int:food_id>/order", views1.order, name="order"),
    path("food/<int:food_id>/set_Status", views1.set_Status, name="status"),
    path("user/<int:user_id>/confirmOrder", views1.confirmOrder, name="confirm"),
    path("food/<int:food_id>/addtopping", views1.addTopping, name="addTopping"),
    path("food/<int:food_id>/addpasta", views1.addPasta, name="addPasta"),
    path("user/<int:user_id>/card", views1.card, name="card"),
    path("user/<int:user_id>/profile", views1.profile, name="profile"),
    path("api/v1/food", apiViews1.FoodView.as_view(), name="foodApi"),
    path("api/v1/toppings", apiViews1.ToppingsView.as_view(), name="toppingsApi"),
    path("api/v1/pizzas", apiViews1.PizzasView.as_view(), name="pizzasApi"),
    path('api/v1/pizzas/<int:pk>', apiViews1.SinglePizzaView.as_view(), name="singlePizaView"),
    path("api/v2/pizzas/", apiViews1.PizzaList.as_view(), name="pizzasApi2"),
    path("v2/item/<int:item_id>", views2.item, name="item"),
    path("v2/menu", views2.v2menu, name="v2menu"),
    path("item/<int:item_id>/additem", views2.addItem, name="addItem"),
    path("v2/user/<int:user_id>/card", views2.itemsCard, name="itemsCard"),

]
