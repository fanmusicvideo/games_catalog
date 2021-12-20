from django.shortcuts import render, redirect
import os
from games.settings import BASE_DIR
from .forms import (
    GenreForm, GameForm, RatingForm,
    PublisherForm, CompanyForm, DeveloperForm,
    LicenseForm, AwardForm, DocumentForm
)
from .models import (
    Game, Rating, Genre,
    Publisher, Company, Developer,
    License, Award, Document
)


def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')


def document_open(request, id):
    documents = Document.objects.all()
    document = Document.objects.get(id=id)
    os.system(f'xdg-open {BASE_DIR}/media/{document.upload}')
    return render(request, 'document-list.html', {'documents': documents})


def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document-list.html', {'documents': documents})


def document_create(request):
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('document-list')
            except:
                pass
    else:
        form = DocumentForm()
    return render(request, 'document-create.html', {'form': form})


def document_update(request, id):
    document = Document.objects.get(id=id)
    form = DocumentForm(initial={
        'upload': document.upload,
    })
    if request.method == "POST":
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/document-list')
            except Exception as e:
                pass
    return render(request, 'document-update.html', {'form': form})


def document_delete(request, id):
    document = Document.objects.get(id=id)
    try:
        document.delete()
    except:
        pass
    return redirect('document-list')


def award_list(request):
    awards = Award.objects.all()
    return render(request, 'award-list.html', {'awards': awards})


def award_create(request):
    if request.method == "POST":
        form = AwardForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('award-list')
            except:
                pass
    else:
        form = AwardForm()
    return render(request, 'award-create.html', {'form': form})


def award_update(request, id):
    award = Award.objects.get(id=id)
    form = AwardForm(initial={
        'name': award.name,
        'description': award.description,
    })
    if request.method == "POST":
        form = AwardForm(request.POST, instance=award)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/award-list')
            except Exception as e:
                pass
    return render(request, 'award-update.html', {'form': form})


def award_delete(request, id):
    award = Award.objects.get(id=id)
    try:
        award.delete()
    except:
        pass
    return redirect('award-list')


def license_list(request):
    licenses = License.objects.all()
    return render(request, 'license-list.html', {'licenses': licenses})


def license_create(request):
    if request.method == "POST":
        form = LicenseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('license-list')
            except:
                pass
    else:
        form = LicenseForm()
    return render(request, 'license-create.html', {'form': form})


def license_update(request, id):
    license = License.objects.get(id=id)
    form = LicenseForm(initial={
        'name': license.name,
        'description': license.description,
    })
    if request.method == "POST":
        form = LicenseForm(request.POST, instance=license)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/license-list')
            except Exception as e:
                pass
    return render(request, 'license-update.html', {'form': form})


def license_delete(request, id):
    license = License.objects.get(id=id)
    try:
        license.delete()
    except:
        pass
    return redirect('license-list')


def developer_list(request):
    developers = Developer.objects.all()
    return render(request, 'developer-list.html', {'developers': developers})


def developer_create(request):
    if request.method == "POST":
        form = DeveloperForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('developer-list')
            except:
                pass
    else:
        form = DeveloperForm()
    return render(request, 'developer-create.html', {'form': form})


def developer_update(request, id):
    developer = Developer.objects.get(id=id)
    form = DeveloperForm(initial={
        'name': developer.name,
        'description': developer.description,
    })
    if request.method == "POST":
        form = DeveloperForm(request.POST, instance=developer)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/developer-list')
            except Exception as e:
                pass
    return render(request, 'developer-update.html', {'form': form})


def developer_delete(request, id):
    developer = Developer.objects.get(id=id)
    try:
        developer.delete()
    except:
        pass
    return redirect('developer-list')


def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company-list.html', {'companies': companies})


def company_create(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('company-list')
            except:
                pass
    else:
        form = CompanyForm()
    return render(request, 'company-create.html', {'form': form})


def company_update(request, id):
    company = Company.objects.get(id=id)
    form = CompanyForm(initial={
        'name': company.name,
        'description': company.description,
    })
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/company-list')
            except Exception as e:
                pass
    return render(request, 'company-update.html', {'form': form})


def company_delete(request, id):
    company = Company.objects.get(id=id)
    try:
        company.delete()
    except:
        pass
    return redirect('company-list')


def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher-list.html', {'publishers': publishers})


def publisher_create(request):
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('publisher-list')
            except:
                pass
    else:
        form = PublisherForm()
    return render(request, 'publisher-create.html', {'form': form})


def publisher_update(request, id):
    publisher = Publisher.objects.get(id=id)
    form = PublisherForm(initial={
        'name': publisher.name,
        'description': publisher.description,
    })
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/publisher-list')
            except Exception as e:
                pass
    return render(request, 'publisher-update.html', {'form': form})


def publisher_delete(request, id):
    publisher = Publisher.objects.get(id=id)
    try:
        publisher.delete()
    except:
        pass
    return redirect('publisher-list')


def game_list(request):
    games = Game.objects.all()
    return render(request, 'game-list.html', {'games': games})


def game_create(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('game-list')
            except:
                pass
    else:
        form = GameForm()
    return render(request, 'game-create.html', {'form': form})


def game_update(request, id):
    game = Game.objects.get(id=id)
    form = GameForm(initial={
        'title': game.title,
        'description': game.description,
        'rating': game.rating,
        'genres': game.genres.all,
        'publishers': game.publishers.all,
        'developers': game.developers.all,
        'companies': game.companies.all,
        'awards': game.awards.all,
        'licenses': game.licenses.all,
    })
    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/game-list')
            except Exception as e:
                pass
    return render(request, 'game-update.html', {'form': form})


def game_delete(request, id):
    game = Game.objects.get(id=id)
    try:
        game.delete()
    except:
        pass
    return redirect('game-list')


def rating_list(request):
    ratings = Rating.objects.all()
    return render(request, 'rating-list.html', {'ratings': ratings})


def rating_create(request):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('rating-list')
            except:
                pass
    else:
        form = RatingForm()
    return render(request, 'rating-create.html', {'form': form})


def rating_update(request, id):
    rating = Rating.objects.get(id=id)
    form = RatingForm(initial={'name': rating.name})
    if request.method == "POST":
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/rating-list')
            except Exception as e:
                pass
    return render(request, 'rating-update.html', {'form': form})


def rating_delete(request, id):
    rating = Rating.objects.get(id=id)
    try:
        rating.delete()
    except:
        pass
    return redirect('rating-list')


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre-list.html', {'genres': genres})


def genre_create(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('genre-list')
            except:
                pass
    else:
        form = GenreForm()
    return render(request, 'genre-create.html', {'form': form})


def genre_update(request, id):
    genre = Genre.objects.get(id=id)
    form = GenreForm(initial={'name': genre.name})
    if request.method == "POST":
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/genre-list')
            except Exception as e:
                pass
    return render(request, 'genre-update.html', {'form': form})


def genre_delete(request, id):
    genre = Genre.objects.get(id=id)
    try:
        genre.delete()
    except:
        pass
    return redirect('genre-list')
