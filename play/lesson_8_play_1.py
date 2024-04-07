class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name="Demo app"):
        if app_name not in self.app_list:
            print(f"Installing {app_name}...")
            self.app_list.append(app_name)
            return self.app_list
        else:
            print(f"{app_name} is already installed.)")
            return self.app_list
        
    def delete_app(self, app_name):
        if app_name in self.app_list:
            print(f"Deleting {app_name}.")
            self.app_list.remove(app_name)
            return self.app_list
        else:
            print(f"{app_name} is not installed.")
            return self.app_list    


device_0 = SmartDevice(123345, 'POD', 6.5)
device_0.report()
device_0.install_app("Python Dojo")
print(device_0.app_list)
device_0.install_app()
print(device_0.app_list)
