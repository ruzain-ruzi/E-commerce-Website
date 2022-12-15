from django.db import models


# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    u_type = models.CharField(max_length=200)


class shop(models.Model):
    shop_id = models.ForeignKey(login, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    pin = models.BigIntegerField()
    photo = models.FileField(upload_to='shop-images')
    email = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    password = models.CharField(max_length=200)


class customer(models.Model):
    login_id = models.ForeignKey(login, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    pin = models.BigIntegerField()
    photo = models.FileField(upload_to='customer-images')
    email = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class complaint(models.Model):
    cust_id = models.ForeignKey(customer, default=1, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=500)
    date = models.DateField()
    reply = models.CharField(max_length=500, default='NULL')
    reply_date = models.DateField(default='NULL')


class feedback(models.Model):
    cust_id = models.ForeignKey(customer, default=1, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)
    date = models.DateField()


class products(models.Model):
    shop_id = models.ForeignKey(shop, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    photo = models.FileField(upload_to='product-images')
    price = models.CharField(max_length=200)
    stock = models.BigIntegerField()


class master(models.Model):
    cust_id = models.ForeignKey(customer, default=1, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    date = models.DateField()


class order(models.Model):
    product_id = models.ForeignKey(products, default=1, on_delete=models.CASCADE)
    master_id = models.ForeignKey(master, default=1, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()

    def total_price(self):
        return float(self.quantity) * float(self.product_id.price)

    @classmethod
    def extra(cls, select):
        pass


class reviews(models.Model):
    cust_id = models.ForeignKey(customer, default=1, on_delete=models.CASCADE)
    order_id = models.ForeignKey(order, default=1, on_delete=models.CASCADE)
    review = models.CharField(max_length=500)
    date = models.DateField()
