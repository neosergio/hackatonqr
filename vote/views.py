from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from vote.models import Candidate


# Create your views here.
def index(request):
    candidate_list = Candidate.objects.all()
    context = {'candidate_list':candidate_list}
    return render(request, 'vote/index.html', context)

def vote(request, id_candidate):
    candidate = get_object_or_404(Candidate, pk=id_candidate)
    context = {'candidate':candidate}
    return render(request, 'vote/vote.html', context)

def confirm_vote(request, id_candidate):
    candidate = get_object_or_404(Candidate, pk=id_candidate)
    candidate.votes += 1
    candidate.save()
    return redirect('vote:results')

def result(request):
    first = Candidate.objects.get(name="Android")
    second = Candidate.objects.get(name="iOS")
    total = first.votes + second.votes
    first_percentage = float(first.votes) * 100 / total
    second_percentage = float(second.votes) * 100 / total
    context = {'first_percentage':first_percentage, 'second_percentage':second_percentage}
    return render(request, 'vote/results.html', context)