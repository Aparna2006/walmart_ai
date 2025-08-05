def chatbot_response(query):
    keywords = {
        "toothpaste": "Aisle 3, Personal Care section.",
        "shampoo": "Aisle 4, Hair Care section.",
        "milk": "Aisle 1, Dairy section."
    }
    for keyword in keywords:
        if keyword in query.lower():
            return keywords[keyword]
    return "Sorry, I couldn't find that. Please ask a store associate."
