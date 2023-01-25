from django.urls import path
from issues import views

urlpattern = [
    path('', views.IssueListView.as_view(), name='issue_list'),
    path('<int:pk>/', views.IssueDetailView.as_view(), name='issue_detail'),
    path('<int:pk>/', views.IssueUpdateView.as_view(), name='issue_edit'),
    path('<int:pk>/', views.IssueDeleteView.as_view(), name='issue_delete'),
    path('new/', views.IssuecreateView.as_view(), name='issue_new'),
]
