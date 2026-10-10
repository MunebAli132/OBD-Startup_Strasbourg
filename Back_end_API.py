
import random
import time
from datetime import datetime

def read_vehicle_data():
    """Simulate readings from an OBD-II vehicle."""

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "engine_temperature": random.randint(85, 120),
        "battery_voltage": round(random.uniform(11.5, 14.5), 2),
        "engine_rpm": random.randint(700, 3500),
        "vehicle_speed": random.randint(0, 120),
    }

def check_alerts(data):
    """Illustrative alert rules for the MVP."""

    alerts = []

    if data["engine_temperature"] > 110:
        alerts.append("High engine temperature")

    if data["battery_voltage"] < 12.0:
        alerts.append("Low battery voltage")

    return alerts

if __name__ == "__main__":
    while True:
        data = read_vehicle_data()
        alerts = check_alerts(data)

        print("\n--- OBD SmartCare ---")
        for metric, value in data.items():
            print(f"{metric}: {value}")

        print("Alert:", "Yes" if alerts else "No")

        for alert in alerts:
            print("Warning:", alert)

        time.sleep(3)