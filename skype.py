playlist = QMediaPlaylist()
url = QUrl.fromLocalFile("/home/user/Downloads/ss.mp3")
playlist.addMedia(QMediaContent(url))


player.setPlaylist(playlist)
player.playlist().setCurrentIndex(0)
player.play()