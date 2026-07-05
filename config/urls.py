"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from django.http import HttpResponse

from users.views import UserViewSet
from workspaces.views import WorkspaceViewSet
from documents.views import DocumentViewSet
from comments.views import CommentViewSet
from tags.views import TagViewSet
from auditlogs.views import AuditLogViewSet

router = DefaultRouter()

router.register("users", UserViewSet)
router.register("workspaces", WorkspaceViewSet)
router.register("documents", DocumentViewSet)
router.register("comments", CommentViewSet)
router.register("tags", TagViewSet)
router.register("auditlogs", AuditLogViewSet)


def home(request):
    return HttpResponse("🚀 CollabDocs API is running successfully!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
