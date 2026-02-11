from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_home')
    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.all().order_by('-created_at')[:5]
    return render(request, 'user_data/home.html', {'form': form, 'feedbacks': feedbacks})
