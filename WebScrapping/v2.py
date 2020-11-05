import csv
import errno
from socket import error as SocketError
import requests
from bs4 import BeautifulSoup
import concurrent.futures, time


MAX_THREADS = 30

def scrap(page):
    try:
        url = f"https://indopos.co.id/page/{page}/?s=corona"
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
        }
        results = requests.get(url, headers=header)
        status = results.status_code
        print(f'Scrapping halaman {page}\n')

        if status == 200:
            soup = BeautifulSoup(results.text, "html.parser")
            berita = soup.findAll('article', class_='type-post')

            beritas = []
            for be in berita:
                judul = be.find('h2', 'title').text.strip()
                tanggal = be.find('time', 'post-published updated').text.strip()
                try:
                    kategori = be.find('div', 'term-badges floated').text.strip()
                except AttributeError:
                    kategori = ''
                beritas.append([judul, tanggal, kategori, page])

            with open(r'results/berita_tanpa_batas.csv', 'a', newline='', encoding='utf-8') as file:
                for d in beritas:
                    writer = csv.writer(file)
                    writer.writerow(d)

            time.sleep(0.25)

        else:
            print('Halaman habis')
            exit()

    except SocketError as e:
        print("Servernya ngadat brow")
        if e.errno != errno.ECONNRESET:
            raise  # Not error we are looking for
        pass  # Handle error here.


if __name__ == '__main__':
    batas = range(200,205)
    threads = min(MAX_THREADS, len(batas))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(scrap, batas)
