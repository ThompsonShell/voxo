from django.shortcuts import render
from django.views.generic import TemplateView, View


# def home(request):
#     return render(request, 'index.html')


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


def users(request):
    return render(request, 'pages/all-users.html')

# def add_user(request):
#     return render(request, 'pages/add-new-user.html')
#
# def orders(request):
#     return render(request, 'pages/order-list.html')
#
# def order_detail(request):
#     return render(request, 'pages/order-detail.html')
#
# def order_tracking(request):
#     return render(request, 'pages/order-tracking.html')
#
# def vendors(request):
#     return render(request, 'pages/vendor-list.html')
#
# def add_vendor(request):
#     return render(request, 'pages/create-vendor.html')




# Function-based views
def add_new_product(request):
    return render(request, 'pages/add-new-product.html')

def add_new_user(request):
    return render(request, 'pages/add-new-user.html')

def all_users(request):
    return render(request, 'pages/all-users.html')

def coupon_list(request):
    return render(request, 'pages/coupon-list.html')

def create_coupon(request):
    return render(request, 'pages/create-coupon.html')

def create_menu(request):
    return render(request, 'pages/create-menu.html')

def create_vendor(request):
    return render(request, 'pages/create-vendor.html')

def currency_rates(request):
    return render(request, 'pages/currency-rates.html')

def forgot_password(request):
    return render(request, 'pages/forgot-password.html')

def invoice(request):
    return render(request, 'pages/invoice.html')

def list_page(request):
    return render(request, 'pages/list-page.html')

def login(request):
    return render(request, 'pages/login.html')

def menu_lists(request):
    return render(request, 'pages/menu-lists.html')

def order_detail(request):
    return render(request, 'pages/order-detail.html')

def order_list(request):
    return render(request, 'pages/order-list.html')

def order_tracking(request):
    return render(request, 'pages/order-tracking.html')

def product_review(request):
    return render(request, 'pages/product-review.html')

def products(request):
    return render(request, 'pages/products.html')

def profile_setting(request):
    return render(request, 'pages/profile-setting.html')

def reports(request):
    return render(request, 'pages/reports.html')

def sign_up(request):
    return render(request, 'pages/sign-up.html')

def support_ticket(request):
    return render(request, 'pages/support-ticket.html')

def taxes(request):
    return render(request, 'pages/taxes.html')

def translation(request):
    return render(request, 'pages/translation.html')

def vendor_list(request):
    return render(request, 'pages/vendor-list.html')
