from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_products(category_url, pages=3):
    driver = webdriver.Chrome()  
    driver.get(category_url)
    products = []

    for page in range(1, pages + 1):
        print(f"Парсинг страницы {page}...")

        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".s-item")))

        product_cards = driver.find_elements(By.CSS_SELECTOR, ".s-item")
        for card in product_cards:
            try:
                name = card.find_element(By.CSS_SELECTOR, ".s-item__title").text
                price = card.find_element(By.CSS_SELECTOR, ".s-item__price").text
                item_id = card.get_attribute("data-view")
                products.append({"name": name, "price": price, "id": item_id})
            except Exception as e:
                print(f"Ошибка при парсинге товара: {e}")
                continue

        try:
            next_page = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".pagination__next"))
            )
            driver.execute_script("arguments[0].click();", next_page)
            time.sleep(3)  # Задержка для ожидания загрузки следующей страницы
        except Exception as e:
            print(f"Не удалось кликнуть по кнопке 'Next': {e}")
            break

    driver.quit()
    return products