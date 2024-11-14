from users.models import User
from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Expense
        fields = ["id", "user", "title", "amount", "date", "category"]


class ExpenseSerializerByDate(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    start_date = serializers.DateField(write_only=True)
    end_date = serializers.DateField(write_only=True)

    class Meta:
        model = Expense
        fields = ["id", "user", "start_date", "end_date"]


class ExpenseSerializerByCategorySummary(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    month = serializers.IntegerField(write_only=True)
    year = serializers.IntegerField(write_only=True)
    category = serializers.CharField()

    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        fields = ["user", "month", "year", "category", "total_amount"]
