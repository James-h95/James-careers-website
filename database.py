# Code to connect & extract data from DB. Using SQL alchemy.
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://trucqkh86khixzq43yfm:pscale_pw_eAQqtnBiHxoJfHun5VLtcFPoWbNrwddYoQAB9WovpmJ@aws.connect.psdb.cloud/jamescareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string, 
  connect_args={
  "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())
  