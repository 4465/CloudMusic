import json
import re
import csv

def Json():
    print("sdd")
    f = open('data/163music_hy_hot.txt', 'r', encoding='utf-8')
    f1 = open('data/str.txt', 'w', encoding='utf-8')
    str = f.read()
    str1 = str.split()
    str2 = ''.join(str1)
    # str_regex = r'{.*?}'
    pattern = re.compile(r'{.*?}')
    result = pattern.findall(str2)  # 去除空格
    index = 1
    dic = {}
    for i in result:
        j = json.loads(i)
        # print(index,j)
        print(type(j))
        lst = []
        lst.append(j)
        dic[index] = lst
        index = index + 1
    print(dic)
    with open('data/163music_hy_hot.json', 'w', encoding='utf8') as f:
        json.dump(dic, f, ensure_ascii=False)

def get_music_entity(data):
    csvfile = open(r"data/music_nodes.csv", 'w', encoding='utf8', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'lyric'])
    for i in data:
        music_info = []
        music_dic = data[i][0]       #data[i] is list
        music_id = music_dic["_id"]
        music_name = music_dic["name"]
        music_lyric = music_dic["lyric"]
        music_info.append(music_id)
        music_info.append(music_name)
        music_info.append(music_lyric)
        print(music_info)
        writer.writerow(music_info)

def get_artist_entity(data):
    csvfile = open(r'data/artist_nodes.csv', 'w', encoding='utf8', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['id','name'])
    artist_info = {}
    for i in data:
        music_dic = data[i][0]
        for j in music_dic['artist_ids']:
            index = music_dic['artist_ids'].index(j)
            artist_info[j] = music_dic['artist_names'][index]
    for i in artist_info:
        lst = []
        lst.append(i)
        lst.append(artist_info[i])
        writer.writerow(lst)

def get_album_entity(data):
    csvfile = open(r"data/album_nodes.csv", 'w', encoding='utf8', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['album_id', 'album_name'])
    album_info = {}
    for i in data:
        music_dic = data[i][0]
        album_info[music_dic['album_id']] = music_dic['album_name']
    for i in album_info:
        lst = []
        lst.append(i)
        lst.append(album_info[i])
        writer.writerow(lst)

def get_playlist_entity(data):
    csvfile = open(r'data/playlist_nodes.csv', 'w', encoding='utf8', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['playlist_id', 'playlist_name'])
    playlist_info = {}
    for i in data:
        music_dic = data[i][0]
        if "playlist_ids" in music_dic:
            for j in music_dic['playlist_ids']:
                index = music_dic['playlist_ids'].index(j)
                playlist_info[j] = music_dic['playlist_names'][index]
        else:
            print(music_dic['_id'])
    for i in playlist_info:
        lst = []
        lst.append(i)
        lst.append(playlist_info[i])
        writer.writerow(lst)

def get_rel_sungby(data):
    csvfile = open(r'data/sung_rel.csv', 'w', encoding='utf8', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['end_id', 'music', 'start_id', 'artist', 'relation'])
    for i in data:
        music_dic = data[i][0]
        artists = music_dic['artist_names']
        for j in artists:
            lst = []
            lst.append(music_dic['_id'])
            lst.append(music_dic['name'])
            index = artists.index(j)
            lst.append(music_dic['artist_ids'][index])
            lst.append(j)
            lst.append('演唱')
            writer.writerow(lst)


def get_rel_albumMusic(data):
    csvfile = open(r'data/albumMusic.csv', 'w', encoding='utf8', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['start_id', 'album', 'end_id', 'music', 'relation'])
    for i in data:
        music_dic = data[i][0]
        lst = []
        lst.append(music_dic['album_id'])
        lst.append(music_dic['album_name'])
        lst.append(music_dic['_id'])
        lst.append(music_dic['name'])
        lst.append('收录')
        writer.writerow(lst)

def get_rel_playlistMusic(data):
    csvfile = open(r'data/playlistMusic.csv', 'w', encoding='utf8', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['start_id', 'playlist', 'end_id', 'music', 'relation'])
    for i in data:
        music_dic = data[i][0]
        if 'playlist_ids' in music_dic:
            playlists = music_dic['playlist_ids']
            for j in playlists:
                lst = []
                lst.append(j)
                index = playlists.index(j)
                lst.append(music_dic['playlist_names'][index])
                lst.append(music_dic['_id'])
                lst.append(music_dic['name'])
                lst.append('收藏')
                writer.writerow(lst)

def get_rel_similarMusic(data):
    csvfile = open(r'data/similarMusic.csv', 'w', encoding='utf8', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['start_id', 'music', 'end_id', 'music', 'relation'])
    for i in data:
        music_dic = data[i][0]
        if 'similar_musics_ids' in music_dic:
            musics = music_dic['similar_musics_ids']
            for j in musics:
                lst = []
                lst.append(j)
                index = musics.index(j)
                lst.append(music_dic['similar_musics_names'][index])
                lst.append(music_dic['_id'])
                lst.append(music_dic['name'])
                lst.append('相似')
                writer.writerow(lst)



print("ssss")
if __name__ == "__main__":
    with open('data/163music_hy_hot.json', 'r', encoding='utf8') as f:
        data = json.load(f)            #data is dic
    get_rel_similarMusic(data)