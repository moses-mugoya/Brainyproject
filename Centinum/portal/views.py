from django.shortcuts import render, redirect, get_object_or_404
from .forms import BusinessForm, IdeaForm
from .models import Ideas, StartupBusiness, IdeaInvestments, BusinessInvestments, BusinessTeams, IdeaTeams
from django.contrib.auth.decorators import login_required
from .decorators import innovator_required, investor_required, entrepreneur_required
from account.models import Profile


def index(request):
    return render(request, 'portal/index.html')


@login_required
def home(request):
    ideas = Ideas.objects.filter(personal=False)
    ideas_count = Ideas.objects.filter(personal=False).count()
    return render(request, 'portal/home.html', {'ideas': ideas, 'ideas_count': ideas_count})


@login_required
def home_biz(request):
    startup = StartupBusiness.objects.filter(personal=False)
    startup_count = StartupBusiness.objects.filter(personal=False).count()
    return render(request, 'portal/home_biz.html', {'startup': startup, 'startup_count': startup_count})


@investor_required
@login_required
def investor(request):
    startup = StartupBusiness.objects.all()
    startup_count = StartupBusiness.objects.count()
    return render(request, 'portal/investor.html', {'startup': startup, 'startup_count': startup_count})


@investor_required
@login_required
def investor_idea(request):
    ideas = Ideas.objects.all()
    ideas_count = Ideas.objects.count()
    return render(request, 'portal/investor_idea.html', {'ideas': ideas, 'ideas_count': ideas_count})


@innovator_required
@login_required
def innovator(request):
    ideas = Ideas.objects.filter(user=request.user)
    ideas_count = Ideas.objects.filter(user=request.user).count()
    return render(request, 'portal/innovator.html', {'ideas': ideas, 'ideas_count': ideas_count})


@entrepreneur_required
@login_required
def entrepreneur(request):
    startup = StartupBusiness.objects.filter(user=request.user)
    startup_count = StartupBusiness.objects.count()
    return render(request, 'portal/entrepreneur.html', {'startup': startup, 'startup_count': startup_count})


def business_detail(request, id):
    business = get_object_or_404(StartupBusiness, id=id)
    investors = business.invest_business.filter(approved=True)
    investors_count = business.invest_business.filter(approved=True).count()
    return render(request, 'portal/business_detail.html', {'business': business, 'investors': investors, 'investors_count': investors_count})


def idea_detail(request, id):
    idea = get_object_or_404(Ideas, id=id)
    user_profile = get_object_or_404(Profile, user=request.user)
    investors = idea.invest_idea.filter(approved=True)
    investors_count = idea.invest_idea.filter(approved=True).count()
    return render(request, 'portal/idea_detail.html', {'idea': idea, 'investors': investors, 'investors_count': investors_count, 'user_profile': user_profile})


@innovator_required
@login_required
def add_idea(request):
    if request.method == 'POST':
        idea_form = IdeaForm(data=request.POST)
        if idea_form.is_valid():
            new_idea_form = idea_form.save(commit=False)
            new_idea_form.user = request.user
            new_idea_form.save()
            return redirect('portal:innovator')
    else:
        idea_form = IdeaForm()
    return render(request, 'portal/idea.html', {'idea_form': idea_form})


@innovator_required
@login_required
def edit_idea(request, id):
    idea = get_object_or_404(Ideas, id=id)
    if request.method == 'POST':
        idea_form = IdeaForm(data=request.POST, instance=idea)
        if idea_form.is_valid():
            idea = idea_form.save(commit=False)
            idea.save()
            return redirect('portal:innovator')
    else:
        idea_form = IdeaForm(instance=idea)
    return render(request, 'portal/edit_idea.html', {'idea_form': idea_form})


@entrepreneur_required
@login_required
def add_business(request):
    if request.method == 'POST':
        business_form = BusinessForm(data=request.POST)
        if business_form.is_valid():
            new_business_form = business_form.save(commit=False)
            new_business_form.user = request.user
            new_business_form.save()
            return redirect('portal:entrepreneur')
    else:
        business_form = BusinessForm()
    return render(request, 'portal/business.html', {'business_form': business_form})


@entrepreneur_required
@login_required
def edit_business(request, id):
    business = get_object_or_404(StartupBusiness, id=id)
    if request.method == 'POST':
        business_form = BusinessForm(data=request.POST, instance=business)
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.save()
            return redirect('portal:entrepreneur')
    else:
        business_form = BusinessForm(instance=business)
    return render(request, 'portal/edit_business.html', {'business_form': business_form})


@investor_required
@login_required
def investments(request):
    investments = IdeaInvestments.objects.filter(investor=request.user)
    investment_count = IdeaInvestments.objects.count()
    return render(request, 'portal/investments.html', {'investments': investments, 'investment_count': investment_count})


@investor_required
def invest_idea(request, id):
    idea = get_object_or_404(Ideas, id=id)
    ideaInvest = IdeaInvestments()
    ideaInvest.idea = idea
    ideaInvest.investor = request.user
    ideaInvest.save()
    return redirect('portal:investments')


@login_required
@investor_required
def investments_business(request):
    biz_investments = BusinessInvestments.objects.filter(investor=request.user)
    biz_investment_count = BusinessInvestments.objects.count()
    return render(request, 'portal/investment_biz.html', {'investments': biz_investments, 'investment_count': biz_investment_count})


@investor_required
@login_required
def invest_business(request, id):
    busines = get_object_or_404(StartupBusiness, id=id)
    businesInvest = BusinessInvestments()
    businesInvest.business = busines
    businesInvest.investor = request.user
    businesInvest.save()
    return redirect('portal:investments')


@login_required
def join_business(request, id):
    business = get_object_or_404(StartupBusiness, id=id)
    biz_team = BusinessTeams()
    biz_team.business = business
    biz_team.member = request.user
    biz_team.save()
    return redirect('portal:home')


@login_required
def join_idea(request, id):
    idea = get_object_or_404(Ideas, id=id)
    idea_team = IdeaTeams()
    idea_team.idea = idea
    idea_team.member = request.user
    idea_team.save()
    return redirect('portal:home')


def terms(request):
    return render(request, 'portal/terms.html')


def privacy(request):
    return render(request, 'portal/privacy.html')












