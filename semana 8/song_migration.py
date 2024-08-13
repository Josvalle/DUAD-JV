def open_song():
    with open('semana 8/song.txt') as file:
        for line in file:
            song = file.readlines()
        
        song.sort()
        return song


def write_new_list(new_file):
    song = open_song()
    with open(new_file, 'w') as file:
        file.writelines(song)


write_new_list('semana 8/new_file.txt')


