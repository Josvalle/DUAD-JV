import json

def open_jason():
    with open('jobs.json') as file:
        convert_python = json.load(file)
        
        return convert_python
    
def export_json(convert_python, export_json):
    convert_json = json.dumps(convert_python)
    with open(export_json, 'w') as file:
        file.write(convert_json)