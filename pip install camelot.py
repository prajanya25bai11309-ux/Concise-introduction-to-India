import random
import time

# Indian states with folk tales, famous places, and historical landmarks
STATES_DATA = {
    "Andhra Pradesh": {
        "tale": "Long ago in the Godavari delta, a poor farmer found a magical drum. Every time he beat it, food appeared! He shared it with his village. A greedy king heard about it and stole the drum, but when he played it, only stones came out. The farmer explained: 'The drum responds to kindness, not greed.' The king returned it and learned to be generous.",
        "conclusion": "True magic lies in sharing, not hoarding.",
        "places": ["Tirupati Temple - Ancient hilltop temple, one of the richest in the world", 
                   "Charminar, Hyderabad - 16th century monument symbolizing the city",
                   "Golconda Fort - Medieval fortress famous for its acoustics and diamond trade"],
        "history": "Known as the 'Rice Bowl of India'. Home to the Satavahana dynasty and later the mighty Vijayanagara Empire. Hyderabad was ruled by the Nizams, known for their wealth and culture."
    },
    "Arunachal Pradesh": {
        "tale": "High in the mountains, a young boy chased a golden deer through the clouds. The deer led him to a hidden valley where the sun was trapped in a cage by jealous spirits. The boy freed the sun, and it blessed him with courage. When he returned, his village prospered, and the mountains glowed with eternal beauty.",
        "conclusion": "Courage lights up the darkest places.",
        "places": ["Tawang Monastery - Largest monastery in India, 400 years old",
                   "Ziro Valley - UNESCO Heritage Site, home to the Apatani tribe",
                   "Sela Pass - Breathtaking high-altitude pass at 13,700 feet"],
        "history": "Land of the rising sun in India. Home to diverse indigenous tribes with rich oral traditions. Has historical Buddhist monasteries and was an important part of ancient trade routes between India and Tibet."
    },
    "Assam": {
        "tale": "The mighty Brahmaputra River once had a daughter who loved to dance. When invaders threatened the land, she danced so beautifully that the enemy soldiers forgot their weapons and started dancing too. The kingdom was saved through the power of art, not war.",
        "conclusion": "Art and culture are the greatest warriors.",
        "places": ["Kaziranga National Park - Home to two-thirds of world's one-horned rhinos",
                   "Kamakhya Temple - Ancient Shakti Peeth shrine",
                   "Majuli Island - World's largest river island, center of Vaishnavite culture"],
        "history": "Gateway to Northeast India. Was ruled by the Ahom dynasty for 600 years, one of the longest-reigning dynasties in India. Famous for tea plantations established by the British in the 19th century."
    },
    "Bihar": {
        "tale": "Under the Bodhi tree in ancient Magadha, a prince sat meditating while a demon tried to distract him with illusions of fear and desire. The prince remained calm, touching the earth as witness to his compassion. At dawn, he became Buddha, the enlightened one, showing that inner peace conquers all darkness.",
        "conclusion": "Enlightenment comes from inner stillness, not external battles.",
        "places": ["Mahabodhi Temple, Bodh Gaya - Where Buddha attained enlightenment, UNESCO site",
                   "Nalanda University ruins - Ancient world's first residential university",
                   "Vikramshila University ruins - Major center of Buddhist learning"],
        "history": "Birthplace of Buddhism and Jainism. Home to the powerful Maurya and Gupta empires. Nalanda University attracted scholars from across Asia from 5th to 12th century CE before being destroyed."
    },
    "Chhattisgarh": {
        "tale": "In the dense forests, tribal elders tell of a shepherd who shared his food with a wounded tiger. Years later, when hunters chased the shepherd, that same tiger appeared and led him to safety through secret jungle paths. The forest remembers kindness forever.",
        "conclusion": "Kindness plants seeds that grow into protection.",
        "places": ["Chitrakote Falls - India's Niagara, spectacular waterfall",
                   "Bhoramdeo Temple - 11th century temple called 'Khajuraho of Chhattisgarh'",
                   "Kanger Valley National Park - Underground limestone caves and wildlife"],
        "history": "Rich in tribal culture and ancient temples. Was part of the Kalchuri and Satavahana kingdoms. The region has evidence of human habitation from the paleolithic age with cave paintings."
    },
    "Goa": {
        "tale": "A Portuguese merchant's daughter fell in love with a local fisherman. Her father forbade it, so they prayed at different temples. One moonlit night, the sea parted, creating a golden path where they met. Realizing love transcends all barriers, the merchant blessed their union, and both communities celebrated together on the beaches.",
        "conclusion": "Love builds bridges between all shores.",
        "places": ["Basilica of Bom Jesus - UNESCO site holding St. Francis Xavier's remains",
                   "Aguada Fort - 17th century Portuguese fort with lighthouse",
                   "Dudhsagar Falls - Four-tiered waterfall meaning 'Sea of Milk'"],
        "history": "Portuguese colony for 450 years until 1961. Blend of Indian and Portuguese cultures visible in architecture and cuisine. Important spice trading port that attracted European colonizers."
    },
    "Gujarat": {
        "tale": "In Dwarka, young Krishna lifted an entire mountain on his little finger to protect villagers from torrential rains sent by an angry god. The villagers huddled underneath for seven days. The god, impressed by Krishna's devotion to his people, blessed the land with prosperity forever.",
        "conclusion": "True leaders shield their people from any storm.",
        "places": ["Somnath Temple - One of 12 Jyotirlingas, rebuilt after destructions",
                   "Rann of Kutch - Vast white salt desert, spectacular during full moon",
                   "Dholavira - Harappan civilization ruins, 5000 years old"],
        "history": "Birthplace of Mahatma Gandhi. Home to the ancient Indus Valley civilization. Gujarat has been a major maritime trading hub for millennia, connecting India with Africa and Europe."
    },
    "Haryana": {
        "tale": "On the battlefield of Kurukshetra, warrior Arjuna faced his cousins in war and froze. Lord Krishna became his charioteer and taught him about duty, purpose, and the eternal soul. This divine conversation, the Bhagavad Gita, became wisdom for all humanity.",
        "conclusion": "Your duty, done with devotion, leads to liberation.",
        "places": ["Kurukshetra - Site of the Mahabharata war",
                   "Sultanpur Bird Sanctuary - Winter home to migratory birds",
                   "Panipat - Site of three historic battles that shaped India"],
        "history": "The land of the Mahabharata epic. Site of the crucial battles of Panipat that decided Delhi's rulers. Important agricultural region surrounding the capital."
    },
    "Himachal Pradesh": {
        "tale": "A shepherd boy in the Himalayas saved a frozen serpent. The serpent was the king of nagas who rewarded him with a gem that could control weather. The boy used it only to protect crops from hail, never for personal gain. The mountains blessed him with eternal youth to guard the valleys forever.",
        "conclusion": "Selfless power becomes eternal blessing.",
        "places": ["Shimla - Summer capital of British India, toy train UNESCO site",
                   "Rohtang Pass - Gateway to Lahaul and Spiti valleys",
                   "Hidimba Devi Temple - Ancient cave temple in Manali"],
        "history": "Land of gods with thousands of temples. Was composed of numerous hill kingdoms. Became popular British summer retreat. Rich in Tibetan Buddhist culture in upper regions."
    },
    "Jharkhand": {
        "tale": "In Santhal tribal lore, two lovers transformed into trees growing from opposite riverbanks. During droughts, their branches would stretch across and touch, and rain would fall. The tribes learned that unity brings life even in the harshest times.",
        "conclusion": "Connection nourishes life in the driest seasons.",
        "places": ["Hundru Falls - 320 feet waterfall near Ranchi",
                   "Parasnath Hills - Sacred Jain pilgrimage site",
                   "Betla National Park - Tiger reserve with ancient forts"],
        "history": "Separated from Bihar in 2000. Rich in minerals and tribal culture. Home to Birsa Munda who led tribal resistance against British. Has evidence of Stone Age settlements."
    },
    "Karnataka": {
        "tale": "The Hoysala king found a boy fighting a tiger with bare hands. Impressed, he made him army chief. The boy, named 'Sala,' founded the Hoysala dynasty. Before every battle, he would feed the poor, believing that a kingdom is only as strong as its weakest citizen.",
        "conclusion": "A nation's strength flows from its compassion.",
        "places": ["Hampi - UNESCO site, ruins of Vijayanagara Empire",
                   "Mysore Palace - Indo-Saracenic palace lit with 100,000 lights",
                   "Belur and Halebidu - Intricately carved Hoysala temples"],
        "history": "Home to powerful empires: Chalukyas, Hoysalas, and Vijayanagara. Tipu Sultan's kingdom resisted British expansion. Bengaluru became India's Silicon Valley in the late 20th century."
    },
    "Kerala": {
        "tale": "King Mahabali ruled Kerala so justly that even gods became jealous. During Onam, he returns to visit his people who once prospered under his rule. The festival celebrates not a god, but a king who loved his people more than power itself.",
        "conclusion": "True rulers live forever in their people's hearts.",
        "places": ["Backwaters of Alleppey - Network of lagoons and lakes",
                   "Padmanabhaswamy Temple - Ancient temple with mysterious vaults",
                   "Athirappilly Falls - Largest waterfall in Kerala"],
        "history": "Known as 'God's Own Country.' First state with 100% literacy. Historic spice trade attracted Romans, Arabs, Chinese, and Europeans. Witnessed Syrian Christian and Jewish settlements from ancient times."
    },
    "Madhya Pradesh": {
        "tale": "In Ujjain, a poor priest's lamp never went out though he had no oil. Lord Shiva himself appeared, explaining that the priest's devotion was the fuel. The priest learned that faith needs no material wealth to burn bright.",
        "conclusion": "True devotion lights its own way.",
        "places": ["Khajuraho Temples - UNESCO site with intricate sculptures",
                   "Sanchi Stupa - Buddhist monument built by Emperor Ashoka",
                   "Gwalior Fort - Ancient hilltop fortress called 'Gibraltar of India'"],
        "history": "Heart of India with most UNESCO sites. Home to ancient rock shelters at Bhimbetka showing Stone Age art. Ruled by numerous dynasties including Mauryas, Guptas, and Mughals."
    },
    "Maharashtra": {
        "tale": "Young Shivaji disguised himself as a merchant to scout enemy forts. When captured, he didn't fight but told the general stories of honor and freedom. The general, moved by his courage and vision, joined Shivaji's cause. Sometimes words win battles swords cannot.",
        "conclusion": "Vision and courage inspire even adversaries.",
        "places": ["Ajanta and Ellora Caves - UNESCO rock-cut cave temples",
                   "Gateway of India, Mumbai - Iconic 1924 monument",
                   "Raigad Fort - Capital of Maratha Empire under Shivaji"],
        "history": "Home to the Maratha Empire that challenged Mughal rule. Mumbai became major port city under British. Birthplace of Indian film industry (Bollywood) and important industrial hub."
    },
    "Odisha": {
        "tale": "Emperor Ashoka won the brutal Kalinga War, but the suffering he witnessed transformed him. Walking through blood-soaked fields, he renounced violence, embraced Buddhism, and spread peace across Asia. From history's bloodiest warrior emerged its greatest messenger of peace.",
        "conclusion": "The greatest victory is conquering one's own violence.",
        "places": ["Konark Sun Temple - UNESCO site, chariot-shaped temple",
                   "Jagannath Temple, Puri - Ancient pilgrimage site",
                   "Chilika Lake - Largest coastal lagoon in India"],
        "history": "Ancient Kalinga kingdom known for maritime trade with Southeast Asia. Rich tradition of classical Odissi dance. Famous for Jagannath Rath Yatra festival drawing millions."
    },
    "Punjab": {
        "tale": "Guru Nanak saw people throwing water toward the sun for their ancestors. He started throwing it westward. When asked why, he said, 'If water reaches your ancestors in heaven, surely it will reach my fields!' This wit taught people to question blind rituals and think freely.",
        "conclusion": "Question tradition with wisdom, not disrespect.",
        "places": ["Golden Temple, Amritsar - Holiest Sikh shrine, serves 100,000 free meals daily",
                   "Jallianwala Bagh - Memorial of 1919 massacre",
                   "Wagah Border - Evening flag ceremony with Pakistan"],
        "history": "Land of five rivers. Birthplace of Sikhism. Witnessed partition violence in 1947. Green Revolution started here, making India food-secure. Rich warrior tradition."
    },
    "Rajasthan": {
        "tale": "Queen Padmini's beauty was legendary. When Alauddin Khilji attacked Chittorgarh to capture her, she chose jauhar (self-immolation) over dishonor. The women's sacrifice inspired warriors to fight with unprecedented bravery, and Chittorgarh's spirit of resistance became eternal.",
        "conclusion": "Honor preserved becomes inspiration for generations.",
        "places": ["Amber Fort, Jaipur - Magnificent hilltop fort with mirror palace",
                   "Mehrangarh Fort, Jodhpur - One of India's largest forts",
                   "Lake Palace, Udaipur - Floating marble palace on Lake Pichola"],
        "history": "Land of kings and desert kingdoms. Rajput warriors known for chivalry and honor. Rich tradition of miniature paintings, folk music, and colorful festivals. Major tourist destination."
    },
    "Tamil Nadu": {
        "tale": "The poet-saint Thiruvalluvar wrote 1330 couplets covering every aspect of life - love, virtue, wealth, and politics. A humble weaver by profession, his wisdom became timeless. His wife Vasuki once demonstrated virtue's power by floating a needle on water through her purity of character.",
        "conclusion": "True wisdom needs no royal throne.",
        "places": ["Meenakshi Temple, Madurai - Architectural marvel with 14 gopurams",
                   "Shore Temple, Mahabalipuram - UNESCO 8th century coastal temple",
                   "Brihadeeswarar Temple, Thanjavur - 1000-year-old temple with 66m tower"],
        "history": "Home to Tamil language, one of the oldest living languages. Ruled by Chola, Chera, and Pandya dynasties who built magnificent temples. Major center of Dravidian culture and classical arts."
    },
    "Uttar Pradesh": {
        "tale": "Emperor Shah Jahan's beloved wife Mumtaz died giving birth to their 14th child. Grief-stricken, he built her a monument so beautiful that heaven itself would envy it. For 22 years, 20,000 artisans created the Taj Mahal - proof that true love transcends even death.",
        "conclusion": "Love creates beauty that time cannot touch.",
        "places": ["Taj Mahal, Agra - UNESCO site, one of Seven Wonders",
                   "Varanasi Ghats - Oldest living city, spiritual capital of India",
                   "Fatehpur Sikri - Abandoned Mughal city, UNESCO site"],
        "history": "Most populous state. Birthplace of Lord Rama (Ayodhya) and Krishna (Mathura). Home to Mughal heritage in Agra. Buddhist pilgrimage site at Sarnath where Buddha gave first sermon."
    },
    "West Bengal": {
        "tale": "Rabindranath Tagore wrote songs for both India and Bangladesh's national anthems. When the British divided Bengal, his music united hearts across borders. He showed that art builds nations, not just maps. His vision of universal humanity still echoes in Shantiniketan.",
        "conclusion": "Art unites what politics divides.",
        "places": ["Victoria Memorial, Kolkata - Marble monument of British era",
                   "Sundarbans - UNESCO site, largest mangrove forest, Bengal tiger habitat",
                   "Darjeeling - Himalayan town famous for tea and toy train"],
        "history": "Colonial capital of British India until 1911. Bengali Renaissance center producing Nobel laureates, filmmakers, and revolutionaries. Witnessed partition and millions of refugees in 1947 and 1971."
    },
    "Telangana": {
        "tale": "In ancient Warangal, Queen Rudrama Devi ruled as king, wearing male attire and leading armies. When enemies mocked her gender, she defeated them in battle and proved that courage has no gender. She built a thousand-pillar temple where every pillar represented a woman warrior of her kingdom.",
        "conclusion": "Leadership is defined by courage, not gender.",
        "places": ["Charminar, Hyderabad - Iconic 16th century monument with four minarets",
                   "Golconda Fort - Medieval fortress famous for diamonds and acoustics",
                   "Ramoji Film City - World's largest film studio complex"],
        "history": "Separated from Andhra Pradesh in 2014, becoming India's youngest state. Home to the Kakatiya dynasty and later the Qutb Shahi kingdom. Hyderabad was ruled by Nizams known for wealth and pearls."
    },
    "Uttarakhand": {
        "tale": "A young girl praying in the Himalayas heard the Ganga river crying. The goddess said, 'I want to flow to the plains to purify the world, but the fall will destroy everything.' The girl meditated so deeply that Lord Shiva appeared and agreed to catch Ganga in his locks, releasing her gently to bless humanity.",
        "conclusion": "Great power requires gentle guidance.",
        "places": ["Kedarnath Temple - Sacred Shiva shrine at 11,755 feet",
                   "Valley of Flowers - UNESCO site with rare Himalayan flowers",
                   "Rishikesh - Yoga capital of the world, gateway to Himalayas"],
        "history": "Carved from Uttar Pradesh in 2000. Known as 'Land of Gods' (Devbhoomi) with four sacred Char Dham pilgrimage sites. Source of holy rivers Ganga and Yamuna. Rich in ancient Hindu pilgrimage traditions."
    },
    "Tripura": {
        "tale": "Long ago, the Fourteen Gods descended to protect Tripura from demons. A brave princess led the people in devotion, and the gods blessed the land with fourteen sacred groves. To this day, these groves protect the land's biodiversity, showing that faith and nature are intertwined.",
        "conclusion": "Sacred protection preserves natural heritage.",
        "places": ["Ujjayanta Palace - Royal palace with Mughal gardens",
                   "Neermahal - Water palace in middle of Rudrasagar Lake",
                   "Sepahijala Wildlife Sanctuary - Home to spectacled monkeys"],
        "history": "Ruled by Manikya dynasty for over 500 years until 1949. Rich tribal culture with unique bamboo handicrafts and handloom. Became full state in 1972 after being a Union Territory."
    },
    "Manipur": {
        "tale": "Princess Thoibi and commoner Khamba loved each other despite class barriers. When a divine polo game decided Khamba's fate, Thoibi's prayers gave him strength to win. Their love transformed Manipur's society, teaching that true nobility comes from character, not birth.",
        "conclusion": "Love recognizes character over class.",
        "places": ["Loktak Lake - Largest freshwater lake in Northeast with floating islands",
                   "Kangla Fort - Ancient seat of Manipur kingdom",
                   "Ima Keithel - Asia's largest all-women market run by 5000+ women"],
        "history": "Known as 'Jewel of India'. Ancient independent kingdom until 1949. Birthplace of modern polo. Rich tradition of Manipuri classical dance. Site of World War II battles against Japanese invasion."
    },
    "Meghalaya": {
        "tale": "The Khasi people tell of living root bridges grown by guiding tree roots across rivers. These bridges, created by ancestors centuries ago, grow stronger each year. They teach patience - what we plant today becomes the path for future generations.",
        "conclusion": "True legacy grows stronger with time.",
        "places": ["Cherrapunji - One of wettest places on Earth with living root bridges",
                   "Mawlynnong - Asia's cleanest village",
                   "Nohkalikai Falls - India's tallest plunge waterfall at 1100 feet"],
        "history": "Separated from Assam in 1972, name means 'Abode of Clouds'. Matrilineal society where property passes through women. Rich tribal culture with unique megalithic traditions and sacred groves."
    },
    "Mizoram": {
        "tale": "During a great famine, Chief Chawngbawla shared his last grain with starving villagers rather than save it for himself. The mountains, moved by his sacrifice, caused bamboo to flower and provide food. Mizos still celebrate this selfless spirit during Chapchar Kut festival.",
        "conclusion": "Leaders eat last, their people first.",
        "places": ["Phawngpui Peak - Blue Mountain, highest peak in Mizoram",
                   "Vantawng Falls - 13th highest waterfall in India",
                   "Reiek Tlang - Hilltop offering panoramic views and traditional Mizo villages"],
        "history": "Became full state in 1987. Predominantly Christian tribal population with strong oral traditions. Known for high literacy rate and community spirit. 'Tlawmngaihna' cultural code emphasizes selflessness."
    },
    "Nagaland": {
        "tale": "Naga warriors were known for headhunting, but when they heard a missionary's message of peace, the fiercest warrior laid down his spear and picked up a Bible. His transformation inspired the entire tribe to choose harmony over violence, reshaping Naga identity forever.",
        "conclusion": "The bravest warrior is one who chooses peace.",
        "places": ["Kohima War Cemetery - Memorial of World War II Battle of Kohima",
                   "Dzukou Valley - Valley of flowers on Nagaland-Manipur border",
                   "Hornbill Festival - Festival of festivals showcasing all tribes"],
        "history": "Became 16th state in 1963. Home to diverse Naga tribes, each with unique language and customs. Site of crucial WWII battle that stopped Japanese advance. Rich warrior culture transformed by Christianity."
    },
    "Sikkim": {
        "tale": "When Guru Padmasambhava blessed Sikkim, he hid sacred treasures throughout the land for future generations to discover when needed. A humble farmer once found a text teaching compassion during a crisis. Sikkim learned that the greatest treasures are wisdom, not gold.",
        "conclusion": "True treasures enlighten, not enrich.",
        "places": ["Tsomgo Lake - Glacial lake sacred to local people at 12,400 feet",
                   "Rumtek Monastery - Seat of Karmapa, important Buddhist center",
                   "Kanchenjunga - World's third highest peak, guardian deity of Sikkim"],
        "history": "Former Buddhist kingdom that joined India in 1975. India's least populous state. First organic state in the world. Rich Tibetan Buddhist heritage. Strategic location between Tibet, Nepal, and Bhutan."
    }
}


