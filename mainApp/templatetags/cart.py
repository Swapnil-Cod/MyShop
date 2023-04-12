from django import template
register = template.Library()
from mainApp.models import Product

@register.filter('cartQuantity')
def cartQuantity(request, id):
    cart = request.session.get('cart', None)
    for key,value in cart.items():
        if key==str(id):
            return value
        
@register.filter('cartFinal')
def cartFinal(request, id):
    cart = request.session.get('cart', None)
    for key,value in cart.items():
        if key==str(id):
            p = Product.objects.get(id=id)
            return value*p.finalprice
