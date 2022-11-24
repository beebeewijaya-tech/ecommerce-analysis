from services.customers import Customer
from services.orders import Order


def get_customers_count_by_city():
    '''get_customers_count_by_city will fetch get customers and city data from SQL that already use INNER JOIN in the query
    and will merge into orders data and aggregating using count
    '''
    customers = Customer.get_customers_and_city()
    order = Order.get_orders()

    customer_order = customers.merge(order, on="customer_id", how="left")
    customer_order.fillna(0)

    customer_grouped = customer_order.groupby(
        "customer_city")["customer_id"].count().sort_values(ascending=False).reset_index(name="count")

    # Returning TOP - 5 Data for plotting
    return customer_grouped.head(n=5)
