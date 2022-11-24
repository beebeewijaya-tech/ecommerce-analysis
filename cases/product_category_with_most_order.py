from services.product import Product


def get_orders_categories_by_product_count():
    '''get_orders_categories_by_product_count will fetch categories count on each product that being orders
    '''
    categories = Product.get_products_categories_by_order_count()

    categories["total"].dropna()

    # Returning TOP - 5 Data for plotting
    return categories.head(n=5)
