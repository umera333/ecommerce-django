from django.shortcuts import render, redirect
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'store/product_detail.html', {'product': product})


def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    grand_total = 0

    for product in products:
        quantity = cart.get(str(product.id), 0)
        total = product.price * quantity
        grand_total += total

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': total
        })

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'grand_total': grand_total
    })



def increase(request, id):
    cart = request.session.get('cart', {})
    cart[str(id)] = cart.get(str(id), 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')


def decrease(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        if cart[str(id)] > 1:
            cart[str(id)] -= 1
        else:
            del cart[str(id)]

    request.session['cart'] = cart
    return redirect('view_cart')


def remove(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart
    return redirect('view_cart')
