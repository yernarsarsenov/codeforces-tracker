from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import HandleForm
from . import services
from datetime import datetime

def index(request):
    if request.method == 'POST':
        form = HandleForm(request.POST)
        if form.is_valid():
            handle = form.cleaned_data['handle']
            return redirect('profile', handle=handle)
    else:
        form = HandleForm()
    return render(request, 'tracker/index.html', {'form': form})

def profile(request, handle):
    user_info = services.get_user_info(handle)
    if not user_info:
        messages.error(request, f"User '{handle}' not found or Codeforces API is currently unavailable.")
        return redirect('index')

    rating_history = services.get_user_rating_history(handle)
    submissions = services.get_user_submissions(handle)
    
    solved_stats, solved_problems = services.get_solved_stats(submissions)
    
    current_rating = user_info.get('rating')
    recommendations = services.get_recommendations(handle, current_rating, solved_problems)

    # Process submissions for display (recent 20)
    recent_submissions = []
    if submissions:
        for sub in submissions[:20]:
            sub_time = datetime.fromtimestamp(sub['creationTimeSeconds']).strftime('%Y-%m-%d %H:%M')
            recent_submissions.append({
                'id': sub['id'],
                'problem': sub['problem'],
                'verdict': sub.get('verdict', 'UNKNOWN').replace('_', ' ').title(),
                'raw_verdict': sub.get('verdict', 'UNKNOWN'),
                'language': sub['programmingLanguage'],
                'time': sub_time
            })

    context = {
        'user': user_info,
        'rating_history': rating_history,
        'recent_submissions': recent_submissions,
        'solved_stats': solved_stats,
        'recommendations': recommendations,
    }
    return render(request, 'tracker/profile.html', context)
