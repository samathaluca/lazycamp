from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_basket(request):
    """A View that renders the basket contents page"""
    return render(request, "basket.html")


def add_to_basket(request, id):
    """Add a quantity of the specified product to the basket"""
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})
    basket[id] = basket.get(id, quantity)

    request.session['basket'] = basket
    return redirect(reverse('index'))


def adjust_basket(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[id] = quantity
    else:
        basket.pop(id)
    
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))from django.shortcuts import render

# Create your views here.
