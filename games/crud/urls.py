from django.urls import path

from .views import (
    genre_list, genre_create, genre_delete, genre_update,
    rating_list, rating_create, rating_delete, rating_update,
    game_list, game_create, game_update, game_delete,
    publisher_list, publisher_create, publisher_delete, publisher_update,
    company_update, company_create, company_list, company_delete,
    developer_delete, developer_create, developer_update, developer_list,
    license_list, license_create, license_delete, license_update,
    award_create, award_delete, award_update, award_list,
    document_create, document_delete, document_update, document_list, document_open

)

urlpatterns = [
    path('genre-list', genre_list, name='genre-list'),
    path('genre-create', genre_create, name='genre-create'),
    path('genre-update/<int:id>', genre_update, name='genre-update'),
    path('genre-delete/<int:id>', genre_delete, name='genre-delete'),

    path('rating-list', rating_list, name='rating-list'),
    path('rating-create', rating_create, name='rating-create'),
    path('rating-update/<int:id>', rating_update, name='rating-update'),
    path('rating-delete/<int:id>', rating_delete, name='rating-delete'),

    path('game-list', game_list, name='game-list'),
    path('game-create', game_create, name='game-create'),
    path('game-update/<int:id>', game_update, name='game-update'),
    path('game-delete/<int:id>', game_delete, name='game-delete'),

    path('publisher-list', publisher_list, name='publisher-list'),
    path('publisher-create', publisher_create, name='publisher-create'),
    path('publisher-update/<int:id>', publisher_update, name='publisher-update'),
    path('publisher-delete/<int:id>', publisher_delete, name='publisher-delete'),

    path('company-list', company_list, name='company-list'),
    path('company-create', company_create, name='company-create'),
    path('company-update/<int:id>', company_update, name='company-update'),
    path('company-delete/<int:id>', company_delete, name='company-delete'),

    path('developer-list', developer_list, name='developer-list'),
    path('developer-create', developer_create, name='developer-create'),
    path('developer-update/<int:id>', developer_update, name='developer-update'),
    path('developer-delete/<int:id>', developer_delete, name='developer-delete'),

    path('license-list', license_list, name='license-list'),
    path('license-create', license_create, name='license-create'),
    path('license-update/<int:id>', license_update, name='license-update'),
    path('license-delete/<int:id>', license_delete, name='license-delete'),

    path('award-list', award_list, name='award-list'),
    path('award-create', award_create, name='award-create'),
    path('award-update/<int:id>', award_update, name='award-update'),
    path('award-delete/<int:id>', award_delete, name='award-delete'),

    path('document-list', document_list, name='document-list'),
    path('document-create', document_create, name='document-create'),
    path('document-update/<int:id>', document_update, name='document-update'),
    path('document-delete/<int:id>', document_delete, name='document-delete'),
    path('document-open/<int:id>', document_open, name='document-open'),
]
