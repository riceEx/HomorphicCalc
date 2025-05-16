from participant import Participant
from surveyor import Surveyor

def main():
    # Simulate 5 participants
    salaries = [50000, 60000, 55000, 65000, 70000]
    participants = [Participant(s) for s in salaries]
    surveyor = Surveyor()

    for p in participants:
        encrypted_salary, noise = p.encrypt()
        surveyor.collect(encrypted_salary, noise)

    avg_salary = surveyor.compute_average()
    print(f"Computed average salary (without seeing individual values): ${avg_salary:.2f}")

if __name__ == "__main__":
    main()
