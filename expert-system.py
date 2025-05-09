def ask_question(question: str) -> bool:
    response = input(question + " (y/n): ").lower().strip()
    return response.startswith("y")


def diagnose_allergies() -> bool:
    return ask_question("Do you experience any itching or swelling?") and ask_question(
        "Do you have red, watery eyes?"
    )


def diagnose_fever() -> bool:
    return ask_question("Do you have a temperature above 37.5°C?") and ask_question(
        "Do you experience chills?"
    )


def diagnose_cold() -> bool:
    return ask_question("Do you have a runny or stuffy nose?") and ask_question(
        "Are you sneezing frequently?"
    )


def diagnose_flu() -> bool:
    return (
        ask_question("Do you have body aches?")
        and ask_question("Do you feel tired or fatigued?")
        and ask_question("Do you have a temperature above 38°C?")
    )


def diagnose_strep_throat() -> bool:
    return ask_question("Do you have a sore throat?") and ask_question(
        "Are your tonsils swollen?"
    )


def diagnose_food_poisoning() -> bool:
    return (
        ask_question("Do you feel nauseous?")
        and ask_question("Have you been vomiting?")
        and ask_question("Do you have diarrhea?")
    )


def diagnose_appendicitis() -> bool:
    return ask_question("Do you have severe abdominal pain?") and ask_question(
        "Have you lost your appetite?"
    )


def main():
    print("Expert System for Diagnosing Ailments\nPlease answer with 'y' or 'n'.")

    diagnoses = []

    if diagnose_appendicitis():
        diagnoses.append("appendicitis")
    if diagnose_food_poisoning():
        diagnoses.append("food poisoning")
    if diagnose_flu():
        diagnoses.append("flu")
    if diagnose_strep_throat():
        diagnoses.append("strep throat")
    if diagnose_fever():
        diagnoses.append("fever")
    if diagnose_cold():
        diagnoses.append("cold")
    if diagnose_allergies():
        diagnoses.append("allergies")

    if diagnoses:
        print("\nPossible Diagnosis:", ", ".join(diagnoses))
    else:
        print("\nDiagnosis: No clear diagnosis based on the given symptoms. Please consult a doctor.")

if __name__ == "__main__":
    main()
