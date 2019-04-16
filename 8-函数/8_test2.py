__Author__ = "noduez"

#8-6 城市名
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return (city.title() + ", " + country.title())


city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)


#8-7 专辑
def make_album(artist,title,tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title()
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger', tracks=9)
print(album)

#8-8用户的专辑
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'q' at any time to stop.")
while True:
    title = input(title_prompt)
    if title == 'q':
        break

    artist = input(artist_prompt)
    if artist == 'q':
        break

    album = make_album(artist,title)

    print(album)

    print("\nThanks for responding!")
