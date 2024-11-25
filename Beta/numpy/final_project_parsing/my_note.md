1. Определить, какие элементы мы парсим:
- цена
- дата предложения
- сколько комнат, кв.м, этаж
- ссылка на квартиру

AVITO: url = 'https://www.avito.ru/moskva/kvartiry/prodam/1-komnatnye-ASgBAgICAkSSA8YQygiAWQ?context=H4sIAAAAAAAA_wEjANz_YToxOntzOjg6ImZyb21QYWdlIjtzOjc6ImNhdGFsb2ciO312FITcIwAAAA&f=ASgBAgECAkSSA8YQygiAWQFFxpoMHXsiZnJvbSI6MTAwMDAwMCwidG8iOjcwMDAwMDB9&s=104'

2. https://qna.habr.com/q/662475 - парсинг был невозможен, выходила ошибка 403.
То есть проходила блокировка. Сначала была попытка использовать больше headers, 
чтобы сымитировать get-запрос, но ошибка все равно оставалась. Тогда пришлось
прибегнуть к использование обхода Cloudfare.

Парсинг свежих объявлений в количестве 50 штук. -> def get_html(url): -> for item in items[:10]:
Я уменьшила до 10.