def print_slow(text, delay=0.02):
    """Print text with a typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_menu():
    """Display numbered menu of states alphabetically"""
    states = sorted(STATES_DATA.keys())
    print_slow("\n" + "="*70)
    print_slow("🇮🇳  INDIAN STATES FOLK TALES & TRAVEL GUIDE  🇮🇳")
    print_slow("="*70)
    print_slow("\nSelect states to explore (alphabetically ordered):\n")
    
    for i, state in enumerate(states, 1):
        print(f"  {i:2d}. {state}")
    
    print_slow("\n" + "="*70)
    return states

def explore_state_recursive(states_to_visit, all_states, visited=None, depth=0):
    """
    Recursively explore selected Indian states with folk tales and travel info.
    
    Args:
        states_to_visit: List of state names to visit
        all_states: Dictionary of all state data
        visited: Set of visited states
        depth: Recursion depth for visualization
    """
    if visited is None:
        visited = set()
    
    # Base case: no more states to visit
    if not states_to_visit:
        print_slow("\n" + "="*70)
        print_slow("✨ Journey Complete! ✨")
        print_slow(f"\nYou explored {len(visited)} state(s) through the magic of recursion!")
        print_slow("Each tale carries the wisdom of generations. Travel with curiosity! 🙏")
        print_slow("="*70 + "\n")
        return
    
    # Get current state
    current_state = states_to_visit[0]
    remaining_states = states_to_visit[1:]
    visited.add(current_state)
    
    # Visual elements
    indent = "  " * depth
    state_data = all_states[current_state]
    
    # Header
    print_slow("\n" + "="*70)
    print_slow(f"{indent}🚩 STATE #{len(visited)}: {current_state.upper()}")
    print_slow("="*70)
    time.sleep(0.3)
    
    # Historical Background
    print_slow(f"\n{indent}📜 HISTORICAL BACKGROUND:")
    print_slow(f"{indent}   {state_data['history']}")
    time.sleep(0.5)
    
    # Folk Tale
    print_slow(f"\n{indent}📖 FOLK TALE:")
    tale_lines = state_data['tale'].split('. ')
    for line in tale_lines:
        if line:
            print_slow(f"{indent}   {line.strip()}{'.' if not line.endswith('.') else ''}")
            time.sleep(0.3)
    
    # Moral/Conclusion
    print_slow(f"\n{indent}💡 MORAL OF THE TALE:")
    print_slow(f"{indent}   ✨ {state_data['conclusion']}")
    time.sleep(0.5)
    
    # Famous Places
    print_slow(f"\n{indent}🏛  FAMOUS PLACES TO VISIT:")
    for i, place in enumerate(state_data['places'], 1):
        print_slow(f"{indent}   {i}. {place}")
        time.sleep(0.2)
    
    # Recursion info
    print_slow(f"\n{indent}🔄 Recursion Depth: {depth + 1} | States Remaining: {len(remaining_states)}")
    time.sleep(0.8)
    
    # Recursive call
    if remaining_states:
        print_slow(f"\n{indent}➡  Traveling to next destination...")
        time.sleep(0.5)
    
    explore_state_recursive(remaining_states, all_states, visited, depth + 1)
    
    # Backtracking message
    print_slow(f"{indent}⬅  Returning from {current_state}... (Recursion unwinding)")

def main():
    """Main function to run the interactive folk tale explorer"""
    states_list = display_menu()
    
    while True:
        print_slow("\nEnter state numbers separated by spaces (e.g., '1 5 10')")
        print_slow("Or type 'all' to explore all states, 'random' for 5 random states:")
        choice = input("Your choice: ").strip().lower()
        
        if choice == 'all':
            selected_states = states_list
            break
        elif choice == 'random':
            selected_states = random.sample(states_list, min(5, len(states_list)))
            print_slow(f"\n🎲 Randomly selected: {', '.join(selected_states)}")
            time.sleep(1)
            break
        else:
            try:
                numbers = [int(x) for x in choice.split()]
                if all(1 <= n <= len(states_list) for n in numbers):
                    selected_states = [states_list[n-1] for n in numbers]
                    break
                else:
                    print_slow("❌ Please enter valid numbers from the menu!")
            except ValueError:
                print_slow("❌ Invalid input! Please enter numbers or 'all'/'random'.")
    
    # Start the recursive journey
    print_slow("\n🌟 Beginning your journey through India's heritage...")
    time.sleep(1)
    
    explore_state_recursive(selected_states, STATES_DATA)
    
    print_slow("🙏 Thank you for exploring India's rich cultural tapestry!")
    print_slow("   May these tales inspire your travels! Jai Hind! 🇮🇳\n")
main()