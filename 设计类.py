class Car:
    def move(self):
        print("车在移动")
    def stop(self):
        print("停车")
class CarStore:
    def order(self):
        self.car= Car()
        self.car.move()
        self.car.stop()
class SuonataCar:
    def mov(self):
        print("车在移动")
    def stop(self):
        print("车停下了")

