import requests
import library_save_method
from lxml import etree
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}
while True:
    kw = input('Enter keywords: ')
    url = f'https://openlibrary.org/search?q={kw}&mode=everything'
    # print(url)
    response = requests.get(url=url, headers=headers)
    # print(response.text)
    tree = etree.HTML(response.text)
    tips = tree.xpath('//div[@class="red"]')
    if tips:
        print('No result found, please change a word: ')
        continue
    else:
        last_page = tree.xpath('//a[@data-ol-link-track="Pager|LastPage"]/text()')[0]
        print(f'Total: {last_page} pages')
        try:
            page_num = int(input('How many pages you want: '))
            page_num = min(page_num, int(last_page))
        except ValueError:
            print("Invalid number.")
            continue
        all_pages_data = {}
        for page in range(1, page_num + 1):
            url1 = f'https://openlibrary.org/search?q={kw}&mode=everything&page={page}'
            response1 = requests.get(url=url1, headers=headers)
            tree1 = etree.HTML(response1.text)
            div = tree1.xpath('//div[@class="details"]')
            page_data = []
            for i in div:
                title = i.xpath('.//a[@class = "results"]/text()')
                title = title[0] if title else 'No title information'
                writer = ''.join(i.xpath('.//span[@class = "bookauthor"]//text()')).replace('by', '').replace('\n','').replace(' ', '').replace('and', '&')
                writer = writer if writer else 'No writer information'
                want_to_read = i.xpath('(.//span[@class = "ratingsByline"])[2]/text()')
                want_to_read = want_to_read[0] if want_to_read else 'No want_to_read information'
                score = i.xpath('.//span[@itemprop="ratingValue"]/text()')
                score = score[0] if score else 'No score information'
                link = i.xpath('.//a[@class = "results"]/@href')
                link = 'https://openlibrary.org/' + link[0] if link else 'No link information'
                print(f'Title:{title}; Writer: {writer}; {want_to_read}; Score: {score}; Link: {link}')
                page_data.append({
                    'title': title,
                    'writer': writer,
                    'want_to_read': want_to_read,
                    'score': score,
                    'link': link
                })
            print(f'{page} page finished')
            all_pages_data[page] = page_data
        while True:
            save_way = input('Please choose your save method(excel/csv):').lower()
            if save_way == 'excel':
                library_save_method.excel_method(kw, all_pages_data)
                break
            elif save_way == 'csv':
                library_save_method.csv_method(kw, all_pages_data)
                break
            # elif save_way =='googlesheet':
            #     library_save_method.google_method(kw, all_pages_data)
            #     break
            else:
                print('Wrong information. Please choose your save method(excel/csv)')
        break

