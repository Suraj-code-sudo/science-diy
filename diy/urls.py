from django.urls import path, include
from .views import ExpList, ExpDetail, ExpCreate, ExpUpdate, ExpDelete,Student_list, Student_Detail, CustomLoginView, clap
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("exp-admin", ExpList.as_view(), name="exp_list"),
    path("exp/<int:pk>/", ExpDetail.as_view(), name="experiment"),
    path("exp-create", ExpCreate.as_view(), name="experiment_create"),
    path("exp-update/<int:pk>/", ExpUpdate.as_view(), name="experiment_update"),
    path("exp-delete/<int:pk>/", ExpDelete.as_view(), name="experiment_delete"),
    path("", Student_list.as_view(), name="student"),
    path("student-detail/<int:pk>/", Student_Detail.as_view(), name="student-detail"),
    path("clap/<int:pk>/", clap, name="clap")
]   
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

