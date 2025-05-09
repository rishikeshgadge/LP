import streamlit as st

# Function for asking yes/no questions
def ask_question(question: str, question_id: str) -> bool:
    return st.radio(question, ['Yes', 'No'], key=f"{question_id}") == 'Yes'

# Class for ExpertSystem with knowledge base and disease descriptions
class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "fever": ["flu", "COVID-19"],
            "cough": ["cold", "flu", "COVID-19"],
            "shortness of breath": ["COVID-19", "asthma"],
            "headache": ["migraine", "flu"],
            "fatigue": ["flu", "COVID-19", "anemia"],
            "sore throat": ["cold", "flu"],
            "runny nose": ["cold", "flu"],
            "body aches": ["flu", "COVID-19"],
            "chills": ["flu", "COVID-19"],
            "swollen tonsils": ["strep throat", "tonsillitis"]
        }
        
        self.disease_descriptions = {
            "flu": "Influenza (flu) is a viral infection that attacks your respiratory system.",
            "COVID-19": "COVID-19 is an infectious disease caused by the SARS-CoV-2 virus.",
            "cold": "The common cold is a viral infection of your nose and throat.",
            "asthma": "Asthma is a condition in which your airways narrow and swell.",
            "migraine": "A migraine is a severe headache causing throbbing pain.",
            "anemia": "Anemia is a condition where you lack enough healthy red blood cells.",
            "strep throat": "Strep throat is a bacterial infection causing inflammation and pain in the throat.",
            "tonsillitis": "Tonsillitis is inflammation of the tonsils, typically caused by viral or bacterial infection."
        }

    def diagnose(self, symptoms):
        possible_diseases = {}
        
        for symptom in symptoms:
            if symptom in self.knowledge_base:
                for disease in self.knowledge_base[symptom]:
                    possible_diseases[disease] = possible_diseases.get(disease, 0) + 1
        
        if not possible_diseases:
            return "No matching diseases found. Please consult a doctor."
        
        # Sort diseases by likelihood (number of matching symptoms)
        sorted_diseases = sorted(possible_diseases.items(), key=lambda x: x[1], reverse=True)
        most_likely_disease = sorted_diseases[0][0]
        
        # Generate a more comprehensive response with alternative possibilities
        response = f"You may have {most_likely_disease}. {self.disease_descriptions[most_likely_disease]}"
        
        # Add alternative possibilities if they exist
        if len(sorted_diseases) > 1:
            alternatives = [f"{disease} ({count} matching symptoms)" 
                           for disease, count in sorted_diseases[1:3]]  # List next 2 most likely
            response += f"\n\nOther possibilities include: {', '.join(alternatives)}."
            
        response += "\n\nDISCLAIMER: This is not a medical diagnosis. Please consult a healthcare professional."
        return response

# Medical Expert System for specific diseases
class MedicalExpertSystem:
    def __init__(self):
        self.symptoms = {
            "fever": False,
            "cough": False,
            "shortness of breath": False,
            "fatigue": False,
            "body aches": False,
            "loss of taste or smell": False,
            "headache": False,
            "sore throat": False,
            "chest pain": False,
            "nausea": False,
            "vomiting": False,
            "abdominal pain": False,
        }
        self.hospitals = {
            "COVID-19": {"Hospital A": "123-456-7890", "Hospital B": "234-567-8901"},
            "Flu": {"Hospital C": "345-678-9012", "Hospital D": "456-789-0123"},
            "Food Poisoning": {"Hospital E": "567-890-1234", "Hospital F": "678-901-2345"},
        }

    def diagnose(self):
        # Calculate probability scores for each condition
        covid_score = sum([
            self.symptoms["fever"] * 2,
            self.symptoms["cough"] * 2,
            self.symptoms["shortness of breath"] * 3,
            self.symptoms["loss of taste or smell"] * 4,
            self.symptoms["fatigue"],
            self.symptoms["body aches"],
            self.symptoms["headache"],
            self.symptoms["sore throat"]
        ])
        
        flu_score = sum([
            self.symptoms["fever"] * 3,
            self.symptoms["cough"] * 2,
            self.symptoms["fatigue"] * 2,
            self.symptoms["body aches"] * 3,
            self.symptoms["headache"] * 2,
            self.symptoms["sore throat"]
        ])
        
        food_poisoning_score = sum([
            self.symptoms["nausea"] * 3,
            self.symptoms["vomiting"] * 3,
            self.symptoms["abdominal pain"] * 3,
            self.symptoms["fever"]
        ])
        
        # Determine the most likely condition
        max_score = max(covid_score, flu_score, food_poisoning_score)
        
        if max_score < 3:
            return "Your symptoms don't strongly match a specific condition. Please consult with a healthcare professional."
        
        if covid_score == max_score and covid_score >= 5:
            return "You may have COVID-19. Please get tested immediately. Here are some hospitals you can contact: " + str(self.hospitals["COVID-19"])
        elif flu_score == max_score and flu_score >= 5:
            return "You may have the flu. Please rest and drink plenty of fluids. Here are some hospitals you can contact: " + str(self.hospitals["Flu"])
        elif food_poisoning_score == max_score and food_poisoning_score >= 5:
            return "You may have food poisoning. Please seek medical attention. Here are some hospitals you can contact: " + str(self.hospitals["Food Poisoning"])
        else:
            return "Your symptoms suggest a mild condition. Monitor your symptoms and consult a healthcare professional if they worsen."

    def update_symptoms(self, symptom, value):
        if symptom in self.symptoms:
            self.symptoms[symptom] = value

