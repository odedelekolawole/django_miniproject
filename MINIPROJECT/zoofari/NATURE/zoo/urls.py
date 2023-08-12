from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("base/", views.base, name="base"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("animals/", views.animals, name="animals"),
    path("visiting/", views.visiting, name="visiting"),
    path("membership/", views.membership, name="membership"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("error/", views.error, name="error"),
    path("contact/", views.contact, name="contact"),
    path("logout/", views.logout, name="logout"),
]