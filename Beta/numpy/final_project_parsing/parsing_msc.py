import requests
from selectolax.parser import HTMLParser
import time

def get_html(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'ru,en;q=0.9,es;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'u=2xpol28i.m2jz6v.1ad2i750ywb00; _ym_uid=1673775150460749733; buyer_laas_location=637640; buyer_location_id=637640; sessid=be073a17fbde3b655cc843f26607f687.1719310324; auth=1; cfidsw-avito=+EvgP1r/n7VR+scB/B3KBO7piVrN+VJmDzyPtz85hiimOnK72NYykcU92LVU9ilh4FzOscHL0ABzkd0XlSHgTFsQFEG4gfyd0LAh6UHz6HkuQPa+qxrhB25WSX00qqcCq7bh5/lJeJH1EzYT3ArJZknwAab7IKhqZHnY; srv_id=wN2SruMhJjmjrAUT.qhfs61cQKCcHBmUI9xVT9tHZD-1qA5f-aq6uNKwoN7gB4SwnjXYIFU10v4tAcCkO07tA.wROuhC_1RqJjf91prPCeEJ4Ru2-AR8QyaQWvmtKtknk=.web; _ym_d=1728659371; luri=moskva; _gcl_au=1.1.25628145.1732519088; gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; _ym_isad=2; _ga=GA1.1.925179822.1732519089; tmr_lvid=6edb2d5fb947a4ccf291d65aae284e2d; tmr_lvidTS=1673775123511; adrcid=AZb-_NTMMv8YC1s0B9Hxx1Q; adrcid=AZb-_NTMMv8YC1s0B9Hxx1Q; acs_3=%7B%22hash%22%3A%22768a608b20ce960ff29026da95a81203ec583ad1%22%2C%22nextSyncTime%22%3A1732605490008%2C%22syncLog%22%3A%7B%22224%22%3A1732519090008%2C%221228%22%3A1732519090008%2C%221230%22%3A1732519090008%7D%7D; acs_3=%7B%22hash%22%3A%22768a608b20ce960ff29026da95a81203ec583ad1%22%2C%22nextSyncTime%22%3A1732605490008%2C%22syncLog%22%3A%7B%22224%22%3A1732519090008%2C%221228%22%3A1732519090008%2C%221230%22%3A1732519090008%7D%7D; domain_sid=ShSWLbdGCLeXM90y06Yu-%3A1732519090676; cookie_consent_shown=1; f=5.88881e344776caaa4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa1a2a574992f83a9246b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8cad08e7e7eb412c8fa4d7ea84258c63d74c4a16376f87ccd915ac1de0d034112f12b79bbb67ac37d46b8ae4e81acb9fae2415097439d4047fb0fb526bb39450a46b8ae4e81acb9fa34d62295fceb188dd99271d186dc1cd03de19da9ed218fe2d50b96489ab264edd50b96489ab264edd50b96489ab264ed46b8ae4e81acb9fa38e6a683f47425a8352c31daf983fa077a7b6c33f74d335c76ff288cd99dba46f90b7496c3b979e21d49c1c93fcdfd74870f8220644391406a147b064057723717c7721dca45217b3f0b0f8d41ffdf2441992e6d9b995b67e2415097439d404746b8ae4e81acb9fa786047a80c779d5146b8ae4e81acb9faee48ba6bae41dcbb71e7cb57bbcb8e0f2da10fb74cac1eabf142afafcb3cfa297a4873958d8deff2312f8fecc8ca5e543486a07687daa291; ft="VJ0u5eftaWojMDfG8/ZiMAXJYGzbLbH7LlllObKSYExBf6rZMNl8gvsUOtdFgAkVbM9Rcwkd7+2aGHT4il5pmQ9wc7PFE7iHL8B7kC2LzQqsC1DRSEWUkV5IPBe716pDUFDz4nbpppGpeWfhLdk7H7E5QZ5mA64CDKjVMACQ4QaDtaucMpIsrn+U203YW1o2"; ma_vis_id_last_sync_3485699018=1732519093526; ma_prevVisId_3485699018=255a40119036a973e8f0ca41fe34b455; __ai_fp_uuid=9b408bdce6964b37%3A2; __upin=ylnokj1EcQQe3O66jXhmww; uxs_uid=705d5f70-aafd-11ef-9ec5-43810f5b728e; _buzz_fpc=JTdCJTIydmFsdWUlMjIlM0ElN0IlMjJ1ZnAlMjIlM0ElMjIxMjc5MjI4ZWI5NDNlNTE3ZjMwY2U1MTFkNGFjOTJjNCUyMiUyQyUyMmJyb3dzZXJWZXJzaW9uJTIyJTNBJTIyMjQuMTAlMjIlMkMlMjJ0c0NyZWF0ZWQlMjIlM0ExNzMyNTE5MDkyNTAwJTdEJTJDJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyVHVlJTJDJTIwMjUlMjBOb3YlMjAyMDI1JTIwMDclM0ExOCUzQTE3JTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlN0Q=; _buzz_aidata=JTdCJTIydmFsdWUlMjIlM0ElN0IlMjJ1ZnAlMjIlM0ElMjJ5bG5va2oxRWNRUWUzTzY2alhobXd3JTIyJTJDJTIyYnJvd3NlclZlcnNpb24lMjIlM0ElMjIyNC4xMCUyMiUyQyUyMnRzQ3JlYXRlZCUyMiUzQTE3MzI1MTkwOTU3MjUlN0QlMkMlMjJwYXRoJTIyJTNBJTIyJTJGJTIyJTJDJTIyZG9tYWluJTIyJTNBJTIyLnd3dy5hdml0by5ydSUyMiUyQyUyMmV4cGlyZXMlMjIlM0ElMjJUdWUlMkMlMjAyNSUyME5vdiUyMDIwMjUlMjAwNyUzQTE4JTNBMTclMjBHTVQlMjIlMkMlMjJTYW1lU2l0ZSUyMiUzQSUyMkxheCUyMiU3RA==; _buzz_mtsa=JTdCJTIydmFsdWUlMjIlM0ElN0IlMjJ1ZnAlMjIlM0ElMjIyNTVhNDAxMTkwMzZhOTczZThmMGNhNDFmZTM0YjQ1NSUyMiUyQyUyMmJyb3dzZXJWZXJzaW9uJTIyJTNBJTIyMjQuMTAlMjIlMkMlMjJ0c0NyZWF0ZWQlMjIlM0ExNzMyNTE5MDkzNTMwJTdEJTJDJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyVHVlJTJDJTIwMjUlMjBOb3YlMjAyMDI1JTIwMDclM0ExOCUzQTE3JTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlN0Q=; adjust_links=adgroup%3Dperf_yd_c2c_real_resid_web_sea_b_150923_accom_other%26campaign%3Dyandex%26creative%3D---autotargeting; utm_source_ad=yandex; v=1732563380; adrdel=1732563406802; adrdel=1732563406802; _ym_visorc=b; SEARCH_HISTORY_IDS=1%2C%2C4%2C3; _ga_WW6Q1STJ8M=GS1.1.1732565055.1.0.1732565055.0.0.0; _ga_ZJDLBTV49B=GS1.1.1732565055.1.0.1732565055.0.0.0; ma_cid=7749971991732565059; ma_id=1979407311732565089718; ma_ss_64a8dba6-67f3-4fe4-8625-257c4adae014=6603710641732565059.1.1732565127.16; cartCounter=0; sx=H4sIAAAAAAAC%2F1TQwU5bOxDG8Xfx%2BizsscczZhkO4ZJbErWkSZud7RkrnAa1CAih6Lx7xSJReIGfvu%2F%2FbrzV4qs0FMHigTSFQI6lEIfWxJqLd7M3F8a99rT3z4ubaZ9p%2BCumM2ouHHmIFkPEsTM%2BaynqmJuLTlVUNEds4hoD11SOlC%2FT%2B5ndzMr6Zfk1bDZnFIDlNHYGM5LzhUNNAAlTzlKbU0kuqEY6Uf8N69efN7jpJ1fzw9N8dUahRfhYhQLiKRXFhp7BSynM0VKpNSCEeKTue7z8tnz7HXd3%2B8WwaeeUA2vHzkQI1nmBGqUIEKv3yikixwgxuhP1v0y20xUftsPil59P6xkVEvEHRRGl1GqpUU6SULyLzKKQXWOy7khN7p7nfVzWB7%2Bjmz%2B3h8%2FZicfO1Aa5cQueSkHiJGRRq2Ml9VBdOFKX22H18Hj9hrsv2fWPs8%2BtfBg7o64WQF8Rc%2FLZauSmlQtxIhCOp4O3k6Lf03UtV%2BHlaVj%2FOKeACcbxXwAAAP%2F%2F0b1NdFkCAAA%3D; dfp_group=11; isLegalPerson=0; abp=0; pageviewCount=17; _ga_M29JC28873=GS1.1.1732563406.4.1.1732566498.58.0.0; tmr_detect=0%7C1732566501964',
        'if-none-match': 'W/"2a56eb-TqA2P2zxIk46PmEPz/wKDqu3vcA"',
        'priority': 'u=0, i',
        'referer': 'https://www.avito.ru/moskva/kvartiry/prodam/1-komnatnye-ASgBAgICAkSSA8YQygiAWQ?context=H4sIAAAAAAAA_wEjANz_YToxOntzOjg6ImZyb21QYWdlIjtzOjc6ImNhdGFsb2ciO312FITcIwAAAA&s=104',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "YaBrowser";v="24.10", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36'
    }
    
    with requests.Session() as session:
        session.headers.update(headers)
        session.get('https://www.avito.ru')
        response = session.get(url)
    
        if response.status_code == 200:
            html = response.text
            tree = HTMLParser(html)
            items = tree.css('div[data-marker="item"]')
            
            index = 0
            for item in items:
                index += 1
                print(index, item.css_first('h3').text())
        else: 
            print(f"Error: {response.status_code}")
    

def main():
    url = 'https://www.avito.ru/moskva/kvartiry/prodam/1-komnatnye-ASgBAgICAkSSA8YQygiAWQ?context=H4sIAAAAAAAA_wEjANz_YToxOntzOjg6ImZyb21QYWdlIjtzOjc6ImNhdGFsb2ciO312FITcIwAAAA&f=ASgBAgECAkSSA8YQygiAWQFFxpoMHXsiZnJvbSI6MTAwMDAwMCwidG8iOjcwMDAwMDB9&s=104'
    get_html(url)
    
if __name__ == '__main__':
    main()

