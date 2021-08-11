
import datetime
import time

import board
import adafruit_dht

import model

# 객체 생성
data = model.DHTData()

# 센서 설정
# data.define_sensor('DHT1', Adafruit_DHT.DHT22, 18)
dhtDevice = adafruit_dht.DHT22(board.D4)

# 센서값 2초마다 읽기
while True:
    try:
        # 날짜 값 받기
        reading_time = datetime.datetime.now()
        
        humidity = dhtDevice.humidity
        temperature = dhtDevice.temperature
        print('Read sensor: DHT22 humidity: {0:0.2f}% temperature: {1:0.2f}C'.format(humidity, temperature))

        # 센서값을 데이터 베이스에 저장하기 
        data.add_reading(time=reading_time, name='DHT22 Humidity', value=humidity)
        data.add_reading(time=reading_time, name='DHT22 Temperature', value=temperature)
        # Wait 2 seconds and repeat.
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(60.0)
    # finally:
    # # 작업이 끝나면 DB닫기 
    #     data.close()
