from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a chatbot response function with enhanced capabilities
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm doing great, thank you for asking!",
        "what is your name": "I am a chatbot created to help you.",
        "what is 1 plus 1": "1 plus 1 equals 2.",
        "what is two plus two": "Two plus two equals four.",
        "bye": "Goodbye! Have a great day!",
        "what is the weather": "I'm not sure, but you can check a weather website.",
        "what time is it": "I don't have access to the current time.",
        "who was the first president of the usa": "George Washington was the first President of the USA.",
        "what is the capital of france": "The capital of France is Paris.",
        "who wrote 'to kill a mockingbird'": "Harper Lee wrote 'To Kill a Mockingbird'.",
        "what is the chemical formula for water": "The chemical formula for water is H2O.",
        "who was albert einstein": "Albert Einstein was a theoretical physicist known for developing the theory of relativity.",
        "what is the largest planet in our solar system": "The largest planet in our solar system is Jupiter.",
        "who painted the mona lisa": "The Mona Lisa was painted by Leonardo da Vinci.",
        "what is the boiling point of water": "The boiling point of water is 100 degrees Celsius or 212 degrees Fahrenheit.",
        "who discovered penicillin": "Penicillin was discovered by Alexander Fleming.",
        "what is the speed of light": "The speed of light is approximately 299,792,458 meters per second.",
        "who is the author of '1984'": "George Orwell is the author of '1984'.",
        "what is the pythagorean theorem": "The Pythagorean theorem states that in a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.",
        "what is the distance between the earth and the sun": "The average distance between the Earth and the Sun is about 93 million miles or 150 million kilometers.",
        "who was the first man to walk on the moon": "Neil Armstrong was the first man to walk on the moon.",
        "what is the capital of japan": "The capital of Japan is Tokyo.",
        "what is the chemical symbol for gold": "The chemical symbol for gold is Au.",
        "who wrote 'romeo and juliet'": "William Shakespeare wrote 'Romeo and Juliet'.",
        "what is the tallest mountain in the world": "The tallest mountain in the world is Mount Everest.",
        "what is the formula for calculating the area of a circle": "The formula for calculating the area of a circle is πr², where r is the radius of the circle.",
        "who was the second president of the usa": "John Adams was the second President of the USA.",
        "what is the capital of italy": "The capital of Italy is Rome.",
        "what is the freezing point of water": "The freezing point of water is 0 degrees Celsius or 32 degrees Fahrenheit.",
        "who developed the theory of evolution": "Charles Darwin developed the theory of evolution.",
        "what is the largest ocean on earth": "The largest ocean on Earth is the Pacific Ocean.",
        "who wrote 'the great gatsby'": "F. Scott Fitzgerald wrote 'The Great Gatsby'.",
        "what is the currency of the united kingdom": "The currency of the United Kingdom is the British Pound Sterling.",
        "who discovered america": "Christopher Columbus is often credited with discovering America in 1492.",
        "what is the chemical formula for carbon dioxide": "The chemical formula for carbon dioxide is CO2.",
        "who was the first female prime minister of the uk": "Margaret Thatcher was the first female Prime Minister of the UK.",
        "what is the human body's largest organ": "The human body's largest organ is the skin.",
        "who wrote 'moby-dick'": "Herman Melville wrote 'Moby-Dick'.",
        "what is the chemical formula for table salt": "The chemical formula for table salt is NaCl.",
        "who was the 16th president of the usa": "Abraham Lincoln was the 16th President of the USA.",
        "what is the capital of germany": "The capital of Germany is Berlin.",
        "what is the atomic number of hydrogen": "The atomic number of hydrogen is 1.",
        "who invented the telephone": "Alexander Graham Bell is credited with inventing the telephone.",
        "what is the smallest country in the world": "The smallest country in the world is Vatican City.",
        "what is the distance between the earth and the moon": "The average distance between the Earth and the Moon is about 238,855 miles or 384,400 kilometers.",
        "who painted the last supper": "The Last Supper was painted by Leonardo da Vinci.",
        "what is the largest desert in the world": "The largest desert in the world is the Sahara Desert.",
        "who wrote 'pride and prejudice'": "Jane Austen wrote 'Pride and Prejudice'.",
        "what is the chemical symbol for iron": "The chemical symbol for iron is Fe.",
        "who was the first person to reach the south pole": "Roald Amundsen was the first person to reach the South Pole.",
        "what is the capital of australia": "The capital of Australia is Canberra.",
        "what is the formula for calculating the volume of a sphere": "The formula for calculating the volume of a sphere is 4/3πr³, where r is the radius of the sphere.",
        "who wrote 'the adventures of huckleberry finn'": "Mark Twain wrote 'The Adventures of Huckleberry Finn'.",
        "what is the chemical formula for methane": "The chemical formula for methane is CH4.",
        "who was the 44th president of the usa": "Barack Obama was the 44th President of the USA.",
        "what is the capital of canada": "The capital of Canada is Ottawa.",
        "what is the atomic number of oxygen": "The atomic number of oxygen is 8.",
        "who invented the light bulb": "Thomas Edison is credited with inventing the light bulb.",
        "what is the largest lake in the world": "The largest lake in the world by surface area is the Caspian Sea.",
        "what is the currency of japan": "The currency of Japan is the Japanese Yen.",
        "who was the first woman in space": "Valentina Tereshkova was the first woman in space.",
        "what is the capital of russia": "The capital of Russia is Moscow.",
        "what is the chemical symbol for sodium": "The chemical symbol for sodium is Na.",
        "who discovered gravity": "Sir Isaac Newton is credited with discovering gravity.",
        "what is the smallest bone in the human body": "The smallest bone in the human body is the stapes, located in the middle ear.",
        "what is the chemical formula for glucose": "The chemical formula for glucose is C6H12O6.",
        "who was the 35th president of the usa": "John F. Kennedy was the 35th President of the USA.",
        "what is the capital of india": "The capital of India is New Delhi.",
        "what is the atomic number of carbon": "The atomic number of carbon is 6.",
        "who invented the airplane": "The Wright brothers, Orville and Wilbur Wright, are credited with inventing the airplane.",
        "what is the largest continent": "The largest continent is Asia.",
        "who wrote 'war and peace'": "Leo Tolstoy wrote 'War and Peace'.",
        "what is the chemical formula for sulfuric acid": "The chemical formula for sulfuric acid is H2SO4.",
        "who was the 3rd president of the usa": "Thomas Jefferson was the 3rd President of the USA.",
        "what is the capital of china": "The capital of China is Beijing.",
        "what is the atomic number of helium": "The atomic number of helium is 2.",
        "who invented the internet": "The development of the internet was a collaborative effort by many individuals and organizations, but Vint Cerf and Bob Kahn are often credited with developing the foundational protocols.",
        # Add more responses as needed
    }
   
    # Normalize the user input
    user_input = user_input.lower()
   
    # Return the response from the dictionary or a default message
    return responses.get(user_input, "Sorry, I don't understand that question.")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

