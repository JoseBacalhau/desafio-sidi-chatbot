from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect("dbname=chatbot user=postgres password=369963 host=localhost")

@app.route('/check_job_id/<int:id>', methods=['GET'])
def get_check_job_id(id):
    cur = conn.cursor()
    cur.execute("SELECT job FROM check_job_id WHERE id = %s", (id,))
    result = cur.fetchone()
    cur.close()
    return jsonify({'job': result[0]}) if result else jsonify({'job': None})

@app.route('/get_job_messages/<int:id>', methods=['GET'])
def get_job_messages(id):
    cur = conn.cursor()
    cur.execute("SELECT jobmessages FROM get_job_messages WHERE id = %s", (id,))
    result = cur.fetchone()
    cur.close()
    return jsonify({'jobmessages': result[0]}) if result else jsonify({'jobmessages': None})

if __name__ == '__main__':
    app.run()
