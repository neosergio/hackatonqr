from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from vote.models import Candidate


# Create your views here.
def index(request):
    done = request.COOKIES.get('already_voted', False)
    if not done:
        print "osea falso"
    if done:
        response = redirect('vote:results')
    else:
        candidate_list = Candidate.objects.all()
        context = {'candidate_list':candidate_list}
        response = render(request, 'vote/index.html', context)
    return response

def vote(request, id_candidate):
    done = request.COOKIES.get('already_voted', False)
    if done:
        response = redirect('vote:results')
    else:
        candidate = get_object_or_404(Candidate, pk=id_candidate)
        context = {'candidate':candidate}
        response = render(request, 'vote/vote.html', context)
    return response

def confirm_vote(request, id_candidate):
    done = request.COOKIES.get('already_voted', False)
    response = redirect('vote:results')
    if not done:
        candidate = get_object_or_404(Candidate, pk=id_candidate)
        candidate.votes += 1
        candidate.save()
        response.set_cookie(key="already_voted", value=True, max_age=60)
    return response

def result(request):
    first = Candidate.objects.get(name="Android")
    second = Candidate.objects.get(name="iOS")
    total = first.votes + second.votes
    first_percentage = float(first.votes) * 100 / total
    second_percentage = float(second.votes) * 100 / total
    context = {'first_percentage':first_percentage, 'second_percentage':second_percentage}
    return render(request, 'vote/results.html', context)