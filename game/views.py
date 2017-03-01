from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response,render
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.contrib.auth.models import Group
from django.conf import settings

from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from hashlib import md5


from game.models import *
from .forms import *



def about(request):
    return HttpResponse("about page")


def game_view(request, product_id):
    """A view of a single game."""
    game = Game.objects.get(pk=product_id)

    is_creator = (request.user.is_authenticated() and game.creator == request.user.profile)
    is_playable = (request.user.is_authenticated() and game in request.user.profile.owned_games.all() or is_creator)

    topscores = sorted(game.saves.all(), key=lambda x: x.highscore, reverse=True)


    if (is_creator):
        if request.method == 'POST':
            if 'delete_submit' in request.POST:
                delete_form = DeleteGameForm(request.POST, instance=game)

                if delete_form.is_valid():
                    game.delete()
                    return HttpResponseRedirect('/developer/')
            elif 'edit_submit' in request.POST:
                edit_form = GameForm(request.POST, instance=game)

                if edit_form.is_valid():
                    edit_form.save()
                    return HttpResponseRedirect('')
        else:
            edit_form = GameForm(instance=game)
            delete_form = DeleteGameForm(instance=game)
    else:
        delete_form = None
        edit_form = None
    return render(request, 'game/game_view.html', {'game': game, 'is_playable': is_playable, 'topscores':topscores, 'edit_form': edit_form, 'delete_form': delete_form})


@login_required()
def game_buy_view(request, product_id):
    """A view for buying a game."""
    game = Game.objects.get(pk=product_id)
    user = request.user
    print (user)
    owned_games = user.profile.owned_games
    print (owned_games)

    transaction = Transaction()
    transaction.payer = user
    transaction.payed_game = game
    transaction.price = game.price
    transaction.date = timezone.now()
    transaction.save()

    buy_form = BuyGameForm()
    amount = game.price
    print (amount)
    pid = transaction.id
    sid = buy_form.fields["sid"].initial
    secret_key = '6cd118b1432bf22942d93d784cd17084'
    checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
    m = md5(checksumstr.encode("ascii"))
    # print (m)
    checksum = m.hexdigest()
    print (checksum)
    new_buy_form = BuyGameForm(initial={'pid': pid, 'amount': amount, 'checksum': checksum})
    print (new_buy_form)

    return render(request, 'game/game_buy_view.html', {'game': game, 'new_buy_form': new_buy_form})


@login_required()
def game_play_view(request, product_id):
    """View where gameplay happens."""
    game = Game.objects.get(pk=product_id)
    player = request.user.profile

    if game not in player.owned_games.all() and game.creator != player:
        return HttpResponseRedirect('../buy')

    save = Save.objects.filter(player=player, game=game).first() # returns instance or None

    if request.method == 'POST':
        form = SaveForm(request.POST, instance=save)
        if save != None and save.highscore != None:
            old_highscore = save.highscore
        else:
            old_highscore = 0
        if form.is_valid():
            save = form.save(commit=False)
            new_highscore = form.cleaned_data['highscore']
            if new_highscore > old_highscore:
                save.player = player
                save.game = game
                form.save()
    else:
        form = SaveForm(instance=save)

    return render(request, 'game/game_play_view.html', {'game': game, 'save_form': form})


def available_games(request):
    """A view of all games in the shop."""
    string= ""
    games = Game.objects.all()
    query = request.GET.get("q")
    if query:
        games = games.filter(title__icontains = query)
        string = "Searching Results:"
    if request.user.is_authenticated():
        profile = None
        user=request.user
        try:
            profile = user.profile;
        except Profile.DoesNotExist:
           return HttpResponseRedirect("/register/3rd_complete")
    else:
        profile = None


    return render(request, 'game/game_list.html', {'games': games, 'profile': profile, 'string':string})


def third_party_view(request):
    profile_form = ProfileForm(request.POST or None)
    user=request.user

    if  profile_form.is_valid():
        print("Forms are valid")
        profile = Profile()
        profile.user = request.user
        usertype = profile_form.cleaned_data.get('usertype')
        profile.usertype = usertype
        profile.save()
        return HttpResponseRedirect("/")
    return render(request, 'registration/third_party_view.html', {'profile_form': profile_form,'user':user})


