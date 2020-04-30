import json

def update_file(file_name, transform):
    with open(file_name, 'r') as reader:
        data = {}
        try:
            data = json.load(reader)
        except json.decoder.JSONDecodeError as e:
            print ("Error", e)
            pass
        
        try:
            new_data = transform(data)
        except Exception as e:
            print (e)
            return False
        else:
            with open(file_name, 'w') as writer:
                writer.write(json.dumps(new_data))
        
    return True
