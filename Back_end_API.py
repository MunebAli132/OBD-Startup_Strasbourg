
import obd

connection = obd.OBD(
    portstr="COM4",  # Replace with your actual port
    timeout=1,
    fast=False,
    check_voltage=False
)

print("Status:", connection.status())

if connection.is_connected():
    print("Vehicle speed:", connection.query(obd.commands.SPEED))
    connection.close()
else:
    print("Could not connect. Check the adapter and vehicle.")