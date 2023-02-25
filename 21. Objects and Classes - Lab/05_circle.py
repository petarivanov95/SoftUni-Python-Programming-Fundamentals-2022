class Circle:
    __pi = 3.14

    def __init__(self,diameter) -> None:
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = self.diameter * Circle.__pi 
        return circumference
    
    def calculate_area(self):
        return ((self.diameter/2)**2) * Circle.__pi
    
    def calculate_area_of_sector(self,angle):
        area = (angle/360) * ((self.diameter/2)**2) * Circle.__pi
        return area

circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
