from django import forms
from .models import (
    Game, Rating, Genre,
    Publisher, Company, Developer,
    License, Award, Document
)


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = '__all__'


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
