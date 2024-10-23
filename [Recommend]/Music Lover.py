"""Music Lover"""
def main():
    """main"""
    n = int(input())
    artist_dict = {}
    for _ in range(n):
        artist, song = input().split('-')
        if artist not in artist_dict:
            artist_dict[artist] = []
        artist_dict[artist].append(song.strip())
    for artist, songs in artist_dict.items():
        print(artist)
        for song in songs:
            print(song)
main()
