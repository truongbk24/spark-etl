FROM apache/airflow:latest-python3.9
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

RUN USER_NAME=$(whoami) && echo "Current user is: $USER_NAME"

COPY setup_conn.py $AIRFLOW_HOME

USER root
RUN mkdir -p /opt/jars && \
    USER_NAME=$(whoami) && \
    echo "Current user is: $USER_NAME" && \
    chown $USER_NAME /opt/jars

RUN apt-get update && \
    apt-get install -y --no-install-recommends \    
    default-jdk   
RUN apt-get install -y unzip --no-install-recommends
RUN apt-get install -y telnet --no-install-recommends

ENV JAVA_HOME='/usr/lib/jvm/java-17-openjdk-arm64'
ENV PATH=$PATH:$JAVA_HOME/bin    
ENV CLICKHOUSE_HOST=clickhouse
ENV CLICKHOUSE_USER=admin
ENV CLICKHOUSE_PASSWORD=admin
ENV MINIO_USER=minioadmin
ENV MINIO_PASSWORD=minioadmin
ENV SEND_EMAIL_TO=your_email@gmail.com
# Set environment variables to configure airflow.cfg
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
ENV AIRFLOW__SMTP__SMTP_HOST=smtp.gmail.com
ENV AIRFLOW__SMTP__SMTP_USER=your_email@gmail.com
ENV AIRFLOW__SMTP__SMTP_PASSWORD=your_password
ENV AIRFLOW__SMTP__SMTP_PORT=587 


USER $USER_NAME

