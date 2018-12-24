from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView
from django.views import defaults as default_views
from common.views import index_view, careers_view, updates_view, seminars_view

urlpatterns = [
    path("", view=index_view, name="index"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path("seminars-upenn/", view=seminars_view, name="seminars_view"),
    path("updates/", TemplateView.as_view(template_name="pages/updates_landing.html"), name="updates_landing"),
    re_path(r'^updates/(?P<type_of_update>\w+)/(?:page-(?P<page_number>\d+)/)?$', updates_view, name="updates_view"),
    path("careers/", view=careers_view, name="careers_view"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("hain_site.users.urls", namespace="users"),
    ),
    path("accounts/", include("allauth.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("favicon.ico", RedirectView.as_view(url='/static/images/favicons/favicon.ico', permanent=True)),
    path(
        "common/",
        include("hain_site.common.urls", namespace="common"),
    ),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
