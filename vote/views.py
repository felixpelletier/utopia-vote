from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Sum, Count, Max

from models import Sujet, Poids, Vote, Periode

def logout(request):
    auth_logout(request)
    return redirect('/')


def login(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        return render(request, 'vote/login.html')


@login_required(login_url='/login/')
def resultats(request):
    periode = Periode.objects.all().aggregate(Max('debut')).get('debut__max')
    sujets = Sujet.objects
    sujets = sujets.filter(vote__date__gt=periode)
    sujets = sujets.annotate(score=Sum('vote__poids__poids'))
    sujets = sujets.annotate(num_votes=Count('vote'))
    sujets = sujets.order_by('-score')
    sujets = sujets.all()
    return render(request, 'vote/resultats.html', {'sujets': sujets})


@login_required(login_url='/login/')
def index(request):
    sujets = Sujet.objects
    # sujets = sujets.filter(vote__date__lt=datetime.now())
    sujets = sujets.order_by('nom')
    sujets = sujets.all()

    poids = Poids.objects
    poids = poids.order_by('ordre')
    poids = poids.all()

    render_params = {}
    render_params['sujets'] = sujets
    render_params['l_poids'] = poids

    if request.method == "POST":
        with transaction.atomic():
            Vote.objects.filter(usager=request.user).delete()
            votes_in = (entry for entry in request.POST.items()
                        if entry[0].isdigit())
            for poids_id, sujet_id in votes_in:
                sujet = Sujet.objects.get(id=sujet_id)
                poids = Poids.objects.get(id=poids_id)
                vote = Vote(usager=request.user, sujet=sujet, poids=poids)
                vote.save()

    return render(request, 'vote/index.html', render_params)
