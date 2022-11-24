from services.seller import Seller


def get_city_most_seller():
    '''get_city_most_seller will fetch count of seller from city
    '''
    seller = Seller.get_seller_city_total().sort_values(by="total", ascending=False)
    seller["total"].dropna()

    # Returning TOP - 5 Data for plotting
    return seller.head(n=5)
