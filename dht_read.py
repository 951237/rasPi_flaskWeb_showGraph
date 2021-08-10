
import datetime
import time

import board
import Adafruit_DHT

import model

# 객체 생성
data = model.DHTData()

# 센서 설정
data.define_sensor('DHT1', Adafruit_DHT.DHT22, 18)


# 센서값 2초마다 읽기
try:
    while True:
        # 날짜 값 받기
        reading_time = datetime.datetime.now()
        
        # 센서의 값들 가져오기
        for sensor in data.get_sensors():
            # 센서 값 가져오고 출력하기 
            humidity, temperature = Adafruit_DHT.read_retry(sensor.dht_type, sensor.pin)
            print('Read sensor: {0} humidity: {1:0.2f}% temperature: {2:0.2f}C'.format(
                sensor.name, humidity, temperature))

            # 센서값을 데이터 베이스에 저장하기 
            data.add_reading(time=reading_time, name='{0} Humidity'.format(sensor.name), value=humidity)
            data.add_reading(time=reading_time, name='{0} Temperature'.format(sensor.name), value=temperature)
        # Wait 2 seconds and repeat.
        time.sleep(2.0)
finally:
    # 작업이 끝나면 DB닫기 
    data.close()
