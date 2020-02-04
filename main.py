import json
import re


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

print("ssss")
if __name__ == "__main__":
    Json()
    # artist_names = []
    # album_name = []
    # with open('data/163music_hy_hot.json', 'r', encoding='utf8') as f:
    #     data = json.load(f)
    # # print(type(data))
    # artist_num = 1
    # for i in data:
    #     print(i + ':' + data[i])
    #     print(data[i])
    #     if "artist_names" not in data[i]:
    #         continue
    #     if len(json.loads(data[i])['artist_names']) > 1:
    #         for artist_name in json.loads(data[i])['artist_names']:
    #             if artist_name not in artist_names:
    #                 artist_names.append(artist_name)
    #     else:
    #         if json.loads(data[i])['artist_names'][0] not in artist_names:
    #             artist_names.append(json.loads(data[i])['artist_names'][0])
    #
    # print(len(artist_names))
    # # artist_names = list(set(artist_names))
    # print(artist_names)