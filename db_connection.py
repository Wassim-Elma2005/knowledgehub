import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="db-metrics.mysql.database.azure.com",
        user="dblogin1",
        password="Fontys1234!",
        ssl_ca="/etc/ssl/cert.pem"
    )
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS `db_metrics`")
    cur.execute("USE `db_metrics`")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            timestamp VARCHAR(30),
            hostname VARCHAR(100),
            cpu FLOAT,
            ram FLOAT,
            disk FLOAT
        );
    """)
    conn.commit()
    return conn