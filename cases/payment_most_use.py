from services.orders import Order


def get_order_payments():
    '''get_order_payments will fetch payment counts by order
    '''
    payments = Order.get_order_payment().sort_values(by="total", ascending=False)
    payments["total"].dropna()

    # Returning TOP - 3 Data for plotting
    return payments.head(n=3)
