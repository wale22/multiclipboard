import sys
import clipboard
import json

JSondata='mcb.json'

# creation of function to store data in json file
def save_data(text,filepath):
    #opening file with write attribute
    with open(filepath,'w') as f:
        #saving of data to file in json format
        json.dump(text, f)

# creation of function to load saved data from function
def load_data(filepath):
    try:
        #opening file with write attribute
        with open(filepath,'r') as f:
            #loading data
            data=json.load(f)
            return data
    except:
        return {}


print('welcome to python multiclipboard')
print('for more instructions and guide; make use of the "help" command')
if len(sys.argv) == 2:
    data=load_data(JSondata)
    command=sys.argv[1]

    if command == 'save':
        key=input('input the key of the data ')
        data[key]=clipboard.paste()
        save_data(data,JSondata)
        print('data has been saved')

    elif command=='load':
        key=input('input the key of data you want to load ')
        if key in data:
            loaded=data[key]
            clipboard.copy(loaded)
            print('copied data to the clipboard')
        else:
            print('invalid key')

    elif command =='list':
        print(data)

    elif command =='help':
        print('i love to render friends some help; i hope i would be able to indeed, help you')
        print('The "save" command saves data into the clipboard')
        print('The "load" command is to loads data from clipboard ')
        print('The "list" command shows list of saved data')
    
    else:
        print('invalid command')

else:
    print('one command at a time')

