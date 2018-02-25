from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.


def home(request):
    title = "Welcome"
    # if request.user.is_authenticated():
    #     title = "My Title %s" %(request.user)

    # add a form
    if request.method == "POST":
        print (request.POST)

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.full_name:
            instance.full_name = "Justin"
        instance.save()
        print(instance.email)
        print(instance.timestamp)

    context = {
        "title": title,
        "form": form
    }
    return render(request, "home.html", context)
