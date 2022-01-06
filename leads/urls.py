from django.urls import path

from .views import LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView
from .views_function import lead_list, lead_detail, lead_create, lead_update, lead_delete

app_name = "leads"

urlpatterns = [
    path("", LeadListView.as_view(), name="lead-list"),
    path("<int:pk>/", LeadDetailView.as_view(), name="lead-detail"),
    path("<int:pk>/update/", LeadUpdateView.as_view(), name="lead-update"),
    path("<int:pk>/delete/", LeadDeleteView.as_view(), name="lead-delete"),
    path("create/", LeadCreateView.as_view(), name="lead-create")
]

# urlpatterns = [
#     path("", lead_list, name="lead-list"),
#     path("<int:pk>/", lead_detail, name="lead-detail"),
#     path("<int:pk>/update/", lead_update, name="lead-update"),
#     path("<int:pk>/delete/", lead_delete, name="lead-delete"),
#     path("create/", lead_create, name="lead-create")
# ]