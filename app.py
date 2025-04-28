# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     data = request.get_json()
#     name = data.get('name')
#     email = data.get('email')
#     message = data.get('message')

#     # Here, you could save to database, send an email, etc.
#     print(f"Received message from {name} ({email}): {message}")

#     return jsonify({"status": "success", "message": "Form submitted successfully!"})

# if __name__ == '__main__':
#     app.run(debug=True)


# boolean = True
# if boolean:
#     print("This is a test.")



# def extendList(val, list=[]):
#     list.append(val)

#     return list

# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')

# print(list1)

# print(list2)
# print(list3)

