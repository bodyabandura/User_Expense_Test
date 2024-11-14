from django.urls import path
from .views import ExpenseListCreateView, ExpenseRetrieveUpdateDeleteView, ExpenseByDateRangeView, ExpenseCategorySummaryView

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDeleteView.as_view(), name='expense-retrieve-update-delete'),
    path('expenses/by-date-range/', ExpenseByDateRangeView.as_view(), name='expense-by-date-range'),
    path('expenses/category-summary/', ExpenseCategorySummaryView.as_view(), name='expense-category-summary'),
]