@login_required()
def developer_view(request):
    """A view of the logged-in developer's games."""

    if request.user.profile.is_developer():
        profile = request.user.profile
        games = Game.objects.filter(creator=request.user.profile)
    else:
        print("Error")

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            creator = request.user.profile
            game.creator = creator
            form.save()
    else:
        if request.user.profile.is_developer():
            new_game = Game()
            form = GameForm(initial={'title': 'Super Django Bros.', 'price': 0.0}, instance=new_game)
        else:
            form = None
    return render(request, 'game/developer_game_list.html', {'profile':profile, 'games': games, 'form': form})


def developer_public_view(request, developer_id):
    """A public view of a developer's games."""

    developer = User.objects.get(id=developer_id)
    games = Game.objects.filter(creator=developer_id)

    return render(request, 'game/developer_public_page.html', {'developer':developer, 'games': games})


@login_required
def player_view(request):
    profile = request.user.profile
    games = request.user.profile.owned_games.all()
    return render(request, 'game/player_game_list.html', {'profile':profile, 'games': games})


def login_view(request):
    form = UserLoginForm(request.POST or None)

    print (form)
    if form.is_valid():
        print("Login form is valid")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect("/")
    else:
        print("Login form not valid")

    return render(request, "registration/login.html", {"form":form})


def register_view(request):
    user_form = UserRegisterForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    print (profile_form)

    if user_form.is_valid() and profile_form.is_valid():
        print("Forms are valid")
        user = user_form.save(commit=False)
        password = user_form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        profile = Profile()
        profile.user = user
        usertype = profile_form.cleaned_data.get('usertype')
        profile.usertype = usertype
        profile.save()

        # Send email to newly registered member
        subject = 'Congrats to you to become the newbie on Gamesite!'
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email,from_email]
        contact_message = "%s via %s"%(
            user.username,
            user.email)
        some_html_message = """
        <h3>Dear user, </h3>
        <p> Congrats that you have become one of members in Gamesite Family! We warmly welcome your join!
        if you have any question or advice, please email us.</p>
        <h3> Best Regards,</h3>
        <h3> Gamesite </h3>
        """
        try:
            send_mail(subject,
                      contact_message,
                      from_email,
                      to_email,
                      html_message=some_html_message,
                      fail_silently=True)
        except ConnectionRefusedError:
            print("Failed to connect to the SMTP server. Is it running?")


        messages.success(request, 'Profile details updated.')

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return HttpResponseRedirect("/")
    return render(request, "registration/register.html",  {"user_form":user_form, "profile_form":profile_form})


def logout_view(request):
    user= request.user
    print (user)
    logout(request)
    return render(request, "registration/logout.html", {"user":user})


def payment_cancel_view(request):
    return HttpResponse("payment failure, try again")


@login_required
def payment_success_view(request):
    print (request)

    if request.user.is_authenticated:
        user = request.user
        pid = request.GET.get('pid')
        ref = request.GET.get('ref')
        server_check = request.GET.get('checksum')
        result = 'success'
        secret_key = '6cd118b1432bf22942d93d784cd17084'
        checksumstr = "pid={}&ref={}&result={}&token={}".format(pid, ref, result, secret_key)
        m = md5(checksumstr.encode("ascii"))
        checksum = m.hexdigest()

        if checksum == server_check:
            transaction = Transaction.objects.get(pk=pid)
            game = transaction.payed_game
            print (game.id)
            user.profile.owned_games.add(game)
            print("Successfully bought game")
            return HttpResponseRedirect('/player')
        else:
            print ("Forbidden to buy the game!")
            return HttpResponseRedirect('/payment/error/2/')
    else:
        print("Can't buy game when not logged in!")


def payment_error_view(request,error_type):
    if error_type=='0':
        error = "Server rejected the payment!"
        print("error0")
    if error_type=='1':
        error="The game has already existed in your account! Do not pay again!"
        print("error1")
    if error_type=='2':
        error="Dangerous! Forbidden to operate the game! "

    return render(request, "game/payment_error.html", {'error':error})


@login_required()
def test(request):
    if request.user.is_authenticated:
        print(request.user)
        return HttpResponse("url authenticated")
    else:
        return HttpResponse("failure")
