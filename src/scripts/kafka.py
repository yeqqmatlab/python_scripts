

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.0.121:9092')  # 连接kafka

msg = "Hello World".encode('utf-8')  # 发送内容,必须是bytes类型
producer.send('test', msg)  # 发送的topic为test
producer.close()