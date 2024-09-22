def make_album(artist, album, no_songs=None):
	"""creates dictionaries including artist's name and album name"""
	music_album = {'artist': artist, 'album': album}
	if no_songs:
		music_album['number of tracks'] = no_songs
	return music_album

print("Welcome to my album program.  You can keep adding artists and album details for as long as you like.")
print("Press 'q' at any time to quit.")

while True:
	artist_name = input("Artist's name (required): ")
	if artist_name == 'q':
		break
	album_name = input("Album title (required): ")
	if album_name == 'q':
		break
	songs = input("Number of tracks (optional, press enter if not known): ")
	if songs == 'q':
		break

	album = make_album(artist_name, album_name, songs)
	for item, value in album.items():
		print(f"{item}: {value}")

#print("\n")

# album = make_album('olivia rodrigo', 'guts')
# for item, value in album.items():
# 	print(f"{item.title()}: {value}")

# print("\n")

# album = make_album('underworld', 'beaucoup fish', 11)
# for item, value in album.items():
# 	print(f"{item.title()}: {value}")
	
# print("\n")

# for item, value in make_album('kylie', 'wow').items():
# 	print(f"{item.title()}: {value}")