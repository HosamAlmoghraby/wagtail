"""An alternative urlconf module where Wagtail front-end URLs
are rooted at '/site/' rather than '/'"""

from django.urls import include, path

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.images import urls as wagtailimages_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('images/', include(wagtailimages_urls)),
    path('site/', include(wagtail_urls)),
]