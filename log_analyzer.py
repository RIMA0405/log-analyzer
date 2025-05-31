import random

def analyze_log(file_path="log.txt", output_path="rapport.txt"):
    info = warning = error = 0
    with open(file_path, "r") as f:
        for line in f:
            if "INFO" in line:
                info += 1
            elif "WARNING" in line:
                warning += 1
            elif "ERROR" in line:
                error += 1

    random_numbers = [random.randint(1000, 9999) for _ in range(5)]

    with open(output_path, "w") as f:
        f.write(f"STATISTIQUES LOGS:\n")
        f.write(f"INFO: {info}\nWARNING: {warning}\nERROR: {error}\n\n")
        f.write("NUMÉROS GÉNÉRÉS:\n")
        f.write(", ".join(map(str, random_numbers)) + "\n")
        print("Analyse terminée ✅")
if __name__ == "__main__":
    analyze_log()
