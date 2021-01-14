from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from plays.models import Play
# Create your views here.
def write_review(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            play = request.POST.get('play')
            the = Play.objects.get(pk=play)

            content = request.POST.get('content')
            review = Review.objects.create(play=the, user=request.user, content=content)
            review.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html', {'form': form})
def success(request,pk=None, *args, **kwargs):
    pass

    context ={


    }

    return render(request, "reviews/review_success.html", context)
