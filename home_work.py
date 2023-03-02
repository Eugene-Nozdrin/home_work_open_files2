# name_txt_1 = '1.txt'
# txt_1 = open(name_txt_1, encoding='utf-8')
# list_txt_1 = txt_1.readlines()
# print(list_txt_1)
#
# name_txt_2 = '2.txt'
# txt_2 = open(name_txt_2, encoding='utf-8')
# list_txt_2 = txt_2.readlines()
# print(list_txt_2)
#
# name_txt_3 = '3.txt'
# txt_3 = open(name_txt_3, encoding='utf-8')
# list_txt_3 = txt_3.readlines()
# print(list_txt_3)
#
# all_list = sorted([list_txt_1, list_txt_2, list_txt_3], key=lambda x: len(x))
# print(all_list)
# for id, text in enumerate(all_list, start=1):
#     print(id)
#     print(text)
#
file_list = ['1.txt', '2.txt', '3.txt']
all_file = []
for file in file_list:
    txt = open(file, encoding='utf-8')
    txt_list = txt.readlines()
    txt_list.insert(0, str(len(txt_list)) + "\n")
    txt_list.insert(0, file+"\n")
    all_file.append(txt_list)
    txt.close()
print(sorted(all_file, key=lambda x: len(x)))
with open('ответ.txt', 'w') as f:
    for text in sorted(all_file, key=lambda x: len(x)):
        f.writelines(text)