# Streamlit UI for Expert System
def expert_system_ui():
    st.title("Health Diagnosis Expert System")
    st.write("Answer the questions to help diagnose your symptoms.")
    
    # Initialize session state for question counter and symptoms
    if "question_counter" not in st.session_state:
        st.session_state.question_counter = 0
        st.session_state.symptoms = []
        st.session_state.med_expert_system = MedicalExpertSystem()
    
    # Create tabs for different types of diagnoses
    tab1, tab2 = st.tabs(["General Diagnosis", "Specific Diagnosis"])
    
    with tab1:
        st.header("General Symptoms Assessment")
        
        # Reset symptoms list if starting fresh
        if st.button("Start New Diagnosis"):
            st.session_state.symptoms = []
            st.session_state.question_counter = 0
            st.session_state.med_expert_system = MedicalExpertSystem()
            st.experimental_rerun()
        
        # Use a form to collect all symptoms at once
        with st.form(key="symptom_form"):
            symptoms = []
            
            # Body symptoms
            st.subheader("Body Symptoms")
            if ask_question("Do you have body aches?", "body_aches"):
                symptoms.append("body aches")
                
            if ask_question("Do you feel tired or fatigued?", "fatigue"):
                symptoms.append("fatigue")
            
            # Respiratory symptoms
            st.subheader("Respiratory Symptoms")
            if ask_question("Do you have a cough?", "cough"):
                symptoms.append("cough")
                
            if ask_question("Do you have a sore throat?", "sore_throat"):
                symptoms.append("sore throat")
                
            if ask_question("Are your tonsils swollen?", "swollen_tonsils"):
                symptoms.append("swollen tonsils")
                
            if ask_question("Do you have a runny or stuffy nose?", "runny_nose"):
                symptoms.append("runny nose")
                
            if ask_question("Do you have shortness of breath?", "shortness_breath"):
                symptoms.append("shortness of breath")
            
            # Temperature symptoms
            st.subheader("Temperature Symptoms")
            if ask_question("Do you have a temperature above 37.5°C?", "temperature"):
                symptoms.append("fever")
                
            if ask_question("Do you experience chills?", "chills"):
                symptoms.append("chills")
            
            # Head symptoms
            st.subheader("Head Symptoms")
            if ask_question("Do you have a headache?", "headache"):
                symptoms.append("headache")
            
            submit_button = st.form_submit_button(label="Get Diagnosis")
            
            if submit_button:
                st.session_state.symptoms = symptoms
        
        # Display diagnosis after form submission
        if st.session_state.symptoms:
            expert_system = ExpertSystem()
            result = expert_system.diagnose(st.session_state.symptoms)
            st.subheader("Diagnosis Results:")
            st.write(result)
            
            # Display selected symptoms
            if st.session_state.symptoms:
                st.subheader("Your reported symptoms:")
                for symptom in st.session_state.symptoms:
                    st.write(f"- {symptom}")
    
    with tab2:
        st.header("Specific Disease Assessment")
        
        # Create a more targeted assessment for specific conditions
        with st.form(key="specific_form"):
            st.subheader("COVID-19 & Flu Symptoms")
            if ask_question("Do you have a fever?", "sp_fever"):
                st.session_state.med_expert_system.update_symptoms("fever", True)
                
            if ask_question("Do you have a cough?", "sp_cough"):
                st.session_state.med_expert_system.update_symptoms("cough", True)
                
            if ask_question("Do you have shortness of breath?", "sp_breath"):
                st.session_state.med_expert_system.update_symptoms("shortness of breath", True)
                
            if ask_question("Do you have fatigue?", "sp_fatigue"):
                st.session_state.med_expert_system.update_symptoms("fatigue", True)
                
            if ask_question("Do you have body aches?", "sp_aches"):
                st.session_state.med_expert_system.update_symptoms("body aches", True)
                
            if ask_question("Have you lost your sense of taste or smell?", "sp_taste"):
                st.session_state.med_expert_system.update_symptoms("loss of taste or smell", True)
                
            if ask_question("Do you have a headache?", "sp_headache"):
                st.session_state.med_expert_system.update_symptoms("headache", True)
                
            if ask_question("Do you have a sore throat?", "sp_throat"):
                st.session_state.med_expert_system.update_symptoms("sore throat", True)
            
            st.subheader("Digestive Symptoms")
            if ask_question("Do you feel nauseous?", "sp_nausea"):
                st.session_state.med_expert_system.update_symptoms("nausea", True)
                
            if ask_question("Have you been vomiting?", "sp_vomit"):
                st.session_state.med_expert_system.update_symptoms("vomiting", True)
                
            if ask_question("Do you have abdominal pain?", "sp_abdomen"):
                st.session_state.med_expert_system.update_symptoms("abdominal pain", True)
                
            if ask_question("Do you have chest pain?", "sp_chest"):
                st.session_state.med_expert_system.update_symptoms("chest pain", True)
            
            submit_specific = st.form_submit_button(label="Get Specific Diagnosis")
        
        # Diagnose using medical expert system
        if submit_specific:
            st.subheader("Specific Diagnosis Results:")
            st.write(st.session_state.med_expert_system.diagnose())
            
            # Show active symptoms
            active_symptoms = [symptom for symptom, value in 
                              st.session_state.med_expert_system.symptoms.items() if value]
            
            if active_symptoms:
                st.subheader("Your reported symptoms:")
                for symptom in active_symptoms:
                    st.write(f"- {symptom}")
    
    # Disclaimer at the bottom of the page
    st.markdown("---")
    st.warning("""**DISCLAIMER**: This tool is for educational purposes only and does not provide 
                medical advice. The diagnoses provided are speculative and should not replace 
                consultation with healthcare professionals.""")

if __name__ == "__main__":
    expert_system_ui()
