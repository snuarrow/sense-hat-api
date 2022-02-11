import sys
from flask import Flask
from sense_hat import SenseHat

app = Flask(__name__)
sense = SenseHat()
sense.set_imu_config(True, True, True) # compass, gyro, accel

def read_sense_hat():
    orientation = sense.get_orientation_degrees()
    return {
        "sensorId": "senseHat",
        "temperature": sense.get_temperature(),
        "humidity": sense.get_humidity(),
        "temperatureFromHumidity": sense.get_temperature_from_humidity(),
        "temperatureFromPressure": sense.get_temperature_from_pressure(),
        "pressure": sense.get_pressure(),
        "orientation": orientation,
        
    }


@app.route("/")
def root():
    return read_sense_hat()


def main():
    app.run(host="0.0.0.0", port=80)
    print('yolo')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)