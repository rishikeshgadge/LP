from nltk.chat.util import Chat, reflections
import datetime

pairs = [
    (r'\bhi\b|\bhello\b', ['hi there, I am chatbot', 'Hello, I am chatbot']),
    (r'\bhow are you\b', ['I am goot thank you!']),
    (r'\bwho are you\b', ['I am chatbot, I am here to help you']),
    (r'\bquit\b', ["type 'exit' to quit"]),
    (r'\bproducts\b', ['mobiles\nlaptops\ndesktops']),
    (r'\bbye\b', ['bye!'])
]

orders = {
    1 : 'processing'
}

info = {
    1: "samsung galaxy a5\nApple mac book pro"
}

chatbot = Chat(pairs, reflections)

print("This is a chatbot application!(type 'exit' to quit)")
while True:
    inp = input("You: ").lower()

    if inp == 'exit':
        break

    elif 'time' in inp or 'date' in inp:
        print(datetime.datetime.now())

    elif 'status' in inp:
        orderid = int(input('orderid: '))
        if orderid in orders:
            print("The order is " + orders[orderid])
        else:
            print('orderid not found')
    
    elif 'refund' in inp:
        orderid = int(input('orderid: '))
        if orderid in orders:
            if orders[orderid] == 'refunded':
                print("already refunded")
            else:
                print("intiated refund")
                orders[orderid] = 'refunded'
        else:
            print('orderid not found')
    
    elif "order" in inp:
        orderid = int(input('orderid: '))
        if orderid in info:
            print(info[orderid])
        else:
            print('orderid not found')
    
    else:
        response = chatbot.respond(inp)
        if response:
            print(response)
        else:
            print("I did not understand the command please try again!")
    print()