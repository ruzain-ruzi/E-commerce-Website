import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from shop.models import *


def login_page(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        qry = login.objects.filter(username=email, password=password)

        if qry.exists():
            qry = qry[0]
            if qry.u_type == 'admin':
                messages.success(request, "Login Successful")
                return redirect('/admin')
            elif qry.u_type == 'shop':
                request.session['lid'] = qry.id
                messages.success(request, "Login Successful")
                return redirect('/shop')
            elif qry.u_type == 'customer':
                request.session['lid'] = qry.id
                messages.success(request, "Login Successful")
                return redirect('/customer')
            else:
                messages.error(request, 'Incorrect Email ID/Password')
                return redirect('/')
        else:
            messages.error(request, 'Incorrect Email ID/Password')
            return redirect('/')
    else:
        # messages.success(request, "Logout Successful")
        return render(request, 'login.html')


# ---------------------- Admin --------------------- #

def admin_home(request):
    return render(request, 'admin/admin_home.html')


def view_registered_shop(request):
    qry = shop.objects.filter(shop_id__u_type='pending')
    return render(request, 'admin/view_reg_shop.html', {'data': qry})


def approve_shop(request, id):
    login.objects.filter(id=id).update(u_type='shop')
    messages.success(request, "Shop Approved")
    return redirect('/vregshop')


def reject_shop(request, id):
    shop.objects.get(shop_id=id).delete()
    login.objects.get(id=id).delete()
    messages.success(request, "Shop Rejected")
    return redirect('/vregshop')


def view_shop(request):
    qry = shop.objects.filter(shop_id__u_type='shop')
    return render(request, 'admin/view_shop.html', {'data': qry})


def view_complaint(request):
    qry = complaint.objects.all()
    return render(request, 'admin/view_complaint.html', {'data': qry})


def send_reply(request, id):
    if request.method == 'POST':
        r = request.POST['reply']
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        obj = complaint.objects.get(id=id)
        obj.reply = r
        obj.reply_date = date
        obj.save()

        messages.success(request, "Reply Send")
        return redirect('/vcomplaint')
    else:
        r = complaint.objects.get(id=id)
        return render(request, 'admin/send_reply.html', {'rep': r})


def view_cust(request):
    qry = customer.objects.all()
    return render(request, 'admin/view_customer.html', {'data': qry})


def view_feedback(request):
    qry = feedback.objects.all()
    return render(request, 'admin/view_feedback.html', {'data': qry})


# ----------------------- Shop --------------------- #

def reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        pict = request.FILES['fileField']
        number = request.POST['number']
        email = request.POST['email']
        pas = request.POST['passwd']

        qry = login.objects.filter(username=email)

        if qry.exists():
            messages.warning(request, "Email ID Already Exists")
            return redirect('/register')
        else:
            obj = login()
            obj.username = email
            obj.password = pas
            obj.u_type = 'pending'
            obj.save()

            sho = shop()
            sho.name = name
            sho.place = place
            sho.post = post
            sho.pin = pin
            sho.photo = pict
            sho.email = email
            sho.phone_number = number
            sho.password = pas
            sho.shop_id = obj
            sho.save()

        messages.success(request, "Registered Successfully")
        return redirect('/')
    else:
        return render(request, 'register.html')


def shop_home(request):
    qry = shop()
    sid = request.session['lid']
    qry.shop_id_id = sid
    return render(request, 'shop/shop_home.html')


def add_prod(request):
    if request.method == 'POST':
        name = request.POST['name']
        pict = request.FILES['file']
        price = request.POST['price']
        st = request.POST['stk']

        sid = request.session['lid']
        obj = products()
        obj.name = name
        obj.photo = pict
        obj.price = price
        obj.stock = st
        obj.shop_id_id = sid
        obj.save()

        messages.success(request, "Product Added")
        return redirect('/view_product')
    else:
        return render(request, 'shop/add_product.html')


def view_prod(request):
    sid = request.session['lid']
    qry = products.objects.filter(shop_id=sid)
    return render(request, 'shop/view_product.html', {'data': qry})


def update_prod(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        pict = request.FILES['fileInput']
        price = request.POST['price']
        st = request.POST['stk']

        sid = request.session['lid']
        obj = products.objects.filter(id=id)
        obj.update(name=name)
        obj.update(photo=pict)
        obj.update(price=price)
        obj.update(stock=st)
        obj.update(shop_id_id=sid)

        messages.success(request, "Product Updated")
        return redirect('/view_product')
    else:
        prod = products.objects.get(id=id)
        return render(request, 'shop/edit_product.html', {'data': prod})


def delete_prod(request, id):
    products.objects.filter(id=id).delete()
    return redirect('/view_product')


def view_booking(request):
    sid = request.session['lid']
    qry = order.objects.filter(product_id__shop_id=sid)
    return render(request, 'shop/booking.html', {'data': qry})


def view_reviews(request):
    sid = request.session['lid']
    qry = reviews.objects.filter(order_id__product_id__shop_id=sid)
    return render(request, 'shop/reviews.html', {'data': qry})


def view_profile(request):
    sid = request.session['lid']
    qry = shop.objects.filter(shop_id_id=sid)
    return render(request, 'shop/profile.html', {'data': qry})


def shop_update_profile(request):
    if request.method == 'POST':
        name = request.POST['name']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        pict = request.FILES['avatar']
        email = request.POST['email']
        number = request.POST['phone']

        sid = request.session['lid']
        obj = shop.objects.filter(shop_id_id=sid)
        obj.update(name=name)
        obj.update(place=place)
        obj.update(post=post)
        obj.update(pin=pin)
        obj.update(photo=pict)
        obj.update(email=email)
        obj.update(phone_number=number)
        obj.update(shop_id_id=sid)

        messages.success(request, "Profile Updated")
        return redirect('/s_profile')
    else:
        sid = request.session['lid']
        sho = shop.objects.get(shop_id_id=sid)
        return render(request, 'shop/update_profile.html', {'data': sho})


def shop_change_pass(request):
    if request.method == 'POST':
        sid = request.session['lid']
        db = login.objects.get(id=sid)

        oldpasswd = request.POST['oldPassword']
        newpasswd = request.POST['passwordFile']
        conpasswd = request.POST['password2']

        if db.password != oldpasswd:
            messages.error(request, "Incorrect Password")
            return redirect('/cust_change_password')

        elif newpasswd != conpasswd:
            messages.error(request, "Password Mismatch")
            return redirect('/cust_change_password')

        else:
            obj = shop.objects.filter(shop_id_id=sid)
            obj.update(password=newpasswd)

            db = login.objects.filter(id=sid)
            db.update(password=newpasswd)

            messages.success(request, "Password Changed")
            return redirect('/s_profile')
    else:
        return render(request, 'shop/change_pass.html')


# ----------------------- Customer --------------------- #

def user_reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        pict = request.FILES['fileField']
        dob = request.POST['dob']
        gend = request.POST['gender']
        number = request.POST['number']
        email = request.POST['email']
        pas = request.POST['passwd']

        qry = login.objects.filter(username=email)

        if qry.exists():
            messages.warning(request, "Email ID Already Exists")
            return redirect('/user_reg')
        else:
            obj = login()
            obj.username = email
            obj.password = pas
            obj.u_type = 'customer'
            obj.save()

            cus = customer()
            cus.name = name
            cus.place = place
            cus.post = post
            cus.pin = pin
            cus.photo = pict
            cus.dob = dob
            cus.gender = gend
            cus.email = email
            cus.phone_number = number
            cus.password = pas
            cus.login_id = obj
            cus.save()

        messages.success(request, "Registered Successfully")
        return redirect('/')
    else:
        return render(request, 'register.html')


def cust_home(request):
    return render(request, 'customer/customer_home.html')


def cust_view_shop(request):
    qry = shop.objects.filter(shop_id__u_type='shop')
    return render(request, 'customer/cust_view_shop.html', {'data': qry})


def view_shop_products(request, id):
    if request.method == 'POST':

        sid = request.session['lid']
        stat = 'Add to Cart'
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        q = request.POST['quantFile']
        pro = request.POST['product']

        qry = master.objects.filter(cust_id__login_id=sid)
        cust = customer.objects.get(login_id=sid)
        book = order.objects.filter(master_id__cust_id__login_id=sid)
        order_dbb = order.objects.filter(master_id__cust_id__login_id=sid)
        product_dbb = order_dbb.filter(product_id=pro)
        carts = product_dbb.filter(master_id__status='Add to Cart')

        if qry.exists():

            if qry.filter(status='Booked').exists() and not qry.filter(status='Add to Cart').exists():
                mast = master()
                mast.status = stat
                mast.date = date
                mast.cust_id_id = cust.id
                mast.save()

                db = order()
                db.quantity = q
                db.date = date
                db.master_id_id = mast.id
                db.product_id_id = pro
                db.save()

            elif not qry.filter(status='Add to Cart').exists():
                mast = master()
                mast.status = stat
                mast.date = date
                mast.cust_id_id = cust.id
                mast.save()

                db = order()
                db.quantity = q
                db.date = date
                db.master_id_id = mast.id
                db.product_id_id = pro
                db.save()

            elif carts.filter(product_id=pro).exists():
                order_db = order.objects.filter(master_id__cust_id__login_id=sid)
                product_db = order_db.filter(product_id=pro)
                cart = product_db.filter(master_id__status='Add to Cart')
                cart.update(quantity=F('quantity') + q)

            else:
                obj = master.objects.filter(cust_id__login_id=sid)
                cart = obj.filter(status='Add to Cart')
                order_db = qry.filter(status='Add to Cart')

                mast = cart.get(id=order_db.first().id)

                obj.update(date=date)

                db = order()
                db.quantity = q
                db.date = date
                db.master_id_id = mast.id
                db.product_id_id = pro
                db.save()

        else:
            obj = master()
            obj.status = stat
            obj.date = date
            obj.cust_id_id = cust.id
            obj.save()

            db = order()
            db.quantity = q
            db.date = date
            db.master_id_id = obj.id
            db.product_id_id = pro
            db.save()

        messages.success(request, "Added to Cart")
        return redirect('/shops')
    else:
        qry = products.objects.filter(shop_id_id=id)
        n = shop.objects.get(shop_id_id=id)
        return render(request, 'customer/view_shop_products.html', {'data': qry, 'n': n})


def add_cart(request):
    if request.method == 'POST':
        sid = request.session['lid']
        stat = 'Add to Cart'
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        q = request.POST['quantFile']
        pro = request.POST['product']

        qry = master.objects.filter(cust_id__login_id=sid)
        cust = customer.objects.get(login_id=sid)
        book = order.objects.filter(master_id__cust_id__login_id=sid)
        order_dbb = order.objects.filter(master_id__cust_id__login_id=sid)
        product_dbb = order_dbb.filter(product_id=pro)
        carts = product_dbb.filter(master_id__status='Add to Cart')

        if qry.exists():

            if qry.filter(status='Booked').exists() and not qry.filter(status='Add to Cart').exists():
                mast = master()
                mast.status = stat
                mast.date = date
                mast.cust_id_id = cust.id
                mast.save()

                db = order()
                db.quantity = q
                db.date = date
                db.master_id_id = mast.id
                db.product_id_id = pro
                db.save()

            elif not qry.filter(status='Add to Cart').exists():
                mast = master()
                mast.status = stat
                mast.date = date
                mast.cust_id_id = cust.id
                mast.save()

                db = order()
                db.quantity = q
                db.date = date
                db.master_id_id = mast.id
                db.product_id_id = pro
                db.save()

            elif carts.filter(product_id=pro).exists():
                order_db = order.objects.filter(master_id__cust_id__login_id=sid)
                product_db = order_db.filter(product_id=pro)
                cart = product_db.filter(master_id__status='Add to Cart')
                cart.update(quantity=F('quantity') + q)

            else:
                obj = master.objects.filter(cust_id__login_id=sid)
                cart = obj.filter(status='Add to Cart')
                order_db = qry.filter(status='Add to Cart')

                mast = cart.get(id=order_db.first().id)

                obj.update(date=date)

                db = order()
                db.quantity = q
                db.date = date
                db.master_id_id = mast.id
                db.product_id_id = pro
                db.save()

        else:
            obj = master()
            obj.status = stat
            obj.date = date
            obj.cust_id_id = cust.id
            obj.save()

            db = order()
            db.quantity = q
            db.date = date
            db.master_id_id = obj.id
            db.product_id_id = pro
            db.save()

        messages.success(request, "Added to Cart")
        return redirect('/products')
    else:
        qry = products.objects.all()
        return render(request, 'customer/view_products.html', {'data': qry})


def view_cart(request):
    sid = request.session['lid']
    qry = order.objects.filter(master_id__cust_id__login_id=sid)
    cart = qry.filter(master_id__status='Add to Cart')

    prod = []
    for i in range(0, len(cart)):
        total = float(cart[i].product_id.price) * float(cart[i].quantity)
        prod.append(total)

    total = sum(prod)

    return render(request, 'customer/cart.html', {'data': qry, 'total': total})


def remove_cart(request, id):
    order.objects.filter(id=id).delete()

    messages.success(request, "Product Removed")
    return redirect('/cart')


def cart_checkout(request):
    sid = request.session['lid']
    stat = 'Booked'
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    obj = master.objects.filter(cust_id__login_id=sid)
    obj.update(status=stat)
    obj.update(date=date)

    # qry = order.objects.filter(master_id__cust_id__login_id=sid)
    # cart = qry.filter(master_id__status='Add to Cart')
    # for i in range(0, len(cart)):
    # prod = products.objects.get(id=cart.product_id_)
    # prod.stock = prod.stock - db.first().quantity
    # prod.save()

    messages.success(request, "Product Booked")
    return redirect('/cart')


def view_orders(request):
    sid = request.session['lid']
    db = order.objects.filter(master_id__cust_id__login_id=sid)
    rev = reviews.objects.filter(order_id__master_id__cust_id=sid)

    return render(request, 'customer/orders.html', {'ord': db, 'rev': rev})


def product_review(request, id):
    if request.method == 'POST':
        rev = request.POST['review']
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        qry = order.objects.get(id=id)
        db = reviews()
        db.date = date
        db.review = rev
        db.cust_id_id = qry.master_id.cust_id_id
        db.order_id_id = qry.id
        db.save()

        messages.success(request, "Review Send")
        return redirect('/cust_orders')
    else:
        odr = order.objects.get(id=id)
        return render(request, 'customer/product_review.html', {'data': odr})


def cust_reviews(request, id):
    qry = reviews.objects.filter(order_id__product_id=id)
    return render(request, 'customer/cust_reviews.html', {'data': qry})


def view_cust_profile(request):
    sid = request.session['lid']
    qry = customer.objects.filter(login_id_id=sid)
    return render(request, 'customer/customer_profile.html', {'data': qry})


def cust_update_profile(request):
    if request.method == 'POST':
        name = request.POST['name']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        pict = request.FILES['avatar']
        email = request.POST['email']
        number = request.POST['phone']
        dob = request.POST['dob']
        gen = request.POST['RadioGroup1']

        sid = request.session['lid']
        obj = customer.objects.filter(login_id_id=sid)
        obj.update(name=name)
        obj.update(place=place)
        obj.update(post=post)
        obj.update(pin=pin)
        obj.update(photo=pict)
        obj.update(email=email)
        obj.update(phone_number=number)
        obj.update(dob=dob)
        obj.update(gender=gen)

        messages.success(request, "Profile Updated")
        return redirect('/cust_profile')
    else:
        sid = request.session['lid']
        sho = customer.objects.get(login_id_id=sid)
        return render(request, 'customer/customer_update_profile.html', {'data': sho})


def cust_change_pass(request):
    if request.method == 'POST':
        sid = request.session['lid']
        db = login.objects.get(id=sid)

        oldpasswd = request.POST['oldPassword']
        newpasswd = request.POST['passwordFile']
        conpasswd = request.POST['password2']

        if db.password != oldpasswd:
            messages.error(request, "Incorrect Password")
            return redirect('/cust_change_password')

        elif newpasswd != conpasswd:
            messages.error(request, "Password Mismatch")
            return redirect('/cust_change_password')
        else:
            obj = customer.objects.filter(login_id_id=sid)
            obj.update(password=newpasswd)

            db = login.objects.filter(id=sid)
            db.update(password=newpasswd)

            messages.success(request, "Password Changed")
            return redirect('/cust_profile')
    else:
        return render(request, 'customer/customer_change_pass.html')


def send_comp(request):
    if request.method == 'POST':
        sid = request.session['lid']
        comp = request.POST['complaint']
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        cust = customer.objects.get(login_id_id=sid)

        obj = complaint()
        obj.complaint = comp
        obj.date = date
        obj.reply = 'pending'
        obj.reply_date = date
        obj.cust_id_id = cust.id
        obj.save()

        messages.success(request, "Complaint Send")
        return redirect('/send_complaint')
    else:
        return render(request, 'customer/send_complaint.html')


def send_feed(request):
    if request.method == 'POST':
        sid = request.session['lid']
        feed = request.POST['feedback']
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        cust = customer.objects.get(login_id_id=sid)

        obj = feedback()
        obj.feedback = feed
        obj.date = date
        obj.cust_id_id = cust.id
        obj.save()

        messages.success(request, "Feedback Send")
        return redirect('/send_feedback')
    else:
        return render(request, 'customer/send_feedback.html')


# ========================================================================================
#                              ANDROID USER MODULE
# ====================================================================================

def android_user_reg(request):
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    pict = request.FILES['pic']
    date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
    fs = FileSystemStorage()
    fs.save(r"C:\Users\ruzai\PycharmProjects\E-commerce_Website\shop\static\customer\img\\" + date + '.jpg', pict)
    path = "/static/customer/img/" + date + '.jpg'
    dob = request.POST['dob']
    gend = request.POST['gender']
    number = request.POST['phone']
    email = request.POST['email']
    pas = request.POST['password']

    qry = login.objects.filter(username=email)

    if qry.exists():
        return JsonResponse({"status": "exist"})
    else:
        obj = login()
        obj.username = email
        obj.password = pas
        obj.u_type = 'customer'
        obj.save()

        cus = customer()
        cus.name = name
        cus.place = place
        cus.post = post
        cus.pin = pin
        cus.photo = str(path)
        cus.dob = dob
        cus.gender = gend
        cus.email = email
        cus.phone_number = number
        cus.password = pas
        cus.login_id = obj
        cus.save()

    return JsonResponse({"status": "ok"})


def android_login(request):
    email = request.POST['id']
    password = request.POST['passwd']
    qry = login.objects.filter(username=email, password=password)

    if qry.exists():
        qry = qry[0]
        return JsonResponse({"status": "ok", "type": qry.u_type, "lid": qry.id})
    else:
        return JsonResponse({"status": "no"})


def android_view_shop(request):
    # qry = list(shop.objects.values())
    qry = shop.objects.filter(shop_id__u_type='shop')
    ar = []
    for i in qry:
        ar.append({"id": i.shop_id_id, "photo": i.photo, "name": i.name, "place": i.place, "post": i.post, "pin": i.pin,
                   "email": i.email,
                   "phone_number": i.phone_number})
    return JsonResponse({"status": "ok", "data": ar})


def android_view_shop_product(request):
    sid = request.POST['sid']

    qry = products.objects.filter(shop_id_id=sid)
    ar = []
    for i in qry:
        ar.append({"photo": i.photo, "name": i.name, "price": i.price, "stock": i.stock, "product_id": i.id})
    return JsonResponse({"status": "ok", "data": ar})


def android_view_product(request):
    qry = products.objects.all()
    ar = []
    for i in qry:
        ar.append({"photo": i.photo, "name": i.name, "price": i.price, "stock": i.stock, "product_id": i.id})
    return JsonResponse({"status": "ok", "data": ar})


def android_add_cart(request):
    sid = request.POST['id']
    stat = 'Add to Cart'
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    # q = request.POST['quantity']
    pro = request.POST['product_id']

    qry = master.objects.filter(cust_id__login_id=sid)
    cust = customer.objects.get(login_id=sid)
    book = order.objects.filter(master_id__cust_id__login_id=sid)
    order_dbb = order.objects.filter(master_id__cust_id__login_id=sid)
    product_dbb = order_dbb.filter(product_id=pro)
    carts = product_dbb.filter(master_id__status='Add to Cart')

    if qry.exists():

        if qry.filter(status='Booked').exists() and not qry.filter(status='Add to Cart').exists():
            mast = master()
            mast.status = stat
            mast.date = date
            mast.cust_id_id = cust.id
            mast.save()

            db = order()
            db.quantity = 1
            db.date = date
            db.master_id_id = mast.id
            db.product_id_id = pro
            db.save()

        elif not qry.filter(status='Add to Cart').exists():
            mast = master()
            mast.status = stat
            mast.date = date
            mast.cust_id_id = cust.id
            mast.save()

            db = order()
            db.quantity = 1
            db.date = date
            db.master_id_id = mast.id
            db.product_id_id = pro
            db.save()

        elif carts.filter(product_id=pro).exists():
            order_db = order.objects.filter(master_id__cust_id__login_id=sid)
            product_db = order_db.filter(product_id=pro)
            cart = product_db.filter(master_id__status='Add to Cart')
            cart.update(quantity=F('quantity') + 1)

        else:
            obj = master.objects.filter(cust_id__login_id=sid)
            cart = obj.filter(status='Add to Cart')
            order_db = qry.filter(status='Add to Cart')

            mast = cart.get(id=order_db.first().id)

            obj.update(date=date)

            db = order()
            db.quantity = 1
            db.date = date
            db.master_id_id = mast.id
            db.product_id_id = pro
            db.save()

    else:
        obj = master()
        obj.status = stat
        obj.date = date
        obj.cust_id_id = cust.id
        obj.save()

        db = order()
        db.quantity = 1
        db.date = date
        db.master_id_id = obj.id
        db.product_id_id = pro
        db.save()

    return JsonResponse({"status": "ok"})


def android_view_cart(request):
    sid = request.POST['id']
    qry = order.objects.filter(master_id__cust_id__login_id=sid)
    cart = qry.filter(master_id__status='Add to Cart')

    prod = []
    for i in range(0, len(cart)):
        total = float(cart[i].product_id.price) * float(cart[i].quantity)
        prod.append(total)

    total = sum(prod)

    ar = []
    for i in cart:
        ar.append(
            {"name": i.product_id.name, "price": i.total_price(), "photo": i.product_id.photo,
             "quantity": i.quantity, "total": total, "order_id": i.id})

    return JsonResponse({"status": "ok", "data": ar})


def android_add_quantity(request):
    oid = request.POST['order_id']
    qnt = request.POST['quantity']
    quant = int(qnt) + 1
    order_db = order.objects.filter(id=oid)
    order_db.update(quantity=quant)

    return JsonResponse({"status": "ok"})


def android_remove_quantity(request):
    oid = request.POST['order_id']
    qnt = request.POST['quantity']
    quant = int(qnt) - 1
    order_db = order.objects.filter(id=oid)

    if quant > 0:
        order_db.update(quantity=quant)
    else:
        order_db.delete()

    return JsonResponse({"status": "ok"})


def android_remove_cart(request):
    oid = request.POST['order_id']
    order.objects.filter(id=oid).delete()

    return JsonResponse({"status": "ok"})


def android_cart_checkout(request):
    lid = request.POST['id']
    stat = 'Booked'
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    obj = master.objects.filter(cust_id__login_id=lid)
    obj.update(status=stat)
    obj.update(date=date)

    return JsonResponse({"status": "ok"})


def android_view_order(request):
    lid = request.POST['id']
    # qry = list(shop.objects.values())

    qry = order.objects.filter(master_id__cust_id__login_id=lid)
    ar = []
    for i in qry:
        ar.append({"pid": i.product_id.id, "photo": i.product_id.photo, "name": i.product_id.name,
                   "quantity": i.quantity, "price": i.total_price(), "date": i.date})
    return JsonResponse({"status": "ok", "data": ar})


def android_review(request):
    lid = request.POST['id']
    pid = request.POST['pid']
    rev = request.POST['rev']
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    cust = customer.objects.get(login_id_id=lid)
    qry = order.objects.filter(product_id=pid)

    db = reviews()
    db.date = date
    db.review = rev
    db.cust_id_id = cust.id
    db.order_id_id = qry.first().id
    db.save()

    return JsonResponse({"status": "ok"})


def android_view_reviews(request):
    pid = request.POST['pid']
    qry = reviews.objects.filter(order_id__product_id=pid)
    print(pid)

    if qry.exists():
        ar = []
        for i in qry:
            ar.append({"photo": i.order_id.product_id.photo, "name": i.order_id.product_id.name, "review": i.review,
                       "date": i.date})
    else:
        return JsonResponse({"status": "no"})

    return JsonResponse({"status": "ok", "data": ar})


def android_complaint(request):
    lid = request.POST['id']
    comp = request.POST['comp']
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    cust = customer.objects.get(login_id_id=lid)

    obj = complaint()
    obj.complaint = comp
    obj.date = date
    obj.reply = 'pending'
    obj.reply_date = date
    obj.cust_id_id = cust.id
    obj.save()

    return JsonResponse({"status": "ok"})


def android_view_reply(request):
    lid = request.POST['id']
    qry = complaint.objects.filter(cust_id__login_id=lid)

    ar = []
    for i in qry:
        ar.append({"complaint": i.complaint, "date": i.date, "reply": i.reply, "reply_date": i.reply_date})
    return JsonResponse({"status": "ok", "data": ar})


def android_feedback(request):
    lid = request.POST['id']
    feed = request.POST['feed']
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    cust = customer.objects.get(login_id_id=lid)

    obj = feedback()
    obj.feedback = feed
    obj.date = date
    obj.cust_id_id = cust.id
    obj.save()

    return JsonResponse({"status": "ok"})


def android_view_profile(request):
    lid = request.POST['id']
    qry = customer.objects.filter(login_id_id=lid)

    ar = []
    for i in qry:
        ar.append(
            {"photo": i.photo, "name": i.name, "email": i.email, "phone": i.phone_number, "place": i.place,
             "post": i.post, "pin": i.pin, "dob": i.dob, "gender": i.gender})
    return JsonResponse({"status": "ok", "data": ar})


def android_change_password(request):
    lid = request.POST['id']
    db = login.objects.get(id=lid)

    oldpasswd = request.POST['old']
    newpasswd = request.POST['new']
    conpasswd = request.POST['con']

    if db.password != oldpasswd:
        return JsonResponse({"status": "incorrect"})

    elif newpasswd != conpasswd:
        return JsonResponse({"status": "mismatch"})

    else:
        obj = customer.objects.filter(login_id_id=lid)
        obj.update(password=newpasswd)

        db = login.objects.filter(id=lid)
        db.update(password=newpasswd)

        return JsonResponse({"status": "ok"})


def android_update_profile(request):
    lid = request.POST['id']
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    pict = request.FILES['pic']
    date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
    fs = FileSystemStorage()
    fs.save(r"C:\Users\ruzai\PycharmProjects\E-commerce_Website\shop\static\pic\customer\\" + date + '.jpg', pict)
    path = "/static/pic/customer/" + date + '.jpg'
    email = request.POST['email']
    number = request.POST['phone']
    dob = request.POST['dob']
    gen = request.POST['gender']

    obj = customer.objects.filter(login_id=lid)
    obj.update(name=name)
    obj.update(place=place)
    obj.update(post=post)
    obj.update(pin=pin)
    obj.update(photo=path)
    obj.update(email=email)
    obj.update(phone_number=number)
    obj.update(dob=dob)
    obj.update(gender=gen)

    lo = login.objects.filter(id=lid)
    lo.update(username=email)

    return JsonResponse({"status": "ok"})
