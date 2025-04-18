# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is now powered ON.")

    def power_off(self):
        print(f"{self.brand} {self.model} is shutting down.")


# Child class: Smartphone inherits from Device
class Smartphone(Device):
    def __init__(self, brand, model, os, storage, camera_mp):
        super().__init__(brand, model)  # Call parent constructor
        self.__os = os                  # Encapsulated attribute
        self.__storage = storage        # Encapsulated attribute
        self.__camera_mp = camera_mp    # Encapsulated attribute
        self.apps = []

    # Getter for encapsulated attributes
    def get_specs(self):
        return {
            "Operating System": self.__os,
            "Storage": f"{self.__storage} GB",
            "Camera": f"{self.__camera_mp} MP"
        }

    # Method to install an app
    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"{app_name} installed successfully on {self.model}.")

    # Method to take a photo
    def take_photo(self):
        print(f"Photo taken with {self.__camera_mp}MP camera.")

    # Method override (polymorphism)
    def power_on(self):
        print(f"{self.brand} {self.model} with {self.__os} is booting up...")

    def __str__(self):
        return f"{self.brand} {self.model} - {self.__os} - {self.__storage}GB"

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S21", "Android", 128, 64)
phone2 = Smartphone("Apple", "iPhone 13", "iOS", 256, 12)

# Using methods
phone1.power_on()
phone1.install_app("WhatsApp")
print(phone1.get_specs())
phone1.take_photo()
phone1.power_off()

print("\n")
phone2.power_on()
phone2.install_app("Safari")
print(phone2.get_specs())
phone2.take_photo()
phone2.power_off()
