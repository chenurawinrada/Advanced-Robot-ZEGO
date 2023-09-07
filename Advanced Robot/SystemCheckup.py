import psutil

class SystemStatus:
    def RamStatus(self):
        RAM = psutil.virtual_memory()
        gb = RAM[3]/1000000000
        total = RAM.total/1024/1024/1024
        inp = (gb/total) * 100

        if inp <= 90:
            return True
        else:
            return False

    def BatteryStatus(self):
        status = psutil.sensors_battery()
        if status.percent >= 30:
            return True
        else:
            return False

# print(SystemStatus().RamStatus())