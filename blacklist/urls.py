from django.conf.urls import url

from . import views

app_name = 'blacklist'

urlpatterns = [
    url(r'^notes/$', views.note_board, name='note_board'),
    url(r'^blacklist/$', views.blacklist, name='blacklist'),
    url(r'^get_add_note/(?P<eve_id>(\d)*)/$', views.get_add_evenote, name='modal_add'),
    url(r'^get_comments/(?P<evenote_id>(\d)*)/$', views.get_evenote_comments, name='modal_comment'),
    url(r'^get_edit_note/(?P<evenote_id>(\d)*)/$', views.get_edit_evenote, name='modal_edit'),
    url(r'^get_add_comment/(?P<evenote_id>(\d)*)/$', views.get_add_comment, name='modal_add_comment'),
    url(r'^search_names/$', views.search_names, name='search_names'),
    url(r'^add_comment/(?P<note_id>(\d)*)/$', views.add_comment, name='add_comment'),
    url(r'^add_note/(?P<eve_id>(\d)*)/$', views.add_note, name='add_note'),
    url(r'^edit_note/(?P<note_id>(\d)*)/$', views.edit_note, name='edit_note'),
]
