class Surveyor:
    def __init__(self):
        self.encrypted_values = []
        self.noises = []

    def collect(self, encrypted_salary, noise):
        self.encrypted_values.append(encrypted_salary)
        self.noises.append(noise)

    def compute_average(self):
        total_encrypted = sum(self.encrypted_values)
        total_noise = sum(self.noises)
        total_real = total_encrypted - total_noise
        return total_real / len(self.encrypted_values) if self.encrypted_values else 0
