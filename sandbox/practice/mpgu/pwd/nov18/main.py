import pandas as pd
from ebay_parser import get_products

if __name__ == "__main__":
    category_url = "https://www.ebay.com/b/Computer-Components-Parts/175673/bn_1643095"

    products = get_products(category_url, pages=5)
    
    if products:
        df = pd.DataFrame(products)
        output_file = "ebay_products.csv"
        df.to_csv(output_file, index=False)
        print(f"Сохранено {len(products)} товаров в файл {output_file}")
    else:
        print("Не удалось получить данные о товарах.")
