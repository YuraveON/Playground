from socket import error as SocketError
import csv
import errno
from bs4 import BeautifulSoup
from urllib.request import urlopen

#TODO: BENERIN OUTPUT CSV

try:
    url = "http://indonesiasatu.co/category/berita"
    page = urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html, "html.parser")

    headline = soup.findAll('div', 'blog-page')
    for he in headline:
        judulHeadline = he.find('h1', 'title').text.strip()
        tanggalHeadline = he.find('span', 'date').text
        kontenHeadline = he.find('div', 'blog-content').text.strip().split("\n ")[3]

    beritas=[]
    berita = soup.findAll('div', 'blog-style')
    for be in berita:
        judulBerita = be.find('div', 'title').text.strip()
        textTanggalBerita = be.find('div', 'date').text.split()
        tanggalBerita = textTanggalBerita[2].strip(",")
        kontenBerita = be.find('p').text.strip("Read more...")
        beritas.append([judulBerita, tanggalBerita, kontenBerita])

    kepala = ['Judul', 'Tanggal', 'Konten']
    writer = csv.writer(open('results/berita_macam_apa.csv', 'w', newline=''))
    writer.writerow(kepala)
    for d in beritas:
        writer.writerow(d)


except SocketError as e:
    print("Servernya ngadat brow")
    if e.errno != errno.ECONNRESET:
        raise # Not error we are looking for
    pass # Handle error here.



