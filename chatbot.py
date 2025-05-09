from nltk.chat.util import Chat, reflections

# Define movies and showtimes
movies = {
    'Interstellar': ['Morning: 10:00 AM', 'Afternoon: 2:00 PM', 'Evening: 6:00 PM'],
    'The Dark Knight': ['Morning: 11:00 AM', 'Afternoon: 3:00 PM', 'Evening: 7:00 PM'],
    'Dune': ['Morning: 9:30 AM', 'Afternoon: 1:30 PM', 'Evening: 5:30 PM']
}

# Function to return formatted showtimes
def get_showtimes():
    response = "Here are the showtimes for the available movies:\n"
    for movie, timings in movies.items():
        response += f"{movie}: {', '.join(timings)}\n"
    return response.strip()

# Chat patterns (no timing/showtime pattern here anymore)
patterns = [
    (r'hi|hello|hey', 
     ['Hello! How can I assist you today?', 'Hey there! What can I do for you?', 'Hi! Ready to book some movie tickets?']),
    (r'how are you', 
     ['I am just a bot, but I am always ready to help you book tickets!']),
    (r'(.*) movie', 
     ['Here is the list of movies: ' + ', '.join(movies.keys()) + '. Which movie would you like to watch?']),
    (r'(.*) ticket', 
     ['How many tickets do you need?', 'Sure! How many tickets would you like to book?']),
    (r'(.*) (morning|afternoon|evening|night)', 
     ['We have showtimes available in the morning, afternoon, evening, and night. When would you like to watch?']),
    (r'(.*) book tickets', 
     ['Sure! Let\'s proceed with booking tickets.']),
    (r'(.*) (bye|goodbye)', 
     ['Thank you for visiting ChatBot. Have a great day!', 'Goodbye! Enjoy your movie!']),
]

# Create chatbot instance
tea_bot = Chat(patterns, reflections)

# Booking logic
def book_tickets(movie, tickets, showtime):
    ticket_price = 100  # Fixed price
    total_bill = tickets * ticket_price
    return f"Booking confirmed! You have booked {tickets} tickets for {movie} at {showtime}.\nTotal amount: Rs. {total_bill}."

# Main chatbot loop
def main():
    print("\nHello! Welcome to ChatBot. How can I assist you today?")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        # Check for showtime/timing manually
        if 'showtime' in user_input or 'timing' in user_input or 'show time' in user_input or 'show' in user_input:
            print("ChatBot:", get_showtimes())
            continue

        # Default response from NLTK Chat
        response = tea_bot.respond(user_input)
        print("ChatBot:", response if response else "I'm sorry, could you please rephrase that?")
        
        # Ticket booking dialog
        if "book tickets" in user_input:
            movie = input("Which movie would you like to watch? :")
            tickets = int(input("How many tickets do you need? :"))
            showtime = input("At what time would you like to watch the movie? :")
            booking_response = book_tickets(movie, tickets, showtime)
            print("ChatBot:", booking_response)

        # Exit condition
        if 'bye' in user_input or 'goodbye' in user_input:
            break

main()
