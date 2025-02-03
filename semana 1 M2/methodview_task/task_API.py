from flask import Flask, request, jsonify
from flask.views import MethodView
from file_handling import open_jason, export_json

app = Flask(__name__)

task_list = open_jason()

class Task_API(MethodView):
    def get(self):
        filter_task_list = task_list
        task_filter = request.args.get("status")
        if task_filter:
            filter_task_list = list(filter(lambda task: task['Status'] == task_filter, filter_task_list))
            return {"Filter Task": filter_task_list}
        else:
            return task_list
        

    def post(self):
        id_list = [task['id'] for task in task_list]
        valid_status = ['To do', 'In progress', 'Complete']
        try:
            if "id" not in request.json:
                raise ValueError('id cannot be empty')
            if request.json['id'] in id_list:
                raise ValueError('id already exist')
            if "Title" not in request.json:
                raise ValueError('Title can not be empty')
            if "Description" not in request.json:
                raise ValueError('Description can not be empty')
            if "Status" not in request.json:
                raise ValueError('Status can not be empty')
            if request.json['Status'] not in valid_status:
                raise ValueError('Status enter is not valid ("To do", "In progress", "Complete")')
            
            task_list.append({
                'id': int(request.json['id']),
                'Title': request.json['Title'],
                'Description': request.json['Description'],
                'Status': request.json['Status']
            })
            export_json(task_list, "jobs_mv.json")
            return task_list
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
                
            return jsonify(message=str(ex)), 500
        
    def put(self, id):
        self.id = id
        try:
            update_id = id
        except ValueError as ex:
                    return jsonify(message=str(ex)), 400
        for item in task_list:
            if update_id == item['id']:
                try:
                    if 'id' in request.json:
                        raise ValueError('id cannot be update, only Title, Description or Status')
                    if 'Title' in request.json:
                        item['Title'] = request.json['Title']
                    if 'Description'  in request.json:
                        item['Description'] = request.json['Description']
                    if 'Status' in request.json:
                        item['Status'] = request.json['Status'] 
                    
                    export_json(task_list, "jobs_mv.json")
                    return(f'update task list:{task_list}' )
                except ValueError as ex:
                    return jsonify(message=str(ex)), 400
                except Exception as ex:
                        return jsonify(message=str(ex)), 500
           
    def delete(self):

        if 'id' in request.json:
            remove_id = request.json['id']
            for d in task_list:
                if remove_id == d['id']:
                    task_list.remove(d)
                    export_json(task_list, "jobs_mv.json")
                    return task_list
        elif 'Title' in request.json or 'Description' in request.json or 'Status' in request.json:
             return jsonify({'ERROR':'Only "id" is allow on body to delete a Task'}), 403
        else:
            return jsonify({"ERROR": "The id enter was not found, please check"}), 404

            
def main():
    
    task_view = Task_API.as_view('task_api')
    app.add_url_rule('/info', view_func=task_view, methods=['GET'])
    app.add_url_rule('/new-task', view_func=task_view, methods=['POST'])
    app.add_url_rule('/update/<int:id>', view_func=task_view, methods=['PUT','PATCH'])
    app.add_url_rule('/remove', view_func=task_view, methods=['DELETE'])   


if __name__ == "__main__":
    main()
    app.run(host='localhost', debug=True)