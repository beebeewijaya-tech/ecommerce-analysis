from services.seller import Seller


def get_seller_count_product_total():
    '''get_seller_count_product_total will fetch count of product a seller has sells
    '''
    seller = Seller.get_seller_count_order().sort_values(by="total", ascending=False)
    seller["total"].dropna()

    # Returning TOP - 5 Data for plotting
    return seller.head(n=5)
