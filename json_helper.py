import json
import os
import pickle

def read_json(file_path:str) -> json:
    #file_content = str(open(file_path, 'r'))

    #print(type(file_content))
    #print(type(file_content))

    file_content = open(file_path,)
    file_content_dict = json.load(file_content)

    #print(type(file_content_dict))
    #print(type(json.dumps(file_content_dict)))
    return json.dumps(file_content_dict)

#read_json('/Users/ballakeerthi/dev/PyPart9/data/super_smash_bros/link.json')

def read_all_json_files(dir_path:str) -> list:
    file_content = list()
    os.chdir(dir_path)
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            file_content.append(json.loads(read_json(name)))

    return file_content

#read_all_json_files('/Users/ballakeerthi/dev/PyPart9/data/super_smash_bros')
    #file_content = open(os.getcwd(file_path))

def write_pickle(file_path:str,data):
    file_content = open(file_path,)
    output_file= os.open('super_smash_characters.pickle','w')
    output_list = json.loads(read_json(file_path))

    pickle.dump(file_content,output_file)
    super_smash_characters.pickle.close()

write_pickle('/Users/ballakeerthi/dev/PyPart9/data/super_smash_bros/mario.json','data')