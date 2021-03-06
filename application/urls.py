from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),

    # path('search', views.search, name="search"),

    path('profile/', views.profile, name="profile"),
    path("reset-password", views.reset_password, name="reset-password"),

    # path('bookmarks/<bookmark_id>/delete', views.delete_bookmark, name="delete_bookmark"),
    # path('bookmarks/', views.bookmarks, name="bookmarks"),

    # path('learn_by_query/', views.learn_by_query, name="learn_by_query"),
    # path('new_learn_by_query/', views.new_learn_by_query, name="new_learn_by_query"),
    # path('bookmark/<bookmark_id>', views.learn_bookmark, name="learn_bookmark"),
    # path('term/<term_id>', views.learn_term, name="learn_term"),
    # path('learn/', views.learn, name="learn"),

    # path('folders/', views.folders, name="folders"),
    # path('folders/<folder_id>', views.single_folder, name="single-folder"),
    # path('folders/<folder_id>/term/<term_id>', views.single_folder, name="single-term"),
    # path('term/<term_id>/edit', views.create_term, name="edit_term"),
    # path('folders/<folder_id>/delete', views.delete_folder, name="delete_folder"),
    # path('folders/term/add', views.create_folder, name="create-folder"),

    # path('terms/create', views.create_term, name="create-single-term"),

    # path('journal/', views.journal, name="journal"),
    # # path('journal/terms/<term_id>/edit/', views.create_term, name="edit_term"),
    # path('journal/terms/<term_id>/', views.journal, name="open_term"),
    # path('journal/terms/<term_id>/delete/', views.delete_term, name="delete_term"),
    # path('journal/terms/create', views.create_term, name="create_term"),

    # path('topics/', views.topics, name="topics"),
    # path('add-topics/', views.add_topics, name="add-topics"),
    # path('topics/<id>/delete', views.delete_topic, name="delete_topic"),

    # path('categories/', views.categories, name="categories"),
    # path('categories/<id>/delete', views.delete_category, name="delete_category"),
    # path('add-catgories', views.add_catgories, name="add-catgories"),

    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.signout, name="logout"),

    # Test path for checking the browser, IP-address, and device info of the user
    path('browser/', views.get_browser_info, name='browser'),

    path('media/<media_id>/done', views.mark_as_done, name='mark-as-done'),

    path('device/<int:device_id>/delete',
         views.delete_user_device, name='delete_device'),

    # Path to All trainings Page
    path('trainings/', views.all_trainings, name='trainings'),

    # Path to (Single training - with all modules) Page
    path('trainings/<int:training_id>/modules/',
         views.all_modules, name='all_modules'),

    # Path to (Single training - with all modules) Page
    path('trainings/<int:training_id>/',
         views.resume_all_modules, name='resume_all_modules'),

    # Path to (Single training - with single module - with all videos) Page
    path('trainings/<int:training_id>/modules/<int:module_id>/medias/',
         views.media, name='media'),

    # Path to (Single training - with single module - with single media) Page
    path('trainings/<int:training_id>/modules/<int:module_id>/medias/<int:media_id>/',
         views.media, name='single_media'),

    path('progress/',
         views.progress, name="progress"),


    path('progress/customer/<id>/trainings/',
         views.progress_trainings, name="progress-training"),


    path('progress/customer/<id>/trainings/<training_id>/modules/',
         views.progress_modules, name="progress-module")

]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
