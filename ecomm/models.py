from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator


State_Choices = (
    ('Koshi','Koshi'),
    ('Bagmati','Bagmati'),
    ('Gandaki','Gandaki'),
    ('Madhesh','Madhesh'),
    ('Lumbini','Lumbini'),
    ('Karnali','Karnali'),
    ('Sudurpashchim','Sudurpashchim'),
)
# Customer model.
class Customer (models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    name = models.CharField(max_length=20)
    locations = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    state = models.CharField(choices=State_Choices,max_length=20)

    def __str__(self):
        return str(self.id)
    
# Product model.
Category_Choice=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('Top Wear','Top Wear'),
    ('Bottom Wear','Bottom Wear'),
)

class Product(models.Model):
    title = models.CharField(max_length=30)
    selling_price = models.FloatField()
    discunted_prce =models.FloatField()
    discription = models.TextField()
    brand = models.CharField(max_length=30)
    Category = models.CharField(choices=Category_Choice,max_length=20)
    product_image = models.ImageField(upload_to='Product_image')

    def __str__(self):
        return str(self.id)
    
# Cart model.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quentity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quentity * self.product.discunted_prce
    
# Order model.

Status_choice= (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quentity = models.PositiveIntegerField(default=1)
    order_date =models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status_choice,max_length=30,default='Pending')

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quentity * self.product.discunted_prce



    

    








