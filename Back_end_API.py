import obd

# Connect to an OBD-II adapter
connection = obd.OBD()

print("Connection status:", connection.status())

if connection.is_connected():
    cmd = obd.commands.SPEED
    response = connection.query(cmd)

    if response.value is not None:
        print("Vehicle speed:", response.value)
        print("Speed in mph:", response.value.to("mph"))
    else:
        print("No speed data received.")

    connection.close()
else:
    print("No vehicle connection. Check your OBD-II adapter.")