import random
from colorama import init, Fore, Style

def analyze_log(file_path="log.txt", output_path="rapport.txt"):
    init(autoreset=True)  # Initialisation colorama
    
    info = warning = error = 0
    
    try:
        with open(file_path, "r") as f:
            for line in f:
                if "INFO" in line:
                    info += 1
                elif "WARNING" in line:
                    warning += 1
                elif "ERROR" in line:
                    error += 1
    except FileNotFoundError:
        print(Fore.RED + f"Erreur : fichier {file_path} non trouvé.")
        return
    
    random_numbers = [random.randint(1000, 9999) for _ in range(5)]
    
    with open(output_path, "w") as f:
        f.write("STATISTIQUES LOGS:\n")
        f.write(f"INFO: {info}\nWARNING: {warning}\nERROR: {error}\n\n")
        f.write("NUMÉROS GÉNÉRÉS:\n")
        f.write(", ".join(map(str, random_numbers)) + "\n")
    
    print(Fore.GREEN + "Analyse terminée ✅")
    print(Fore.CYAN + f"Statistiques : INFO={info}, WARNING={warning}, ERROR={error}")
    print(Fore.YELLOW + f"Numéros générés : {', '.join(map(str, random_numbers))}")

if __name__ == "__main__":
    analyze_log()
