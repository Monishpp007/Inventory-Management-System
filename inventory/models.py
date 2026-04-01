from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchases')
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase {self.quantity} of {self.item.name}"


class Sale(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='sales')
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale {self.quantity} of {self.item.name}"

