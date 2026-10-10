
import obd

# Use a specific adapter port, e.g. COM3.
# Change COM3 to your adapter's actual port.
connection = obd.OBD(portstr="COM3", fast=False, timeout=2)

print("Connection status:", connection.status())

if connection.is_connected():
    response = connection.query(obd.commands.SPEED, force=True)

    if not response.is_null():
        print("Vehicle speed:", response.value)
        print("Speed in mph:", response.value.to("mph"))
    else:
        print("No speed data received.")

    connection.close()
else:
    print("Connection failed. Check the adapter, ignition, and COM port.")