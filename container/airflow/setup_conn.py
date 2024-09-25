import subprocess
import os
from airflow.models import Variable

def add_airflow_connection():
    connection_id = "spark-default"
    connection_type = "spark"
    host = "spark://spark-master"
    port = "7077"
    cmd = [
        "airflow",
        "connections",
        "add",
        connection_id,
        "--conn-host",
        host,
        "--conn-type",
        connection_type,
        "--conn-port",
        port,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully added {connection_id} connection")
    else:
        print(f"Failed to add {connection_id} connection: {result.stderr}")

def add_send_emmail_variable():
    send_email_to = os.getenv("SEND_EMAIL_TO")
    Variable.set("email_to",send_email_to)

add_airflow_connection()
add_send_emmail_variable()