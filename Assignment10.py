import pandas as pd


def create_data() -> pd.DataFrame:
    data = [
        ['Laptop'   , 'Electronics', 75000, 12],
        ['Mouse'    , 'Electronics', 899  , 150],
        ['Desk'     , 'Furniture'  , 12000, 25],
        ['Chair'    , 'Furniture'  , 8500 , 40],
        ['Monito'   , 'Electronics', 22000, 30],
        ['Bookshelf', 'Furniture'  , 6500 , 18],
        ['Keyboard' , 'Electronics', 2499 , 85],
        ['Lamp'     , 'Home'       , 1200 , 60],
        ['Pillow'   , 'Home'       , 799  , 200],
        ['Rug'      , 'Home'       , 3500 , 35]
    ]
    return pd.DataFrame(
        data = data,
        columns = ['product', 'category', 'price', 'units_sold']
    )


def main():
    products = create_data()
    print("=" * 50)
    print(products)
    print("=" * 50)
    products_with_price_above_5000 = products[products['price'] > 5000]
    print(products_with_price_above_5000)
    print("=" * 50)
    sorted_products = products_with_price_above_5000.sort_values(by='price', ascending=False).reset_index().drop(columns='index')
    print("=" * 50)
    print(sorted_products)
    print("=" * 50)
    products['discounted_price'] = products['price'] * 0.9
    print(products[['product', 'price', 'discounted_price']])
    print("=" * 50)
    products.dropna()


if __name__ == '__main__':
    main()


