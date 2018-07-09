from django.dispatch import Signal

calculate_cart_total = Signal(providing_args=['instance'])