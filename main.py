import matplotlib.pyplot as plt
from cases import city_with_most_order, product_category_with_most_order, payment_most_use, seller_with_highest_rating, city_with_most_seller

# Cases 1 - City with most orders - TOP 5
# city_with_most_order.get_customers_count_by_city().plot(
#     kind="bar", x="customer_city", y="count").set_title("Cases 1 - City with most orders - TOP 5")
# plt.show()

# ------------------------------------------------------------------------------------------------------

# Cases 2 - Top 5 Product Category with the most order
# product_category_with_most_order.get_orders_categories_by_product_count().plot(
#     kind="bar", x="product_category_name", y="total").set_title("Cases 2 - Top 5 Product Category with the most order")
# plt.show()

# ------------------------------------------------------------------------------------------------------

# Cases 3 - Top 3 Payment type that is used
# payment_most_use.get_order_payments().plot(
#     kind="bar", x="payment_type", y="total").set_title("Cases 3 - Top 3 Payment type that is used")
# plt.show()

# ------------------------------------------------------------------------------------------------------

# Cases 4 - Top 5 Seller with highest rating
# seller_with_highest_rating.get_seller_count_product_total().plot(
#     kind="bar", x="seller_id", y="total").set_title("Cases 4 - Top 5 Seller with highest rating")
# plt.show()

# ------------------------------------------------------------------------------------------------------

# Cases 5 - Top 5 City with the most seller that selling
# city_with_most_seller.get_city_most_seller().plot(
#     kind="bar", x="seller_city", y="total").set_title("Cases 4 - Top 5 Seller with highest rating")
# plt.show()
