from flask import Flask, request, jsonify, send_from_directory

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
        #1-30
        "what is 1 plus 1": "1 plus 1 equals 2.",
        "what is 1 plus 2": "1 plus 2 equals 3.",
        "what is 1 plus 3": "1 plus 3 equals 4.",
        "what is 1 plus 4": "1 plus 4 equals 5.",
        "what is 1 plus 5": "1 plus 5 equals 6.",
        "what is 1 plus 6": "1 plus 6 equals 7.",
        "what is 1 plus 7": "1 plus 7 equals 8.",
        "what is 1 plus 8": "1 plus 8 equals 9.",
        "what is 1 plus 9": "1 plus 9 equals 10.",
        "what is 1 plus 10": "1 plus 10 equals 11.",
        "what is 1 plus 11": "1 plus 11 equals 12.",
        "what is 1 plus 12": "1 plus 12 equals 13.",
        "what is 1 plus 13": "1 plus 13 equals 14.",
        "what is 1 plus 14": "1 plus 14 equals 15.",
        "what is 1 plus 15": "1 plus 15 equals 16.",
        "what is 1 plus 16": "1 plus 16 equals 17.",
        "what is 1 plus 17": "1 plus 17 equals 18.",
        "what is 1 plus 18": "1 plus 18 equals 19.",
        "what is 1 plus 19": "1 plus 19 equals 20.",
        "what is 1 plus 20": "1 plus 20 equals 21.",
        "what is 1 plus 21": "1 plus 21 equals 22.",
        "what is 1 plus 22": "1 plus 22 equals 23.",
        "what is 1 plus 23": "1 plus 23 equals 24.",
        "what is 1 plus 24": "1 plus 24 equals 25.",
        "what is 1 plus 25": "1 plus 25 equals 26.",
        "what is 1 plus 26": "1 plus 26 equals 27.",
        "what is 1 plus 27": "1 plus 27 equals 28.",
        "what is 1 plus 28": "1 plus 28 equals 29.",
        "what is 1 plus 29": "1 plus 29 equals 30.",
        "what is 1 plus 30": "1 plus 30 equals 31.",
        #1-30
        "what is 2 plus 1": "2 plus 1 equals 3.",
        "what is 2 plus 2": "2 plus 2 equals 4.",
        "what is 2 plus 3": "2 plus 3 equals 5.",
        "what is 2 plus 4": "2 plus 4 equals 6.",
        "what is 2 plus 5": "2 plus 5 equals 7.",
        "what is 2 plus 6": "2 plus 6 equals 8.",
        "what is 2 plus 7": "2 plus 7 equals 9.",
        "what is 2 plus 8": "2 plus 8 equals 10.",
        "what is 2 plus 9": "2 plus 9 equals 11.",
        "what is 2 plus 10": "2 plus 10 equals 12.",
        "what is 2 plus 11": "2 plus 11 equals 13.",
        "what is 2 plus 12": "2 plus 12 equals 14.",
        "what is 2 plus 13": "2 plus 13 equals 15.",
        "what is 2 plus 14": "2 plus 14 equals 16.",
        "what is 2 plus 15": "2 plus 15 equals 17.",
        "what is 2 plus 16": "2 plus 16 equals 18.",
        "what is 2 plus 17": "2 plus 17 equals 19.",
        "what is 2 plus 18": "2 plus 18 equals 20.",
        "what is 2 plus 19": "2 plus 19 equals 21.",
        "what is 2 plus 20": "2 plus 20 equals 22.",
        "what is 2 plus 21": "2 plus 21 equals 23.",
        "what is 2 plus 22": "2 plus 22 equals 24.",
        "what is 2 plus 23": "2 plus 23 equals 25.",
        "what is 2 plus 24": "2 plus 24 equals 26.",
        "what is 2 plus 25": "2 plus 25 equals 27.",
        "what is 2 plus 26": "2 plus 26 equals 28.",
        "what is 2 plus 27": "2 plus 27 equals 29.",
        "what is 2 plus 28": "2 plus 28 equals 30.",
        "what is 2 plus 29": "2 plus 29 equals 31.",
        "what is 2 plus 30": "2 plus 30 equals 32.",
        #1-30
        "what is 3 plus 1": "3 plus 1 equals 4.",
        "what is 3 plus 2": "3 plus 2 equals 5.",
        "what is 3 plus 3": "3 plus 3 equals 6.",
        "what is 3 plus 4": "3 plus 4 equals 7.",
        "what is 3 plus 5": "3 plus 5 equals 8.",
        "what is 3 plus 6": "3 plus 6 equals 9.",
        "what is 3 plus 7": "3 plus 7 equals 10.",
        "what is 3 plus 8": "3 plus 8 equals 11.",
        "what is 3 plus 9": "3 plus 9 equals 12.",
        "what is 3 plus 10": "3 plus 10 equals 13.",
        "what is 3 plus 11": "3 plus 11 equals 14.",
        "what is 3 plus 12": "3 plus 12 equals 15.",
        "what is 3 plus 13": "3 plus 13 equals 16.",
        "what is 3 plus 14": "3 plus 14 equals 17.",
        "what is 3 plus 15": "3 plus 15 equals 18.",
        "what is 3 plus 16": "3 plus 16 equals 19.",
        "what is 3 plus 17": "3 plus 17 equals 20.",
        "what is 3 plus 18": "3 plus 18 equals 21.",
        "what is 3 plus 19": "3 plus 19 equals 22.",
        "what is 3 plus 20": "3 plus 20 equals 23.",
        "what is 3 plus 21": "3 plus 21 equals 24.",
        "what is 3 plus 22": "3 plus 22 equals 25.",
        "what is 3 plus 23": "3 plus 23 equals 26.",
        "what is 3 plus 24": "3 plus 24 equals 27.",
        "what is 3 plus 25": "3 plus 25 equals 28.",
        "what is 3 plus 26": "3 plus 26 equals 29.",
        "what is 3 plus 27": "3 plus 27 equals 30.",
        "what is 3 plus 28": "3 plus 28 equals 31.",
        "what is 3 plus 29": "3 plus 29 equals 32.",
        "what is 3 plus 30": "3 plus 30 equals 33.",
        #1-34
        "what is 4 plus 1": "4 plus 1 equals 5.",
        "what is 4 plus 2": "4 plus 2 equals 6.",
        "what is 4 plus 3": "4 plus 3 equals 7.",
        "what is 4 plus 4": "4 plus 4 equals 8.",
        "what is 4 plus 5": "4 plus 5 equals 9.",
        "what is 4 plus 6": "4 plus 6 equals 10.",
        "what is 4 plus 7": "4 plus 7 equals 11.",
        "what is 4 plus 8": "4 plus 8 equals 12.",
        "what is 4 plus 9": "4 plus 9 equals 13.",
        "what is 4 plus 10": "4 plus 10 equals 14.",
        "what is 4 plus 11": "4 plus 11 equals 15.",
        "what is 4 plus 12": "4 plus 12 equals 16.",
        "what is 4 plus 13": "4 plus 13 equals 17.",
        "what is 4 plus 14": "4 plus 14 equals 18.",
        "what is 4 plus 15": "4 plus 15 equals 19.",
        "what is 4 plus 16": "4 plus 16 equals 20.",
        "what is 4 plus 17": "4 plus 17 equals 21.",
        "what is 4 plus 18": "4 plus 18 equals 22.",
        "what is 4 plus 19": "4 plus 19 equals 23.",
        "what is 4 plus 20": "4 plus 20 equals 24.",
        "what is 4 plus 21": "4 plus 21 equals 25.",
        "what is 4 plus 22": "4 plus 22 equals 26.",
        "what is 4 plus 23": "4 plus 23 equals 27.",
        "what is 4 plus 24": "4 plus 24 equals 28.",
        "what is 4 plus 25": "4 plus 25 equals 29.",
        "what is 4 plus 26": "4 plus 26 equals 30.",
        "what is 4 plus 27": "4 plus 27 equals 31.",
        "what is 4 plus 28": "4 plus 28 equals 32.",
        "what is 4 plus 29": "4 plus 29 equals 33.",
        "what is 4 plus 30": "4 plus 30 equals 34.",
        #1-35
        "what is 5 plus 1": "5 plus 1 equals 6.",
        "what is 5 plus 2": "5 plus 2 equals 7.",
        "what is 5 plus 3": "5 plus 3 equals 8.",
        "what is 5 plus 4": "5 plus 4 equals 9.",
        "what is 5 plus 5": "5 plus 5 equals 10.",
        "what is 5 plus 6": "5 plus 6 equals 11.",
        "what is 5 plus 7": "5 plus 7 equals 12.",
        "what is 5 plus 8": "5 plus 8 equals 13.",
        "what is 5 plus 9": "5 plus 9 equals 14.",
        "what is 5 plus 10": "5 plus 10 equals 15.",
        "what is 5 plus 11": "5 plus 11 equals 16.",
        "what is 5 plus 12": "5 plus 12 equals 17.",
        "what is 5 plus 13": "5 plus 13 equals 18.",
        "what is 5 plus 14": "5 plus 14 equals 19.",
        "what is 5 plus 15": "5 plus 15 equals 20.",
        "what is 5 plus 16": "5 plus 16 equals 21.",
        "what is 5 plus 17": "5 plus 17 equals 22.",
        "what is 5 plus 18": "5 plus 18 equals 23.",
        "what is 5 plus 19": "5 plus 19 equals 24.",
        "what is 5 plus 20": "5 plus 20 equals 25.",
        "what is 5 plus 21": "5 plus 21 equals 26.",
        "what is 5 plus 22": "5 plus 22 equals 27.",
        "what is 5 plus 23": "5 plus 23 equals 28.",
        "what is 5 plus 24": "5 plus 24 equals 29.",
        "what is 5 plus 25": "5 plus 25 equals 30.",
        "what is 5 plus 26": "5 plus 26 equals 31.",
        "what is 5 plus 27": "5 plus 27 equals 32.",
        "what is 5 plus 28": "5 plus 28 equals 33.",
        "what is 5 plus 29": "5 plus 29 equals 34.",
        "what is 5 plus 30": "5 plus 30 equals 35.",
        #1-30
        "what is 6 plus 1": "6 plus 1 equals 7.",
        "what is 6 plus 2": "6 plus 2 equals 8.",
        "what is 6 plus 3": "6 plus 3 equals 9.",
        "what is 6 plus 4": "6 plus 4 equals 10.",
        "what is 6 plus 5": "6 plus 5 equals 11.",
        "what is 6 plus 6": "6 plus 6 equals 12.",
        "what is 6 plus 7": "6 plus 7 equals 13.",
        "what is 6 plus 8": "6 plus 8 equals 14.",
        "what is 6 plus 9": "6 plus 9 equals 15.",
        "what is 6 plus 10": "6 plus 10 equals 16.",
        "what is 6 plus 11": "6 plus 11 equals 17.",
        "what is 6 plus 12": "6 plus 12 equals 18.",
        "what is 6 plus 13": "6 plus 13 equals 19.",
        "what is 6 plus 14": "6 plus 14 equals 20.",
        "what is 6 plus 15": "6 plus 15 equals 21.",
        "what is 6 plus 16": "6 plus 16 equals 22.",
        "what is 6 plus 17": "6 plus 17 equals 23.",
        "what is 6 plus 18": "6 plus 18 equals 24.",
        "what is 6 plus 19": "6 plus 19 equals 25.",
        "what is 6 plus 20": "6 plus 20 equals 26.",
        "what is 6 plus 21": "6 plus 21 equals 27.",
        "what is 6 plus 22": "6 plus 22 equals 28.",
        "what is 6 plus 23": "6 plus 23 equals 29.",
        "what is 6 plus 24": "6 plus 24 equals 30.",
        "what is 6 plus 25": "6 plus 25 equals 31.",
        "what is 6 plus 26": "6 plus 26 equals 32.",
        "what is 6 plus 27": "6 plus 27 equals 33.",
        "what is 6 plus 28": "6 plus 28 equals 34.",
        "what is 6 plus 29": "6 plus 29 equals 35.",
        "what is 6 plus 30": "6 plus 30 equals 36.",
        #1-30
        "what is 7 plus 1": "7 plus 1 equals 8.",
        "what is 7 plus 2": "7 plus 2 equals 9.",
        "what is 7 plus 3": "7 plus 3 equals 10.",
        "what is 7 plus 4": "7 plus 4 equals 11.",
        "what is 7 plus 5": "7 plus 5 equals 12.",
        "what is 7 plus 6": "7 plus 6 equals 13.",
        "what is 7 plus 7": "7 plus 7 equals 14.",
        "what is 7 plus 8": "7 plus 8 equals 15.",
        "what is 7 plus 9": "7 plus 9 equals 16.",
        "what is 7 plus 10": "7 plus 10 equals 17.",
        "what is 7 plus 11": "7 plus 11 equals 18.",
        "what is 7 plus 12": "7 plus 12 equals 19.",
        "what is 7 plus 13": "7 plus 13 equals 20.",
        "what is 7 plus 14": "7 plus 14 equals 21.",
        "what is 7 plus 15": "7 plus 15 equals 22.",
        "what is 7 plus 16": "7 plus 16 equals 23.",
        "what is 7 plus 17": "7 plus 17 equals 24.",
        "what is 7 plus 18": "7 plus 18 equals 25.",
        "what is 7 plus 19": "7 plus 19 equals 26.",
        "what is 7 plus 20": "7 plus 20 equals 27.",
        "what is 7 plus 21": "7 plus 21 equals 28.",
        "what is 7 plus 22": "7 plus 22 equals 29.",
        "what is 7 plus 23": "7 plus 23 equals 30.",
        "what is 7 plus 24": "7 plus 24 equals 31.",
        "what is 7 plus 25": "7 plus 25 equals 32.",
        "what is 7 plus 26": "7 plus 26 equals 33.",
        "what is 7 plus 27": "7 plus 27 equals 34.",
        "what is 7 plus 28": "7 plus 28 equals 35.",
        "what is 7 plus 29": "7 plus 29 equals 36.",
        "what is 7 plus 30": "7 plus 30 equals 37.",
        #1-30
        "what is 8 plus 1": "8 plus 1 equals 9.",
        "what is 8 plus 2": "8 plus 2 equals 10.",
        "what is 8 plus 3": "8 plus 3 equals 11.",
        "what is 8 plus 4": "8 plus 4 equals 12.",
        "what is 8 plus 5": "8 plus 5 equals 13.",
        "what is 8 plus 6": "8 plus 6 equals 14.",
        "what is 8 plus 7": "8 plus 7 equals 15.",
        "what is 8 plus 8": "8 plus 8 equals 16.",
        "what is 8 plus 9": "8 plus 9 equals 17.",
        "what is 8 plus 10": "8 plus 10 equals 18.",
        "what is 8 plus 11": "8 plus 11 equals 19.",
        "what is 8 plus 12": "8 plus 12 equals 20.",
        "what is 8 plus 13": "8 plus 13 equals 21.",
        "what is 8 plus 14": "8 plus 14 equals 22.",
        "what is 8 plus 15": "8 plus 15 equals 23.",
        "what is 8 plus 16": "8 plus 16 equals 24.",
        "what is 8 plus 17": "8 plus 17 equals 25.",
        "what is 8 plus 18": "8 plus 18 equals 26.",
        "what is 8 plus 19": "8 plus 19 equals 27.",
        "what is 8 plus 20": "8 plus 20 equals 28.",
        "what is 8 plus 21": "8 plus 21 equals 29.",
        "what is 8 plus 22": "8 plus 22 equals 30.",
        "what is 8 plus 23": "8 plus 23 equals 31.",
        "what is 8 plus 24": "8 plus 24 equals 32.",
        "what is 8 plus 25": "8 plus 25 equals 33.",
        "what is 8 plus 26": "8 plus 26 equals 34.",
        "what is 8 plus 27": "8 plus 27 equals 35.",
        "what is 8 plus 28": "8 plus 28 equals 36.",
        "what is 8 plus 29": "8 plus 29 equals 37.",
        "what is 8 plus 30": "8 plus 30 equals 38.",
        #1-30
        "what is 9 plus 1": "9 plus 1 equals 10.",
        "what is 9 plus 2": "9 plus 2 equals 11.",
        "what is 9 plus 3": "9 plus 3 equals 12.",
        "what is 9 plus 4": "9 plus 4 equals 13.",
        "what is 9 plus 5": "9 plus 5 equals 14.",
        "what is 9 plus 6": "9 plus 6 equals 15.",
        "what is 9 plus 7": "9 plus 7 equals 16.",
        "what is 9 plus 8": "9 plus 8 equals 17.",
        "what is 9 plus 9": "9 plus 9 equals 18.",
        "what is 9 plus 10": "9 plus 10 equals 19.",
        "what is 9 plus 11": "9 plus 11 equals 20.",
        "what is 9 plus 12": "9 plus 12 equals 21.",
        "what is 9 plus 13": "9 plus 13 equals 22.",
        "what is 9 plus 14": "9 plus 14 equals 23.",
        "what is 9 plus 15": "9 plus 15 equals 24.",
        "what is 9 plus 16": "9 plus 16 equals 25.",
        "what is 9 plus 17": "9 plus 17 equals 26.",
        "what is 9 plus 18": "9 plus 18 equals 27.",
        "what is 9 plus 19": "9 plus 19 equals 28.",
        "what is 9 plus 20": "9 plus 20 equals 29.",
        "what is 9 plus 21": "9 plus 21 equals 30.",
        "what is 9 plus 22": "9 plus 22 equals 31.",
        "what is 9 plus 23": "9 plus 23 equals 32.",
        "what is 9 plus 24": "9 plus 24 equals 33.",
        "what is 9 plus 25": "9 plus 25 equals 34.",
        "what is 9 plus 26": "9 plus 26 equals 35.",
        "what is 9 plus 27": "9 plus 27 equals 36.",
        "what is 9 plus 28": "9 plus 28 equals 37.",
        "what is 9 plus 29": "9 plus 29 equals 38.",
        "what is 9 plus 30": "9 plus 30 equals 39.",
        # 1-30
        "what is 10 plus 01": "10 plus 1 equals 11.",
       "what is 10 plus 02": "10 plus 2 equals 12.",
        "what is 10 plus 03": "10 plus 3 equals 13.",
        "what is 10 plus 04": "10 plus 4 equals 14.",
        "what is 10 plus 05": "10 plus 5 equals 15.",
        "what is 10 plus 06": "10 plus 6 equals 16.",
        "what is 10 plus 07": "10 plus 7 equals 17.",
        "what is 10 plus 08": "10 plus 8 equals 18.",
        "what is 10 plus 09": "10 plus 9 equals 19.",
        "what is 10 plus 10": "10 plus 10 equals 20.",
        "what is 10 plus 11": "10 plus 11 equals 21.",
        "what is 10 plus 12": "10 plus 12 equals 22.",
        "what is 10 plus 13": "10 plus 13 equals 23.",
        "what is 10 plus 14": "10 plus 14 equals 24.",
        "what is 10 plus 15": "10 plus 15 equals 25.",
        "what is 10 plus 16": "10 plus 16 equals 26.",
        "what is 10 plus 17": "10 plus 17 equals 27.",
        "what is 10 plus 18": "10 plus 18 equals 28.",
        "what is 10 plus 19": "10 plus 19 equals 29.",
        "what is 10 plus 20": "10 plus 20 equals 30.",
        "what is 10 plus 21": "10 plus 21 equals 31.",
        "what is 10 plus 22": "10 plus 22 equals 32.",
        "what is 10 plus 23": "10 plus 23 equals 33.",
        "what is 10 plus 24": "10 plus 24 equals 34.",
        "what is 10 plus 25": "10 plus 25 equals 35.",
        "what is 10 plus 26": "10 plus 26 equals 36.",
        "what is 10 plus 27": "10 plus 27 equals 37.",
        "what is 10 plus 28": "10 plus 28 equals 38.",
        "what is 10 plus 29": "10 plus 29 equals 39.",
        "what is 10 plus 30": "10 plus 30 equals 40.",
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
    "who is the current president of the usa": "As of 2024, the current President of the USA is Joe Biden.",
    "what is the capital of russia": "The capital of Russia is Moscow.",
    "what is the capital of china": "The capital of China is Beijing.",
    "what is the capital of brazil": "The capital of Brazil is Brasília.",
    "who was the 45th president of the usa": "Donald Trump was the 45th President of the USA.",
    "what is the capital of india": "The capital of India is New Delhi.",
    "who was the 3rd president of the usa": "Thomas Jefferson was the 3rd President of the USA.",
    "who was the 4th president of the usa": "James Madison was the 4th President of the USA.",
    "who was the 5th president of the usa": "James Monroe was the 5th President of the USA.",
    "what is the chemical symbol for sodium": "The chemical symbol for sodium is Na.",
    "who was the 6th president of the usa": "John Quincy Adams was the 6th President of the USA.",
    "what is the capital of spain": "The capital of Spain is Madrid.",
    "what is the chemical symbol for potassium": "The chemical symbol for potassium is K.",
    "who was the 7th president of the usa": "Andrew Jackson was the 7th President of the USA.",
    "what is the capital of mexico": "The capital of Mexico is Mexico City.",
    "what is the chemical symbol for calcium": "The chemical symbol for calcium is Ca.",
    "who was the 8th president of the usa": "Martin Van Buren was the 8th President of the USA.",
    "what is the capital of egypt": "The capital of Egypt is Cairo.",
    "what is the chemical symbol for chlorine": "The chemical symbol for chlorine is Cl.",
    "who was the 9th president of the usa": "William Henry Harrison was the 9th President of the USA.",
    "what is the capital of south korea": "The capital of South Korea is Seoul.",
    "what is the chemical symbol for nitrogen": "The chemical symbol for nitrogen is N.",
    "who was the 10th president of the usa": "John Tyler was the 10th President of the USA.",
    "what is the capital of north korea": "The capital of North Korea is Pyongyang.",
    "what is the chemical symbol for carbon": "The chemical symbol for carbon is C.",
    "who was the 11th president of the usa": "James K. Polk was the 11th President of the USA.",
    "what is the capital of vietnam": "The capital of Vietnam is Hanoi.",
    "what is the chemical symbol for oxygen": "The chemical symbol for oxygen is O.",
    "who was the 12th president of the usa": "Zachary Taylor was the 12th President of the USA.",
    "what is the capital of thailand": "The capital of Thailand is Bangkok.",
    "what is the chemical symbol for helium": "The chemical symbol for helium is He.",
        # Add more responses as needed
    }
   
    # Normalize the user input
    user_input = user_input.lower()
   
    # Return the response from the dictionary or a default message
    return responses.get(user_input, "Sorry, I don't understand that question.")
    
# Serve the index.html file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')
    
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

