from django.shortcuts import get_object_or_404
from courses.models import Course
from food_order.models import Food_order


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total_food_order = 0
    total_course = 0
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        course = get_object_or_404(Course, pk=id)
        food_order = get_object_or_404(Food_order, pk=id)
        total_course += quantity * course.price
        total_food_order += quantity * food_order.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'course': course, 'food_order':food_order})

    total = total_course + total_food_order
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}