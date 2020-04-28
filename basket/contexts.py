from django.shortcuts import get_object_or_404
from campspot.models import campme


def basket_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    basket = request.session.get('basket', {})

    basket_items = []
    total = 0
    campspot_count = 0
    
    for id, quantity in basket.items():
        campspot = get_object_or_404(campme, pk=id)
        total += quantity * campspot.price
        campspot_count += quantity
        basket_items.append({'id': id, 'quantity': quantity, 'campspot': campspot})
    
    return {'basket_items': basket_items, 'total': total, 'campspot_count': campspot_count}