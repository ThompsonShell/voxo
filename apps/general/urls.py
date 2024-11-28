from django.urls import path
from .views import (
    HomeView,
    users,
    order_list,
    order_detail,
    order_tracking,
    AddNewProductView,
    all_users,
    coupon_list,
    CreateCouponView,
    CreateMenuView,
    currency_rates,
    forgot_password,
    invoice,
    list_page,
    login,
    menu_lists,
    product_review,
    products,
    profile_setting,
    reports,
    sign_up,
    support_ticket,
    taxes,
    AddNewUserView,
    translation,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    #======== URLS ========

    path('users/', users, name='users'),
    path('add-new-user', AddNewUserView.as_view(), name='add_new_user'),
    #======== URLS ========

    path('add-new-product/', AddNewProductView.as_view(), name='add-new-product'),
    path('all-users/', all_users, name='all-users'),

    # ======== URLS ========
    path('coupon-list/', coupon_list, name='coupon-list'),
    path('create-coupon/', CreateCouponView.as_view(), name='create-coupon'),

    # ======== URLS ========

    path('create-menu/', CreateMenuView.as_view(), name='create-menu'),

    # ======== URLS ========
    path('currency-rates/', currency_rates, name='currency-rates'),

    # ======== URLS ========
    path('forgot-password/', forgot_password, name='forgot-password'),

    # ======== URLS ========
    path('invoice/', invoice, name='invoice'),
    # ======== URLS ========
    path('list-page/', list_page, name='list-page'),

    # ======== URLS ========
    path('login/', login, name='login'),

    # ======== URLS ========
    path('order-detail/', order_detail, name='order-detail'),
    path('order-tracking/', order_tracking, name='order-tracking'),
    path('order-list/', order_list, name='order-list'),

    # ======== URLS ========
    path('menu-lists/', menu_lists, name='menu-lists'),

    # ======== URLS ========
    path('products/', products, name='products'),
    path('product-review/', product_review, name='product-review'),


    # ======== URLS ========
    path('profile-setting/', profile_setting, name='profile-setting'),

    # ======== URLS ========
    path('reports/', reports, name='reports'),

    # ======== URLS ========
    path('sign-up/', sign_up, name='sign-up'),

    # ======== URLS ========
    path('support-ticket/', support_ticket, name='support-ticket'),
    # ======== URLS ========
    path('taxes/', taxes, name='taxes'),

    # ======== translation URLS ========
    path('translation/', translation, name='translation'),
]

