from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime

from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.utils import json

from .models import Expense
from .serializers import ExpenseSerializer, ExpenseSerializerByDate, ExpenseSerializerByCategorySummary
from users.models import User


class ExpenseListCreateView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user', None)

        if not user_id:
            raise ValidationError("User ID is required.")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError("User with this ID does not exist.")

        request.data['user'] = user.id

        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

class ExpenseRetrieveUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs, partial=True)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ExpenseByDateRangeView(generics.GenericAPIView):
    serializer_class = ExpenseSerializerByDate

    def post(self, request, *args, **kwargs):
        try:
            body_data = json.loads(request.body)

            user_id = body_data.get('user', None)
            start_date = body_data.get('start_date', None)
            end_date = body_data.get('end_date', None)

            if not user_id or not start_date or not end_date:
                raise ValidationError("user, start_date, and end_date are required.")

            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise ValidationError("User with this ID does not exist.")

            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
            except ValueError:
                raise ValidationError("Invalid date format. Use YYYY-MM-DD.")

            expenses = Expense.objects.filter(date__range=[start_date, end_date], user=user)
            expense_serializer = ExpenseSerializer(expenses, many=True)

            return JsonResponse(expense_serializer.data, safe=False)

        except Exception as e:
            raise ValidationError(f"Error: {str(e)}")


class ExpenseCategorySummaryView(generics.GenericAPIView):
    serializer_class = ExpenseSerializerByCategorySummary

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data['user'].id
        month = serializer.validated_data['month']
        year = serializer.validated_data['year']
        category = serializer.validated_data['category']

        try:
            start_date = datetime(year, month, 1)
            if month == 12:
                end_date = datetime(year + 1, 1, 1)
            else:
                end_date = datetime(year, month + 1, 1)
        except ValueError:
            raise ValidationError("Invalid month or year.")

        total_amount = (
            Expense.objects.filter(
                user_id=user_id,
                date__range=[start_date, end_date],
                category=category
            )
            .aggregate(total=Sum('amount'))['total'] or 0
        )

        return Response({
            "user": user_id,
            "month": month,
            "year": year,
            "category": category,
            "total_amount": total_amount
        }, 200)
