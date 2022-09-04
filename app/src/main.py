import os
import sys
sys.path.append(os.pardir)

from enum import Enum
from line.notify import send
from nature_remo.sensor import fetch
from nature_remo.power import on, off

nature_appearance = os.getenv('NATURE_APPEARANCE')

class Commands(Enum):
    notify_sensor_data = 'notify_sensor_data'
    turn_on_aircon = 'turn_on_aircon'
    turn_off_aircon = 'turn_off_aircon'

def notify_sensor_data() -> None:
    data = fetch()
    message = f"センサーのデータ\n🌡気温: {str(data.temperature)}℃\n💧湿度: {str(data.humidity)}%\n💡照度: {str(data.illumination)}point"
    send(message)

def turn_on_aircon() -> None:
    if nature_appearance is None:
        return
    on(nature_appearance=nature_appearance)
    send(f"エアコンをONにしました。")

def turn_off_aircon() -> None:
    if nature_appearance is None:
        return
    off(nature_appearance=nature_appearance)
    send(f"エアコンをOFFにしました。")

def route(command: str) -> None:
    if command == Commands.notify_sensor_data.value:
        notify_sensor_data()
    elif command == Commands.turn_on_aircon.value:
        turn_on_aircon()
    elif command == Commands.turn_off_aircon.value:
        turn_off_aircon()
    else:
        print(command)
        raise Exception(f'コマンドは以下のいずれかである必要があります。\n{Commands.__members__.items()}')

def main() -> None:
    command = sys.argv[1]
    route(command)

if __name__ == "__main__":
    main()
