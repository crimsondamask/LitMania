from qbittorrent import Client

qb = Client('http://127.0.0.1:8080/')

qb.login('admin', 'crimsondamask')

torrents = qb.torrents()

for torrent in torrents:
    print(torrent['name'])