class Doctor():
    def __init__(self):
        print("This is class doctor.")
    
    def body_mass_index(weight, height):
        bmi = weight / (height * height)
        print("Your BMI is : " + str(bmi))
    
    def heart_rate(heart_rate):
        if(heart_rate > 60 and heart_rate < 100):
            print("Your heart rate is normal.")
        else:
            print("Your heart rate is not normal.")
            
class Patient(Doctor):
    def __init__(self, name, weight, height, heart_rate):
        self.patient_name = name
        self.patient_weight = weight
        self.patient_height = height
        self.patient_heart_rate = heart_rate
    
    def health_check(self):
        print("Patient name : " , self.patient_name)
        Doctor.body_mass_index(self.patient_weight,self.patient_height)
        Doctor.heart_rate(self.patient_heart_rate)

patient1 = Patient("Kusum", 70, 0.91, 80)
patient1.health_check()

patient2 = Patient("Nitu", 80, 0.91, 90)
patient2.health_check()