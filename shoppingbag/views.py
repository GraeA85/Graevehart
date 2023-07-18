from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_shoppingbag(request):
    """ A view that renders the shoppingbag contents page """
    page_name = "Your Cart"
    page_description = "Your checkout shoppingbag"
    context = {'page_name': page_name, 'page_description': page_description}
    return render(request, 'shoppingbag/shoppingbag.html', context)


def add_to_shoppingbag(request, item_id):
    """ Add a quantity of the specified product to the shopping shoppingbag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoppingbag = request.session.get('shoppingbag', {})

    if item_id in list(shoppingbag.keys()):
        shoppingbag[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {shoppingbag[item_id]}'
        )
    else:
        shoppingbag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your shoppingbag')

    request.session['shoppingbag'] = shoppingbag
    return redirect(redirect_url)


def adjust_shoppingbag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = request.POST.get('quantity')

    # Allows the user to delete the number from the quantity box
    if quantity and quantity.isdigit() and int(quantity) > 0:
        shoppingbag = request.session.get('shoppingbag', {})
        shoppingbag[item_id] = int(quantity)
        messages.success(
            request, f'Changed quantity of {product.name} in your shoppingbag')
    else:
        shoppingbag = request.session.get('shoppingbag', {})
        shoppingbag.pop(item_id, None)
        messages.success(request, f'Removed {product.name} from your shoppingbag')

    request.session['shoppingbag'] = shoppingbag
    return redirect(reverse('view_shoppingbag'))


def remove_from_shoppingbag(request, item_id):
    """Remove the item from the shopping shoppingbag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        shoppingbag = request.session.get('shoppingbag', {})
        shoppingbag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your shoppingbag')

        request.session['shoppingbag'] = shoppingbag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)