from django.shortcuts import redirect, render
from django.db.models import Q
from .models import MailingListUser

# Create your views here.


def MailingListAddView(request):
    if request.POST:
        full_name, email, where_found = (
            request.POST["full-name"],
            request.POST["email"],
            request.POST["where-found"],
        )

        try:
            MailingListUser.objects.get(Q(full_name=full_name) | Q(email=email))
        except MailingListUser.DoesNotExist:
            MailingListUser.objects.create(
                full_name=full_name, email=email, where_found=where_found
            )
            request.session["email"] = email
            return redirect("home")
        else:
            return redirect("home")
    else:
        return redirect("home")


def MailingListRemoveView(request):
    email = request.session["email"]
    if email:
        try:
            user = MailingListUser.objects.get(Q(email=email))
        except MailingListUser.DoesNotExist:
            return redirect("home")
        else:
            user.delete()
            return redirect("home")
