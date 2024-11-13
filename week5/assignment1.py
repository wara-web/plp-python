# Base class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Derived class: Smartphone (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels, battery_capacity):
        super().__init__(brand, model)
        self.__storage = storage  # Encapsulated attribute
        self.camera_megapixels = camera_megapixels
        self.battery_capacity = battery_capacity

    # Getter method for encapsulated attribute
    def get_storage(self):
        return self.__storage

    # Setter method for encapsulated attribute
    def set_storage(self, storage):
        if storage > 0:
            self.__storage = storage
        else:
            print("Invalid storage size")

    def take_photo(self):
        return f"{self.device_info()} is taking a photo with its {self.camera_megapixels}MP camera 📸"

    def charge(self):
        return f"Charging {self.device_info()} with {self.battery_capacity}mAh battery 🔋"

    def __str__(self):
        return f"{self.device_info()} - Storage: {self.__storage}GB, Camera: {self.camera_megapixels}MP"


# Testing the Smartphone class
iphone = Smartphone("Apple", "iPhone 14", 256, 12, 3279)
samsung = Smartphone("Samsung", "Galaxy S22", 512, 50, 4500)

# Print device info
print(iphone)
print(samsung)

# Use methods
print(iphone.take_photo())
print(samsung.charge())

# Test encapsulation
print("Storage before update:", samsung.get_storage())
samsung.set_storage(1024)  # Updating the storage
print("Storage after update:", samsung.get_storage())
