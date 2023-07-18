from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    shoppingbag = request.session.get('shoppingbag', {})
    if not shoppingbag:
        messages.error(request, "There's nothing in your shopping bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NIuDLCHimmDlHcqrwQFvPnRuLSEt0UJ9pO23vOWJNvPmJ651HKVJR0gUWbDJDRO3pMddktZF5xP3IlZ2Wd2ZB9v00SmHtFVQl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)