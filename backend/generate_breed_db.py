"""
Generate comprehensive breed database for all 122 dog breeds.
This creates reliable information for each breed with Wikimedia Commons URLs.
"""

# Comprehensive breed database with all 122 breeds
# Structure: breed_key -> {short_desc, traits, fun_fact, origin, size, temperament, health_notes, image_url}

BREED_DATABASE = {
    "afghan_hound": {
        "short_desc": "The Afghan Hound is an elegant, aristocratic dog breed known for its long, silky coat and distinctive appearance. Originally bred to hunt in the mountains of Afghanistan, these dogs are graceful and independent.",
        "traits": ["Dignified", "Independent", "Aloof", "Athletic"],
        "fun_fact": "Afghan Hounds have one of the longest coats in the dog world and require extensive grooming to maintain their beauty.",
        "origin": "Afghanistan, ancient times",
        "size": "25-27 inches, 45-60 lbs",
        "temperament": "Dignified, independent, aloof with strangers, loyal to family",
        "health_notes": "Prone to hip dysplasia, cataracts; sensitive to anesthesia; needs regular grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Afghan_Hound.jpg/1024px-Afghan_Hound.jpg"
    },
    "african_hunting_dog": {
        "short_desc": "African Hunting Dogs are highly social canines from Africa, known for their cooperative hunting behavior and unique mottled coat patterns. These endangered wild dogs are distinct from domestic dog breeds.",
        "traits": ["Social", "Cooperative", "Energetic", "Alert"],
        "fun_fact": "African Hunting Dogs have a success rate of about 80% on hunts - the highest of any large carnivore.",
        "origin": "Africa, sub-Saharan regions",
        "size": "24-30 inches, 44-66 lbs",
        "temperament": "Highly social, pack hunters, energetic, cooperative",
        "health_notes": "Wild animals; susceptible to diseases; endangered species",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/African_Hunting_Dog.jpg/1024px-African_Hunting_Dog.jpg"
    },
    "airedale": {
        "short_desc": "The Airedale Terrier is the largest terrier breed, known for their confidence and versatility. Originally bred in Yorkshire, England for hunting, they are intelligent and courageous dogs with a distinctive wiry coat.",
        "traits": ["Confident", "Intelligent", "Courageous", "Versatile"],
        "fun_fact": "Airedales were used as messengers, guard dogs, and police dogs, and have even served in military roles.",
        "origin": "Yorkshire, England, 19th century",
        "size": "23-24 inches, 50-70 lbs",
        "temperament": "Confident, intelligent, courageous, sometimes stubborn",
        "health_notes": "Generally hardy; prone to hip dysplasia, bloat; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Airedale_Terrier.jpg/1024px-Airedale_Terrier.jpg"
    },
    "american_staffordshire_terrier": {
        "short_desc": "The American Staffordshire Terrier is a muscular, powerful breed with a strong jaw and determined nature. Despite their intimidating appearance, they are affectionate and loyal family companions when properly socialized.",
        "traits": ["Confident", "Strong-Willed", "Affectionate", "Loyal"],
        "fun_fact": "American Staffordshire Terriers were historically used in dog fighting, but modern breeding focuses on temperament and family suitability.",
        "origin": "United States, 20th century",
        "size": "18-19 inches, 57-67 lbs",
        "temperament": "Confident, strong-willed, affectionate with family, needs socialization",
        "health_notes": "Prone to hip dysplasia, heart disease; requires firm training and socialization",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/American_Staffordshire_Terrier.jpg/1024px-American_Staffordshire_Terrier.jpg"
    },
    "appenzeller": {
        "short_desc": "The Appenzeller is a Swiss mountain dog breed known for their tricolor coat (black, red, white) and excellent working abilities. They are energetic herding dogs that require active families.",
        "traits": ["Alert", "Energetic", "Loyal", "Intelligent"],
        "fun_fact": "Appenzellers are named after the Appenzell region of Switzerland and have been used as herding and cattle dogs for centuries.",
        "origin": "Appenzell, Switzerland, 19th century",
        "size": "20-23 inches, 48-70 lbs",
        "temperament": "Alert, energetic, loyal, intelligent, needs mental stimulation",
        "health_notes": "Generally healthy; prone to hip dysplasia; needs substantial daily exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Appenzeller_Mountain_Dog.jpg/1024px-Appenzeller_Mountain_Dog.jpg"
    },
    "aspin": {
        "short_desc": "Aspin is a generic term for mixed-breed dogs commonly found in the Philippines. These street dogs are resourceful, resilient, and loyal when given a chance, making excellent family companions.",
        "traits": ["Resilient", "Loyal", "Intelligent", "Adaptable"],
        "fun_fact": "Aspins have become increasingly valued as pets and are now recognized for their excellent temperaments despite humble origins.",
        "origin": "Philippines, ancient mix",
        "size": "Variable, typically medium",
        "temperament": "Resilient, loyal, intelligent, adaptable to family life",
        "health_notes": "Generally hardy; mixed genetics; may carry street dog health issues",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Aspin_dog.jpg/1024px-Aspin_dog.jpg"
    },
    "australian_terrier": {
        "short_desc": "The Australian Terrier is a small but sturdy working dog breed from Australia. Known for their courage and alertness, they were originally bred to hunt small game and vermin on Australian farms.",
        "traits": ["Courageous", "Alert", "Spirited", "Loyal"],
        "fun_fact": "Australian Terriers are one of the smallest working terriers and were the first dog breed to be developed and shown in Australia.",
        "origin": "Australia, 19th century",
        "size": "10-11 inches, 12-18 lbs",
        "temperament": "Courageous, alert, spirited, loyal, sometimes stubborn",
        "health_notes": "Generally healthy; prone to patellar luxation, diabetes; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Australian_Terrier.jpg/1024px-Australian_Terrier.jpg"
    },
    "bedlington_terrier": {
        "short_desc": "The Bedlington Terrier is a unique terrier breed with a lamb-like appearance featuring a distinctive topknot. Originally bred in England for hunting, they are surprisingly athletic and determined hunters.",
        "traits": ["Gentle", "Athletic", "Intelligent", "Independent"],
        "fun_fact": "Bedlington Terriers have a distinctive appearance that resembles a lamb, complete with a topknot of hair on their head.",
        "origin": "Bedlington, England, 19th century",
        "size": "15-17 inches, 17-23 lbs",
        "temperament": "Gentle, athletic, intelligent, independent hunters",
        "health_notes": "Prone to copper toxicosis, progressive retinal atrophy; needs moderate exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Bedlington_Terrier.jpg/1024px-Bedlington_Terrier.jpg"
    },
    "bernese_mountain_dog": {
        "short_desc": "The Bernese Mountain Dog is a large, powerful Swiss working dog breed with a distinctive tricolor coat. Known for their loyalty and calm temperament, they excel as family companions and are excellent with children.",
        "traits": ["Loyal", "Calm", "Intelligent", "Strong"],
        "fun_fact": "Bernese Mountain Dogs were originally bred to herd cattle and pull carts in the Swiss Alps.",
        "origin": "Bern, Switzerland, ancient times",
        "size": "23-27 inches, 70-115 lbs",
        "temperament": "Loyal, calm, intelligent, strong bond with family, good with children",
        "health_notes": "Prone to hip dysplasia, degenerative myelopathy; shorter lifespan (7-10 years)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Bernese_Mountain_Dog.jpg/1024px-Bernese_Mountain_Dog.jpg"
    },
    "blenheim_spaniel": {
        "short_desc": "The Blenheim Spaniel is a small spaniel breed with a distinctive chestnut and white coat. Named after Blenheim Palace in England, they are affectionate lap dogs that combine elegance with playfulness.",
        "traits": ["Affectionate", "Playful", "Gentle", "Intelligent"],
        "fun_fact": "Blenheim Spaniels are named after Blenheim Palace where the breed was developed in the 1700s.",
        "origin": "Blenheim Palace, England, 18th century",
        "size": "12-13 inches, 13-16 lbs",
        "temperament": "Affectionate, playful, gentle, intelligent, loves companionship",
        "health_notes": "Prone to heart problems, ear infections; needs regular grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Blenheim_Spaniel.jpg/1024px-Blenheim_Spaniel.jpg"
    },
    "border_collie": {
        "short_desc": "The Border Collie is widely considered the most intelligent dog breed. These herding dogs possess incredible focus, energy, and trainability. They are exceptional working dogs and require extensive mental and physical stimulation.",
        "traits": ["Intelligent", "Energetic", "Focused", "Obedient"],
        "fun_fact": "Border Collies are so intelligent they can learn new commands in just 5 repetitions and remember them for life.",
        "origin": "England-Scotland border, 19th century",
        "size": "19-22 inches, 30-55 lbs",
        "temperament": "Extremely intelligent, energetic, intense focus, excellent herding instinct",
        "health_notes": "Generally healthy; prone to hip dysplasia; needs extensive daily exercise and mental stimulation",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Border_Collie_portrait.jpg/1024px-Border_Collie_portrait.jpg"
    },
    "border_terrier": {
        "short_desc": "The Border Terrier is a small, sturdy working terrier breed from the England-Scotland border. Known for their fearless nature and friendly temperament, they are excellent family companions despite their hunting heritage.",
        "traits": ["Fearless", "Friendly", "Sturdy", "Intelligent"],
        "fun_fact": "Border Terriers were bred to have long legs relative to their size, allowing them to keep pace with horses during fox hunts.",
        "origin": "England-Scotland border, 18th century",
        "size": "12-15 inches, 11-15 lbs",
        "temperament": "Fearless, friendly, sturdy, intelligent, good with family",
        "health_notes": "Generally healthy; prone to hip dysplasia, patellar luxation; needs moderate exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Border_Terrier.jpg/1024px-Border_Terrier.jpg"
    },
    "boston_bull": {
        "short_desc": "The Boston Bull is a rare crossbreed between Boston Terriers and Bulldogs, combining the friendly nature of both breeds. These compact dogs are affectionate and adaptable to various living situations.",
        "traits": ["Friendly", "Adaptable", "Affectionate", "Playful"],
        "fun_fact": "Boston Bulls represent the blend of two iconic dog breeds from different backgrounds.",
        "origin": "United States, modern crossbreed",
        "size": "12-17 inches, 25-50 lbs (varies)",
        "temperament": "Friendly, adaptable, affectionate, playful, good apartment dogs",
        "health_notes": "May inherit health issues from both parent breeds; needs moderate exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Boston_Terrier_puppy.jpg/1024px-Boston_Terrier_puppy.jpg"
    },
    "bouvier_des_flandres": {
        "short_desc": "The Bouvier des Flandres is a large, powerful Belgian working dog breed. Originally bred to herd cattle and pull carts, they are loyal, intelligent, and protective family companions.",
        "traits": ["Powerful", "Loyal", "Intelligent", "Protective"],
        "fun_fact": "Bouviers were used as messenger and ambulance dogs in World War I due to their strength and intelligence.",
        "origin": "Flanders, Belgium, 19th century",
        "size": "23-27 inches, 70-110 lbs",
        "temperament": "Powerful, loyal, intelligent, protective, calm but capable",
        "health_notes": "Prone to hip dysplasia, bloat; needs regular exercise and training",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Bouvier_des_Flandres.jpg/1024px-Bouvier_des_Flandres.jpg"
    },
    "brabancon_griffon": {
        "short_desc": "The Brabancon Griffon is a small Belgian toy dog breed with a distinctive flat face and often a beard-like muzzle. These charming dogs are affectionate, spirited, and excellent lap companions.",
        "traits": ["Affectionate", "Spirited", "Charming", "Alert"],
        "fun_fact": "Brabancon Griffons are known for their human-like expressions and often feature prominently in European art.",
        "origin": "Brussels, Belgium, 19th century",
        "size": "7-8 inches, 6-12 lbs",
        "temperament": "Affectionate, spirited, charming, alert, loves attention",
        "health_notes": "Brachycephalic breed; prone to breathing issues, eye problems; needs temperature control",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Griffon_Bruxellois_600.jpg/1024px-Griffon_Bruxellois_600.jpg"
    },
    "brittany_spaniel": {
        "short_desc": "The Brittany Spaniel is an energetic, athletic sporting dog breed known for their boundless enthusiasm and gentle nature. These birds dogs are excellent hunters and devoted family companions.",
        "traits": ["Energetic", "Athletic", "Gentle", "Eager"],
        "fun_fact": "Brittany Spaniels are sometimes called 'Brittanys' and are one of the smallest sporting dog breeds.",
        "origin": "Brittany, France, 19th century",
        "size": "17.5-20 inches, 30-40 lbs",
        "temperament": "Energetic, athletic, gentle, eager to please, sensitive",
        "health_notes": "Generally healthy; prone to hip dysplasia; needs substantial daily exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Brittany_Spaniel.jpg/1024px-Brittany_Spaniel.jpg"
    },
    "cardigan": {
        "short_desc": "The Cardigan Welsh Corgi is a sturdy, low-riding herding dog with a long body and short legs. Known for their fox-like appearance, they are intelligent, affectionate, and excel as family companions.",
        "traits": ["Intelligent", "Affectionate", "Sturdy", "Alert"],
        "fun_fact": "Cardigans have longer tails than Pembrokes and were often used to herd cattle by nipping at heels.",
        "origin": "Cardigan, Wales, ancient times",
        "size": "10.5-12.5 inches, 25-38 lbs",
        "temperament": "Intelligent, affectionate, sturdy, alert, good family dogs",
        "health_notes": "Prone to hip dysplasia, back problems; needs moderate exercise and weight management",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Cardigan_Welsh_Corgi.jpg/1024px-Cardigan_Welsh_Corgi.jpg"
    },
    "chesapeake_bay_retriever": {
        "short_desc": "The Chesapeake Bay Retriever is a powerful water retriever breed built for harsh conditions. Known for their oily, waterproof coat and strong work ethic, they are excellent hunters and loyal companions.",
        "traits": ["Powerful", "Athletic", "Loyal", "Determined"],
        "fun_fact": "Chesapeakes can break through ice with their strong builds and are exceptional at retrieving waterfowl in cold conditions.",
        "origin": "Chesapeake Bay, Maryland, 19th century",
        "size": "21-26 inches, 55-80 lbs",
        "temperament": "Powerful, athletic, loyal, determined, strong work ethic",
        "health_notes": "Prone to hip dysplasia, degenerative myelopathy; needs substantial exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Cheasapeake-Bay-Retriever.jpg/1024px-Cheasapeake-Bay-Retriever.jpg"
    },
    "chihuahua": {
        "short_desc": "The Chihuahua is the smallest dog breed in the world, yet possesses a surprisingly bold and confident personality. These toy dogs are devoted companions known for their loyalty and spirited nature.",
        "traits": ["Bold", "Confident", "Devoted", "Spirited"],
        "fun_fact": "Chihuahuas can be born so small they fit in a teaspoon and may weigh less than 2 pounds their entire lives.",
        "origin": "Mexico, ancient Aztec times",
        "size": "5-8 inches, 2-6 lbs",
        "temperament": "Bold, confident, devoted, spirited, alert despite small size",
        "health_notes": "Sensitive to cold and injury; prone to dental issues, patellar luxation; needs protection",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Chihuahua1.jpg/1024px-Chihuahua1.jpg"
    },
    "dandie_dinmont": {
        "short_desc": "The Dandie Dinmont Terrier is a small terrier breed with a distinctive silhouette and gentle temperament. These dogs are known for their independence and affectionate nature, making them excellent companions.",
        "traits": ["Independent", "Affectionate", "Determined", "Dignified"],
        "fun_fact": "The Dandie Dinmont was the first dog breed to be named after a fictional character from a novel.",
        "origin": "Scottish Borders, 18th century",
        "size": "8-11 inches, 18-24 lbs",
        "temperament": "Independent, affectionate, determined, dignified, sensitive",
        "health_notes": "Prone to intervertebral disc disease; needs gentle exercise and back support",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Dandie_Dinmont_Terrier.jpg/1024px-Dandie_Dinmont_Terrier.jpg"
    },
    "doberman": {
        "short_desc": "The Doberman Pinscher is a large, elegant working dog breed known for their intelligence, loyalty, and protective nature. These athletic dogs are devoted family companions and excellent guard dogs.",
        "traits": ["Intelligent", "Loyal", "Alert", "Powerful"],
        "fun_fact": "Dobermans were specifically bred in Germany in the 1890s to create the perfect protection dog.",
        "origin": "Germany, 19th century",
        "size": "24-28 inches, 60-88 lbs",
        "temperament": "Intelligent, loyal, alert, protective, devoted to family",
        "health_notes": "Prone to hip dysplasia, dilated cardiomyopathy; needs firm training and socialization",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Doberman_Pinscher_red.jpg/1024px-Doberman_Pinscher_red.jpg"
    },
    "english_foxhound": {
        "short_desc": "The English Foxhound is a large scent hound breed developed for fox hunting in England. Known for their stamina and excellent nose, they are pack hunters with friendly dispositions.",
        "traits": ["Athletic", "Friendly", "Determined", "Sociable"],
        "fun_fact": "English Foxhounds were bred for hundreds of years to have specific characteristics for fox hunting.",
        "origin": "England, 16th century",
        "size": "24-25 inches, 65-70 lbs",
        "temperament": "Athletic, friendly, determined, sociable, excellent pack hunters",
        "health_notes": "Generally healthy; prone to hip dysplasia; needs substantial exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/English_Foxhound.jpg/1024px-English_Foxhound.jpg"
    },
    "english_setter": {
        "short_desc": "The English Setter is an elegant sporting dog breed known for their beauty, athleticism, and gentle nature. These graceful hunters are excellent family companions with a friendly temperament.",
        "traits": ["Elegant", "Athletic", "Gentle", "Friendly"],
        "fun_fact": "English Setters get their name from their characteristic 'setting' behavior when pointing at game.",
        "origin": "England, 17th century",
        "size": "25-27 inches, 65-80 lbs",
        "temperament": "Elegant, athletic, gentle, friendly, sensitive to harsh correction",
        "health_notes": "Prone to hip dysplasia, deafness; needs moderate to substantial exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/English_Setter_standing.jpg/1024px-English_Setter_standing.jpg"
    },
    "english_springer": {
        "short_desc": "The English Springer Spaniel is a medium-sized sporting dog breed known for their enthusiasm and excellent retrieving abilities. These friendly dogs make wonderful family companions and hunting partners.",
        "traits": ["Enthusiastic", "Loyal", "Intelligent", "Athletic"],
        "fun_fact": "English Springers get their name from their 'springing' action when flushing game.",
        "origin": "England, 19th century",
        "size": "19-20 inches, 47-56 lbs",
        "temperament": "Enthusiastic, loyal, intelligent, athletic, eager to please",
        "health_notes": "Prone to hip dysplasia, ear infections; needs regular exercise and grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/English_Springer_Spaniel.jpg/1024px-English_Springer_Spaniel.jpg"
    },
    "entlebucher": {
        "short_desc": "The Entlebucher Mountain Dog is a small Swiss herding dog known for their loyalty and athletic abilities. These energetic dogs are excellent family companions that thrive in active households.",
        "traits": ["Loyal", "Athletic", "Alert", "Energetic"],
        "fun_fact": "Entlebucers are the smallest of the Swiss Mountain Dog breeds.",
        "origin": "Entlebuch, Switzerland, ancient times",
        "size": "16-21 inches, 55-66 lbs",
        "temperament": "Loyal, athletic, alert, energetic, good family dogs",
        "health_notes": "Generally healthy; prone to hip dysplasia; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Entlebucher_Mountain_Dog.jpg/1024px-Entlebucher_Mountain_Dog.jpg"
    },
    "eskimo_dog": {
        "short_desc": "The Eskimo Dog, also known as the Inuit Dog, is a hardy arctic working dog breed. Known for their strength, endurance, and thick double coat, these powerful dogs were bred to haul sleds across frozen terrain.",
        "traits": ["Strong", "Enduring", "Alert", "Loyal"],
        "fun_fact": "Eskimo Dogs can withstand extreme cold and were essential for Arctic exploration and transportation.",
        "origin": "Arctic regions (Inuit peoples)",
        "size": "20-27 inches, 50-105 lbs",
        "temperament": "Strong, enduring, alert, loyal, pack dogs",
        "health_notes": "Prone to hip dysplasia; needs substantial exercise; coat sheds heavily",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Inuit_Sled_Dogs.jpg/1024px-Inuit_Sled_Dogs.jpg"
    },
    "french_bulldog": {
        "short_desc": "The French Bulldog is a small, muscular dog breed with distinctive bat-like ears and charming personality. Despite their small size, they are sturdy, adaptable companions perfect for apartment living.",
        "traits": ["Playful", "Affectionate", "Adaptable", "Charming"],
        "fun_fact": "French Bulldogs cannot swim well and can overheat easily due to their short muzzles.",
        "origin": "France, 19th century (based on English Bulldog)",
        "size": "11-13 inches, 28 lbs",
        "temperament": "Playful, affectionate, adaptable, charming, minimal exercise needs",
        "health_notes": "Brachycephalic breed; prone to breathing issues, spine problems; sensitive to heat",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Frenchie_Isabella.JPG/1024px-Frenchie_Isabella.JPG"
    },
    "german_shepherd": {
        "short_desc": "The German Shepherd is one of the most versatile and intelligent dog breeds. Known for their loyalty, confidence, and remarkable trainability, they excel in police, military, and search-and-rescue work.",
        "traits": ["Intelligent", "Loyal", "Confident", "Versatile"],
        "fun_fact": "German Shepherds are the second most popular dog breed in the USA and are used extensively in law enforcement.",
        "origin": "Germany, 1899",
        "size": "22-26 inches, 50-90 lbs",
        "temperament": "Intelligent, loyal, confident, versatile, eager to work",
        "health_notes": "Prone to hip/elbow dysplasia, degenerative myelopathy; needs mental and physical stimulation",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/German_Shepherd_-_DSC_4797.JPG/1024px-German_Shepherd_-_DSC_4797.JPG"
    },
    "german_short_haired_pointer": {
        "short_desc": "The German Shorthaired Pointer is an athletic sporting dog breed known for their versatility and excellent hunting abilities. These energetic dogs are loyal companions that thrive in active families.",
        "traits": ["Athletic", "Energetic", "Intelligent", "Loyal"],
        "fun_fact": "German Shorthaired Pointers were developed to hunt on both land and water, making them true versatile hunters.",
        "origin": "Germany, 19th century",
        "size": "23-25 inches, 55-70 lbs",
        "temperament": "Athletic, energetic, intelligent, loyal, needs substantial daily activity",
        "health_notes": "Prone to hip dysplasia, bloat; needs consistent exercise and mental stimulation",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/German_Shorthaired_Pointer.jpg/1024px-German_Shorthaired_Pointer.jpg"
    },
    "gordon_setter": {
        "short_desc": "The Gordon Setter is a large, elegant sporting dog breed with a distinctive black and tan coat. Known for their intelligence, athleticism, and loyal nature, they are excellent hunters and devoted family companions.",
        "traits": ["Intelligent", "Athletic", "Loyal", "Elegant"],
        "fun_fact": "Gordon Setters are the heaviest of the setter breeds and are often called 'Black Beauties' by enthusiasts.",
        "origin": "Scotland, 18th century",
        "size": "23-27 inches, 55-80 lbs",
        "temperament": "Intelligent, athletic, loyal, elegant, eager to please",
        "health_notes": "Prone to hip dysplasia, bloat; needs regular exercise and mental stimulation",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Gordon_Setter.jpg/1024px-Gordon_Setter.jpg"
    },
    "great_dane": {
        "short_desc": "The Great Dane is one of the largest dog breeds, known for their gentle giant nature and surprising grace. Despite their impressive size, they are affectionate, loyal, and excellent family companions.",
        "traits": ["Gentle", "Loyal", "Affectionate", "Dignified"],
        "fun_fact": "Great Danes were originally bred in Germany to hunt wild boar and pull heavy carts.",
        "origin": "Germany, ancient times (modern development 19th century)",
        "size": "28-34 inches, 110-175 lbs",
        "temperament": "Gentle, loyal, affectionate, dignified, good family dogs despite size",
        "health_notes": "Prone to hip dysplasia, bloat, heart problems; shorter lifespan (7-10 years)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Great_Dane_blue.jpg/1024px-Great_Dane_blue.jpg"
    },
    "great_pyrenees": {
        "short_desc": "The Great Pyrenees is a large, powerful livestock guardian dog breed with a beautiful white coat. Known for their independence, loyalty, and protective instincts, they were bred to guard sheep in the Pyrenees Mountains.",
        "traits": ["Independent", "Loyal", "Protective", "Intelligent"],
        "fun_fact": "Great Pyrenees are so devoted to their flocks that they would stay with them through harsh mountain conditions.",
        "origin": "Pyrenees Mountains (France/Spain), ancient times",
        "size": "25-32 inches, 100-160 lbs",
        "temperament": "Independent, loyal, protective, intelligent, strong guardian instinct",
        "health_notes": "Prone to hip dysplasia, bloat; needs firm training; may roam if not secured",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Great_Pyrenees.jpg/1024px-Great_Pyrenees.jpg"
    },
    "greater_swiss_mountain_dog": {
        "short_desc": "The Greater Swiss Mountain Dog is a large, powerful working dog breed from Switzerland. Known for their strength, intelligence, and friendly disposition, they are excellent family companions and working dogs.",
        "traits": ["Strong", "Intelligent", "Friendly", "Loyal"],
        "fun_fact": "Greater Swiss Mountain Dogs were used to pull carts and herd cattle in Swiss alpine villages.",
        "origin": "Switzerland, ancient times",
        "size": "25-28 inches, 110-180 lbs",
        "temperament": "Strong, intelligent, friendly, loyal, eager to work",
        "health_notes": "Prone to hip dysplasia, bloat; needs regular exercise; relatively short lifespan",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Greater_Swiss_Mountain_Dog.jpg/1024px-Greater_Swiss_Mountain_Dog.jpg"
    },
    "ibizan_hound": {
        "short_desc": "The Ibizan Hound is an elegant, athletic sighthound breed from the island of Ibiza. Known for their graceful build, incredible jumping ability, and independent nature, they are exceptional hunters and loyal companions.",
        "traits": ["Elegant", "Athletic", "Independent", "Alert"],
        "fun_fact": "Ibizan Hounds can jump extremely high - up to 5 feet vertically - making them excellent hunters.",
        "origin": "Ibiza (Balearic Islands), Spain, ancient times",
        "size": "22-29 inches, 42-50 lbs",
        "temperament": "Elegant, athletic, independent, alert, excellent jumpers",
        "health_notes": "Generally healthy; prone to seizures; needs secure fencing for safety",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Ibizan_Hound.jpg/1024px-Ibizan_Hound.jpg"
    },
    "irish_setter": {
        "short_desc": "The Irish Setter is a large, athletic sporting dog breed known for their beautiful red coat and boundless enthusiasm. These friendly, affectionate dogs are excellent companions and exceptional hunters.",
        "traits": ["Enthusiastic", "Friendly", "Affectionate", "Athletic"],
        "fun_fact": "Irish Setters are known for their love of people and are often considered too friendly to be good guard dogs.",
        "origin": "Ireland, 18th century",
        "size": "25-27 inches, 60-70 lbs",
        "temperament": "Enthusiastic, friendly, affectionate, athletic, eager to please",
        "health_notes": "Prone to hip dysplasia, progressive retinal atrophy; needs substantial daily exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Red_Irish_Setter.jpg/1024px-Red_Irish_Setter.jpg"
    },
    "irish_terrier": {
        "short_desc": "The Irish Terrier is a medium-sized, spirited terrier breed with a distinctive red coat. Known for their courage, loyalty, and independence, these dogs are feisty yet affectionate companions.",
        "traits": ["Spirited", "Courageous", "Loyal", "Independent"],
        "fun_fact": "Irish Terriers are sometimes called 'Daredevils' due to their fearless and bold nature.",
        "origin": "Ireland, 19th century",
        "size": "18 inches, 25-27 lbs",
        "temperament": "Spirited, courageous, loyal, independent, sometimes stubborn",
        "health_notes": "Generally healthy; prone to hip dysplasia, hypothyroidism; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Irish_Terrier.jpg/1024px-Irish_Terrier.jpg"
    },
    "irish_water_spaniel": {
        "short_desc": "The Irish Water Spaniel is a large, athletic retriever breed known for their distinctive curly coat and love of water. These intelligent, spirited dogs are excellent swimmers and devoted companions.",
        "traits": ["Athletic", "Intelligent", "Spirited", "Water-Loving"],
        "fun_fact": "Irish Water Spaniels are the largest of all spaniel breeds and excel at water retrieval.",
        "origin": "Ireland, 19th century",
        "size": "22-24 inches, 55-68 lbs",
        "temperament": "Athletic, intelligent, spirited, loves water, excellent swimmers",
        "health_notes": "Prone to hip dysplasia, ear infections; needs regular exercise and grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Irish_Water_Spaniel.jpg/1024px-Irish_Water_Spaniel.jpg"
    },
    "irish_wolfhound": {
        "short_desc": "The Irish Wolfhound is one of the tallest dog breeds, known for their impressive size, gentle nature, and dignified bearing. Despite their imposing stature, they are affectionate, loyal family companions.",
        "traits": ["Gentle", "Loyal", "Dignified", "Calm"],
        "fun_fact": "Irish Wolfhounds were historically used to hunt wolves and elk in Ireland.",
        "origin": "Ireland, ancient times",
        "size": "30-32 inches, 140-180 lbs",
        "temperament": "Gentle, loyal, dignified, calm, good family dogs despite massive size",
        "health_notes": "Prone to hip dysplasia, bloat, heart problems; shorter lifespan (6-8 years)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Irish_Wolfhound.jpg/1024px-Irish_Wolfhound.jpg"
    },
    "italian_greyhound": {
        "short_desc": "The Italian Greyhound is a miniature sighthound breed known for their delicate build, grace, and affectionate nature. These toy dogs are sensitive, intelligent, and devoted lap companions.",
        "traits": ["Delicate", "Affectionate", "Intelligent", "Sensitive"],
        "fun_fact": "Italian Greyhounds were favored by Italian Renaissance aristocracy and remain symbols of elegance.",
        "origin": "Italy, ancient times (modern development 15th century)",
        "size": "13-18 inches, 3-10 lbs",
        "temperament": "Delicate, affectionate, intelligent, sensitive, devoted to family",
        "health_notes": "Fragile; prone to patellar luxation, dental issues; needs protection from injuries",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Italian_Greyhound.jpg/1024px-Italian_Greyhound.jpg"
    },
    "japanese_spaniel": {
        "short_desc": "The Japanese Spaniel is a small toy dog breed with a distinctive Japanese heritage. Known for their elegant appearance, cat-like temperament, and affectionate nature, they are charming lap companions.",
        "traits": ["Elegant", "Affectionate", "Independent", "Charming"],
        "fun_fact": "Japanese Spaniels have a cat-like temperament and often groom themselves like cats.",
        "origin": "Japan, ancient times",
        "size": "8-11 inches, 7-11 lbs",
        "temperament": "Elegant, affectionate, independent, charming, cat-like demeanor",
        "health_notes": "Prone to eye problems, respiratory issues; needs gentle handling and grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Japanese_Spaniel.jpg/1024px-Japanese_Spaniel.jpg"
    },
    "kerry_blue_terrier": {
        "short_desc": "The Kerry Blue Terrier is a medium-sized terrier breed with a distinctive blue-gray coat. Known for their spirit, athleticism, and loyalty, these dogs are versatile working dogs and devoted companions.",
        "traits": ["Spirited", "Athletic", "Loyal", "Versatile"],
        "fun_fact": "Kerry Blue Terriers were used for hunting, herding, and guarding in their native Ireland.",
        "origin": "County Kerry, Ireland, 19th century",
        "size": "18-19.5 inches, 33-40 lbs",
        "temperament": "Spirited, athletic, loyal, versatile, sometimes stubborn",
        "health_notes": "Prone to hip dysplasia, eye problems; needs firm training and regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Kerry_Blue_Terrier.jpg/1024px-Kerry_Blue_Terrier.jpg"
    },
    "labrador_retriever": {
        "short_desc": "The Labrador Retriever is one of the most popular dog breeds, known for their friendly nature, intelligence, and exceptional trainability. These versatile dogs excel as family companions, service dogs, and hunting partners.",
        "traits": ["Friendly", "Intelligent", "Loyal", "Outgoing"],
        "fun_fact": "Labradors have water-resistant coats and webbed toes, making them excellent swimmers.",
        "origin": "Canada (Newfoundland), 19th century",
        "size": "21-24 inches, 55-80 lbs",
        "temperament": "Friendly, intelligent, loyal, outgoing, eager to please",
        "health_notes": "Prone to hip dysplasia, obesity, bloat; needs regular exercise and proper diet",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Labrador_on_Quantock.jpg/1024px-Labrador_on_Quantock.jpg"
    },
    "lakeland_terrier": {
        "short_desc": "The Lakeland Terrier is a small, sturdy terrier breed from the Lake District in England. Known for their bold spirit, intelligence, and friendly nature, they are excellent family companions and working dogs.",
        "traits": ["Bold", "Intelligent", "Friendly", "Sturdy"],
        "fun_fact": "Lakeland Terriers were bred to hunt foxes that preyed on lambs in the English Lake District.",
        "origin": "Lake District, England, 19th century",
        "size": "13-14 inches, 15-17 lbs",
        "temperament": "Bold, intelligent, friendly, sturdy, sometimes stubborn",
        "health_notes": "Generally healthy; prone to hip dysplasia, lens luxation; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Lakeland_Terrier.jpg/1024px-Lakeland_Terrier.jpg"
    },
    "leonberg": {
        "short_desc": "The Leonberger is a large, powerful German working dog breed known for their lion-like mane and muscular build. These gentle giants are intelligent, loyal, and excellent water rescue dogs.",
        "traits": ["Powerful", "Intelligent", "Loyal", "Gentle"],
        "fun_fact": "Leonbergers were originally bred from St. Bernards, Newfoundlands, and Great Pyrenees.",
        "origin": "Leonberg, Germany, 19th century",
        "size": "25-31 inches, 100-170 lbs",
        "temperament": "Powerful, intelligent, loyal, gentle despite massive size, good swimmers",
        "health_notes": "Prone to hip dysplasia, bloat, heart problems; needs ample space and exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Leonberger.jpg/1024px-Leonberger.jpg"
    },
    "lhasa": {
        "short_desc": "The Lhasa Apso is a small, ancient Tibetan dog breed known for their long, luxurious coat and independent spirit. These alert, intelligent dogs were originally bred as temple guardians in Tibet.",
        "traits": ["Independent", "Alert", "Intelligent", "Confident"],
        "fun_fact": "Lhasa Apsos were considered sacred by Tibetan Buddhist monks and were rarely given away.",
        "origin": "Lhasa, Tibet, ancient times",
        "size": "10-11 inches, 12-18 lbs",
        "temperament": "Independent, alert, intelligent, confident, sometimes aloof with strangers",
        "health_notes": "Prone to hip dysplasia, eye problems; needs regular grooming and exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Lhasa_Apso.jpg/1024px-Lhasa_Apso.jpg"
    },
    "maltese_dog": {
        "short_desc": "The Maltese is a small toy dog breed with a silky white coat and gentle temperament. These affectionate, intelligent dogs are devoted lap companions that thrive on human companionship.",
        "traits": ["Affectionate", "Gentle", "Intelligent", "Devoted"],
        "fun_fact": "Maltese dogs have been favorites of nobility and aristocracy for thousands of years.",
        "origin": "Malta, Mediterranean, ancient times",
        "size": "7-9 inches, 4-7 lbs",
        "temperament": "Affectionate, gentle, intelligent, devoted, loves companionship",
        "health_notes": "Prone to eye problems, patellar luxation, hypothyroidism; needs gentle handling",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Maltese_dog_resting.jpg/1024px-Maltese_dog_resting.jpg"
    },
    "mexican_hairless": {
        "short_desc": "The Mexican Hairless dog (Xoloitzcuintli) is an ancient, hairless breed known for their unique appearance and warm body temperature. These intelligent, loyal dogs are devoted companions with a rich Mesoamerican heritage.",
        "traits": ["Intelligent", "Loyal", "Alert", "Graceful"],
        "fun_fact": "Aztecs considered Mexican Hairless dogs sacred and believed they had healing properties.",
        "origin": "Mexico, ancient Mesoamerican times",
        "size": "10-14 inches (Standard), 9-14 lbs",
        "temperament": "Intelligent, loyal, alert, graceful, devoted to family",
        "health_notes": "Hairless dogs need sun protection and moisturizing; prone to dental issues",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Xoloitzcuintli.jpg/1024px-Xoloitzcuintli.jpg"
    },
    "newfoundland": {
        "short_desc": "The Newfoundland is a large, powerful water dog breed known for their swimming ability, strength, and gentle nature. These intelligent, loyal dogs are excellent water rescue dogs and devoted family companions.",
        "traits": ["Powerful", "Intelligent", "Loyal", "Gentle"],
        "fun_fact": "Newfoundlands have a water-resistant coat and webbed feet, making them exceptional swimmers and rescue dogs.",
        "origin": "Newfoundland, Canada, ancient times",
        "size": "26-28 inches, 100-150 lbs",
        "temperament": "Powerful, intelligent, loyal, gentle, excellent swimmers",
        "health_notes": "Prone to hip dysplasia, bloat, heart problems; needs water access and grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Newfoundland_dog.jpg/1024px-Newfoundland_dog.jpg"
    },
    "norfolk_terrier": {
        "short_desc": "The Norfolk Terrier is a small, sturdy terrier breed with a warm, friendly temperament. Originally bred to hunt rats, they are excellent family companions with bold spirits and affectionate natures.",
        "traits": ["Friendly", "Bold", "Affectionate", "Sturdy"],
        "fun_fact": "Norfolk Terriers are among the smallest working terrier breeds and remain excellent hunters.",
        "origin": "Norfolk, England, 19th century",
        "size": "10 inches, 11-12 lbs",
        "temperament": "Friendly, bold, affectionate, sturdy, good family dogs",
        "health_notes": "Generally healthy; prone to hip dysplasia, patellar luxation; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Norfolk_Terrier.jpg/1024px-Norfolk_Terrier.jpg"
    },
    "norwegian_elkhound": {
        "short_desc": "The Norwegian Elkhound is a Nordic hunting dog breed known for their spitz-type appearance, hardiness, and hunting instinct. These bold, independent dogs are excellent companions for active families.",
        "traits": ["Bold", "Independent", "Intelligent", "Hardy"],
        "fun_fact": "Norwegian Elkhounds were bred to hunt large game like elk and moose in harsh Scandinavian terrain.",
        "origin": "Norway, ancient times",
        "size": "19-20 inches, 48-55 lbs",
        "temperament": "Bold, independent, intelligent, hardy, strong hunting drive",
        "health_notes": "Prone to hip dysplasia, bloat; needs substantial exercise; sheds heavily",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Norwegian_Elkhound.jpg/1024px-Norwegian_Elkhound.jpg"
    },
    "norwich_terrier": {
        "short_desc": "The Norwich Terrier is a small, sturdy terrier breed known for their fox-like appearance, independence, and loyal nature. These brave little dogs are excellent family companions with big personalities.",
        "traits": ["Brave", "Independent", "Loyal", "Alert"],
        "fun_fact": "Norwich Terriers are similar to Norfolk Terriers but with pointed, erect ears instead of droopy ears.",
        "origin": "Norwich, England, 19th century",
        "size": "10 inches, 12 lbs",
        "temperament": "Brave, independent, loyal, alert, sometimes stubborn",
        "health_notes": "Generally healthy; prone to hip dysplasia, patellar luxation; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Norwich_Terrier.jpg/1024px-Norwich_Terrier.jpg"
    },
    "old_english_sheepdog": {
        "short_desc": "The Old English Sheepdog is a large, powerful herding dog breed known for their shaggy coat and playful personality. These intelligent, gentle dogs are excellent family companions despite their working heritage.",
        "traits": ["Playful", "Intelligent", "Gentle", "Loyal"],
        "fun_fact": "Old English Sheepdogs have hair covering their eyes, yet they navigate obstacles without difficulty.",
        "origin": "England, 19th century",
        "size": "21-22 inches, 60-100 lbs",
        "temperament": "Playful, intelligent, gentle, loyal, excellent with children",
        "health_notes": "Prone to hip dysplasia, bloat, eye problems; needs extensive grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Old_English_Sheepdog.jpg/1024px-Old_English_Sheepdog.jpg"
    },
    "pekinese": {
        "short_desc": "The Pekingese is a small Asian toy dog breed with a distinctive lion-like appearance and independent spirit. These affectionate dogs were originally bred for Chinese royalty and remain symbols of elegance.",
        "traits": ["Independent", "Affectionate", "Dignified", "Alert"],
        "fun_fact": "Pekingese were bred in ancient China and were given only to the imperial court and nobility.",
        "origin": "Beijing, China, ancient times",
        "size": "6-9 inches, 7-14 lbs",
        "temperament": "Independent, affectionate, dignified, alert, sometimes stubborn",
        "health_notes": "Brachycephalic breed; prone to breathing problems, eye issues; needs heat protection",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Pekingese.jpg/1024px-Pekingese.jpg"
    },
    "pembroke": {
        "short_desc": "The Pembroke Welsh Corgi is a small, sturdy herding dog breed known for their fox-like appearance and short legs. These intelligent, affectionate dogs are excellent family companions with big personalities.",
        "traits": ["Intelligent", "Affectionate", "Sturdy", "Alert"],
        "fun_fact": "Pembroke Welsh Corgis are favored by British royalty and were the preferred breed of Queen Elizabeth II.",
        "origin": "Pembrokeshire, Wales, ancient times",
        "size": "10-12 inches, 24-30 lbs",
        "temperament": "Intelligent, affectionate, sturdy, alert, excellent family dogs",
        "health_notes": "Prone to hip dysplasia, back problems; needs weight management and moderate exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Pembroke_Welsh_Corgi.jpg/1024px-Pembroke_Welsh_Corgi.jpg"
    },
    "philippine_forest_dog": {
        "short_desc": "The Philippine Forest Dog is a rare, indigenous breed from the Philippines known for their agility and hunting abilities. These athletic dogs are adapted to tropical forest environments and remain relatively uncommon.",
        "traits": ["Agile", "Athletic", "Intelligent", "Independent"],
        "fun_fact": "Philippine Forest Dogs are one of the few indigenous dog breeds native to Southeast Asia.",
        "origin": "Philippines, ancient times",
        "size": "16-20 inches, 16-30 lbs",
        "temperament": "Agile, athletic, intelligent, independent, good hunters",
        "health_notes": "Generally hardy; adapted to tropical climates; needs protection from extreme cold",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Philippine_Forest_Dog.jpg/1024px-Philippine_Forest_Dog.jpg"
    },
    "pomeranian": {
        "short_desc": "The Pomeranian is a small toy spitz-type breed known for their fluffy coat and bold personality. Despite their tiny size, these intelligent dogs are confident and devoted companions with surprising attitudes.",
        "traits": ["Bold", "Intelligent", "Devoted", "Spirited"],
        "fun_fact": "Pomeranians were bred down from larger Spitz breeds and were favorites of European royalty.",
        "origin": "Pomerania (Germany/Poland), 19th century",
        "size": "6-7 inches, 3-7 lbs",
        "temperament": "Bold, intelligent, devoted, spirited, big personality in tiny package",
        "health_notes": "Prone to patellar luxation, dental issues, heart problems; sensitive to heat and cold",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Pomeranian.jpg/1024px-Pomeranian.jpg"
    },
    "rhodesian_ridgeback": {
        "short_desc": "The Rhodesian Ridgeback is a large, powerful African hunting dog breed known for their distinctive back ridge and independent spirit. These athletic, dignified dogs are loyal companions and excellent hunters.",
        "traits": ["Powerful", "Independent", "Loyal", "Dignified"],
        "fun_fact": "Rhodesian Ridgebacks have a distinctive ridge of hair growing opposite the direction of the rest of their coat.",
        "origin": "Zimbabwe (Rhodesia), 19th century",
        "size": "24-27 inches, 70-85 lbs",
        "temperament": "Powerful, independent, loyal, dignified, strong prey drive",
        "health_notes": "Prone to hip dysplasia, bloat; needs firm training and socialization",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Rhodesian_Ridgeback.jpg/1024px-Rhodesian_Ridgeback.jpg"
    },
    "rottweiler": {
        "short_desc": "The Rottweiler is a large, powerful working dog breed known for their confidence and protective instincts. When properly trained and socialized, these intelligent dogs are loyal family companions and exceptional workers.",
        "traits": ["Confident", "Intelligent", "Loyal", "Protective"],
        "fun_fact": "Rottweilers were originally bred by Roman soldiers to guard livestock.",
        "origin": "Rottweil, Germany, ancient (Roman) times",
        "size": "22-27 inches, 80-135 lbs",
        "temperament": "Confident, intelligent, loyal, protective, good family dogs with proper training",
        "health_notes": "Prone to hip dysplasia, bloat, heart problems; needs firm training and socialization",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Rottweiler_standing.jpg/1024px-Rottweiler_standing.jpg"
    },
    "saint_bernard": {
        "short_desc": "The Saint Bernard is a large Swiss working dog breed known for their impressive size, strength, and gentle nature. These powerful dogs were originally bred for alpine rescue and remain devoted family companions.",
        "traits": ["Gentle", "Powerful", "Intelligent", "Loyal"],
        "fun_fact": "Saint Bernards can weigh up to 200 lbs and have been used for over 300 years in mountain rescue.",
        "origin": "Swiss Alps, 17th century",
        "size": "26-35 inches, 120-200 lbs",
        "temperament": "Gentle, powerful, intelligent, loyal, good with children despite massive size",
        "health_notes": "Prone to hip dysplasia, bloat, heart problems; needs cool environment; shorter lifespan",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Saint_Bernard.jpg/1024px-Saint_Bernard.jpg"
    },
    "saluki": {
        "short_desc": "The Saluki is an ancient sighthound breed known for their graceful build, incredible speed, and independent nature. These elegant dogs were historically bred to hunt gazelle in Middle Eastern deserts.",
        "traits": ["Graceful", "Independent", "Alert", "Aristocratic"],
        "fun_fact": "Salukis are one of the oldest dog breeds, with evidence of their existence dating back to ancient Egypt.",
        "origin": "Middle East (Egypt, Arabia), ancient times",
        "size": "23-28 inches, 40-60 lbs",
        "temperament": "Graceful, independent, alert, aristocratic, aloof with strangers",
        "health_notes": "Generally healthy; prone to hip dysplasia, heart problems; needs secure fencing",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Saluki.jpg/1024px-Saluki.jpg"
    },
    "samoyed": {
        "short_desc": "The Samoyed is a large spitz-type working dog breed known for their beautiful white coat and friendly smile. Originally bred to herd reindeer and haul sleds in Siberia, they are excellent family companions.",
        "traits": ["Friendly", "Intelligent", "Loyal", "Athletic"],
        "fun_fact": "Samoyeds are known for their 'Samoyede smile' - a gentle expression that looks like they're smiling.",
        "origin": "Siberia (Samoyede people), ancient times",
        "size": "19-23 inches, 45-65 lbs",
        "temperament": "Friendly, intelligent, loyal, athletic, excellent with family",
        "health_notes": "Prone to hip dysplasia, bloat; sheds heavily; needs cool environment and exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Samoyed_dog.jpg/1024px-Samoyed_dog.jpg"
    },
    "scotch_terrier": {
        "short_desc": "The Scottish Terrier is a small, sturdy terrier breed with a distinctive appearance and bold temperament. Known for their independence and fierce loyalty, these dogs are excellent family companions.",
        "traits": ["Bold", "Independent", "Loyal", "Stubborn"],
        "fun_fact": "Scottish Terriers have a distinctive silhouette with a large head and short legs relative to body size.",
        "origin": "Scotland, 19th century",
        "size": "10-11 inches, 20-25 lbs",
        "temperament": "Bold, independent, loyal, stubborn, fierce protectors",
        "health_notes": "Prone to hip dysplasia, cancer, craniomandibular osteopathy; needs firm training",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Scottish_Terrier.jpg/1024px-Scottish_Terrier.jpg"
    },
    "scottish_deerhound": {
        "short_desc": "The Scottish Deerhound is a large sighthound breed with a wiry coat and aristocratic bearing. Originally bred to hunt Scottish red deer, they are gentle, dignified companions with impressive athleticism.",
        "traits": ["Gentle", "Aristocratic", "Athletic", "Dignified"],
        "fun_fact": "Scottish Deerhounds can run at speeds up to 30 mph and have historically hunted large game.",
        "origin": "Scotland, ancient times",
        "size": "28-32 inches, 75-110 lbs",
        "temperament": "Gentle, aristocratic, athletic, dignified, loves running",
        "health_notes": "Prone to heart problems, cancer; needs substantial exercise; relatively short lifespan",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Scottish_Deerhound.jpg/1024px-Scottish_Deerhound.jpg"
    },
    "sealyham_terrier": {
        "short_desc": "The Sealyham Terrier is a small Welsh terrier breed with a distinctive white coat and sturdy build. These brave little dogs are excellent hunters and loyal family companions.",
        "traits": ["Brave", "Sturdy", "Loyal", "Friendly"],
        "fun_fact": "Sealyham Terriers were bred in Wales specifically to hunt badgers, foxes, and otters.",
        "origin": "Sealyham, Wales, 19th century",
        "size": "10.5-11 inches, 24 lbs",
        "temperament": "Brave, sturdy, loyal, friendly, good family dogs",
        "health_notes": "Generally healthy; prone to hip dysplasia, lens luxation; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Sealyham_Terrier.jpg/1024px-Sealyham_Terrier.jpg"
    },
    "shetland_sheepdog": {
        "short_desc": "The Shetland Sheepdog is a small herding dog breed with a distinctive appearance resembling a miniature Rough Collie. Known for their intelligence, loyalty, and eagerness to please, they excel as family companions.",
        "traits": ["Intelligent", "Loyal", "Sensitive", "Eager"],
        "fun_fact": "Shetland Sheepdogs were developed in the Shetland Islands and used to herd small sheep.",
        "origin": "Shetland Islands, Scotland, 19th century",
        "size": "15-16 inches, 15-25 lbs",
        "temperament": "Intelligent, loyal, sensitive, eager to please, good family dogs",
        "health_notes": "Prone to hip dysplasia, eye problems; sensitive to harsh correction; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Shetland_Sheepdog.jpg/1024px-Shetland_Sheepdog.jpg"
    },
    "shih_tzu": {
        "short_desc": "The Shih Tzu is a small Asian toy dog breed known for their luxurious long coat and affectionate personality. Originally bred for Chinese emperors, these dogs are devoted lap companions that thrive on human interaction.",
        "traits": ["Affectionate", "Playful", "Confident", "Independent"],
        "fun_fact": "Shih Tzus were bred exclusively in China and were not seen in the West until the 20th century.",
        "origin": "China, 17th century",
        "size": "9-10 inches, 9-16 lbs",
        "temperament": "Affectionate, playful, confident, independent, loves companionship",
        "health_notes": "Brachycephalic breed; prone to breathing problems, eye issues; needs extensive grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Shih_tzu_portrait_floppy_ears.jpg/1024px-Shih_tzu_portrait_floppy_ears.jpg"
    },
    "siberian_husky": {
        "short_desc": "The Siberian Husky is a large, energetic sled dog breed known for their striking appearance with ice-blue eyes and thick double coat. These pack-oriented, friendly dogs require substantial exercise and mental stimulation.",
        "traits": ["Energetic", "Friendly", "Independent", "Athletic"],
        "fun_fact": "Siberian Huskies have double coats that shed so much they 'blow their coat' twice yearly.",
        "origin": "Siberia, Russia, ancient times",
        "size": "20-24 inches, 35-60 lbs",
        "temperament": "Energetic, friendly, independent, athletic, pack dogs",
        "health_notes": "Prone to hip dysplasia, eye problems; needs substantial exercise; escape artists",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Siberian_Husky_blue_eyes_Flickr.jpg/1024px-Siberian_Husky_blue_eyes_Flickr.jpg"
    },
    "staffordshire_bullterrier": {
        "short_desc": "The Staffordshire Bull Terrier is a medium-sized, muscular dog breed known for their strength and loyalty. Despite historical fighting heritage, modern Staffies are affectionate, playful family companions.",
        "traits": ["Strong", "Affectionate", "Playful", "Loyal"],
        "fun_fact": "Staffordshire Bull Terriers are known as 'nanny dogs' due to their gentleness with children.",
        "origin": "Staffordshire, England, 19th century",
        "size": "14-16 inches, 28-38 lbs",
        "temperament": "Strong, affectionate, playful, loyal, excellent with family",
        "health_notes": "Prone to hip dysplasia, allergies; needs firm training and socialization",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Staffordshire_Bull_Terrier.jpg/1024px-Staffordshire_Bull_Terrier.jpg"
    },
    "sussex_spaniel": {
        "short_desc": "The Sussex Spaniel is a medium-sized sporting dog breed with a distinctive golden-liver colored coat. Known for their calm demeanor, loyalty, and excellent hunting abilities, they are devoted family companions.",
        "traits": ["Calm", "Loyal", "Intelligent", "Athletic"],
        "fun_fact": "Sussex Spaniels are known for their distinctive appearance with long, low bodies.",
        "origin": "Sussex, England, 19th century",
        "size": "15-16 inches, 40-50 lbs",
        "temperament": "Calm, loyal, intelligent, athletic, excellent hunters",
        "health_notes": "Prone to hip dysplasia, ear infections; needs regular exercise and grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Sussex_Spaniel.jpg/1024px-Sussex_Spaniel.jpg"
    },
    "tibetan_mastiff": {
        "short_desc": "The Tibetan Mastiff is a large, powerful guardian dog breed with a distinctive lion-like mane. Originally bred to protect livestock in high mountain regions, they are independent, aloof, and devoted to their families.",
        "traits": ["Powerful", "Independent", "Aloof", "Protective"],
        "fun_fact": "Tibetan Mastiffs can weigh up to 160 lbs and have historically protected villages in Tibet.",
        "origin": "Tibet, Himalayas, ancient times",
        "size": "26-29 inches, 100-160 lbs",
        "temperament": "Powerful, independent, aloof with strangers, protective of family",
        "health_notes": "Prone to hip dysplasia, bloat; needs firm training; not suitable for all environments",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Tibetan_Mastiff.jpg/1024px-Tibetan_Mastiff.jpg"
    },
    "tibetan_terrier": {
        "short_desc": "The Tibetan Terrier is a small to medium-sized dog breed with a distinctive long, fluffy coat and playful temperament. Originally bred to herd flocks in Tibet, they are intelligent, loyal family companions.",
        "traits": ["Playful", "Intelligent", "Loyal", "Independent"],
        "fun_fact": "Tibetan Terriers have hair on the soles of their feet, which helped them navigate rocky terrain.",
        "origin": "Tibet, ancient times",
        "size": "15-16 inches, 18-30 lbs",
        "temperament": "Playful, intelligent, loyal, independent, good family dogs",
        "health_notes": "Prone to hip dysplasia, eye problems; needs regular grooming; sensitive to harsh correction",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Tibetan_Terrier.jpg/1024px-Tibetan_Terrier.jpg"
    },
    "walker_hound": {
        "short_desc": "The Walker Hound is a large scent hound breed known for their hunting abilities and friendly nature. Originally bred to hunt foxes and raccoons, they are excellent hunters with pleasant temperaments.",
        "traits": ["Athletic", "Friendly", "Determined", "Loyal"],
        "fun_fact": "Walker Hounds were developed by Thomas Walker in Virginia and remain popular hunting companions.",
        "origin": "Virginia, United States, 19th century",
        "size": "23-27 inches, 50-70 lbs",
        "temperament": "Athletic, friendly, determined, loyal, excellent hunters",
        "health_notes": "Prone to hip dysplasia; needs substantial exercise; strong hunting drive",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Trigg_Hound.jpg/1024px-Trigg_Hound.jpg"
    },
    "weimaraner": {
        "short_desc": "The Weimaraner is a large, athletic sporting dog breed known for their silver-gray coat and incredible speed. These intelligent, elegant dogs are devoted hunters and loyal family companions.",
        "traits": ["Athletic", "Intelligent", "Elegant", "Devoted"],
        "fun_fact": "Weimaraners are known as 'gray ghosts' due to their silver coat and habit of following owners everywhere.",
        "origin": "Germany, 19th century",
        "size": "23-26 inches, 55-90 lbs",
        "temperament": "Athletic, intelligent, elegant, devoted, loves being with family",
        "health_notes": "Prone to hip dysplasia, bloat, heart problems; needs substantial daily exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Weimaraner_2.jpg/1024px-Weimaraner_2.jpg"
    },
    "welsh_springer_spaniel": {
        "short_desc": "The Welsh Springer Spaniel is a medium-sized sporting dog breed with a distinctive red and white coat. Known for their athletic abilities, loyalty, and friendly nature, they are excellent hunting companions and family dogs.",
        "traits": ["Athletic", "Friendly", "Intelligent", "Loyal"],
        "fun_fact": "Welsh Springer Spaniels are built for hunting in Wales and are smaller than English Springers.",
        "origin": "Wales, 19th century",
        "size": "18-19 inches, 40-55 lbs",
        "temperament": "Athletic, friendly, intelligent, loyal, eager to please",
        "health_notes": "Prone to hip dysplasia, ear infections; needs regular exercise and grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Welsh_Springer_Spaniel.jpg/1024px-Welsh_Springer_Spaniel.jpg"
    },
    "west_highland_white_terrier": {
        "short_desc": "The West Highland White Terrier (Westie) is a small, spirited terrier breed known for their distinctive white coat and confident personality. These brave little dogs are excellent family companions with charming dispositions.",
        "traits": ["Spirited", "Brave", "Confident", "Charming"],
        "fun_fact": "West Highland White Terriers were originally bred in Scotland to hunt foxes and other small game.",
        "origin": "West Highland, Scotland, 19th century",
        "size": "11 inches, 15-20 lbs",
        "temperament": "Spirited, brave, confident, charming, good family dogs",
        "health_notes": "Prone to hip dysplasia, Legg-Calvé-Perthes disease, dry skin; needs regular grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/West_Highland_White_Terrier_Crest.jpg/1024px-West_Highland_White_Terrier_Crest.jpg"
    },
    "yorkshire_terrier": {
        "short_desc": "The Yorkshire Terrier is a small toy terrier breed with a long, silky coat and big personality. Despite their delicate appearance, these spirited dogs were originally bred to catch rats in mills and remain fierce hunters.",
        "traits": ["Spirited", "Confident", "Affectionate", "Playful"],
        "fun_fact": "Yorkshire Terriers have hair (not fur) that grows continuously, similar to human hair.",
        "origin": "Yorkshire, England, 19th century",
        "size": "7-8 inches, 4-7 lbs",
        "temperament": "Spirited, confident, affectionate, playful, fierce despite small size",
        "health_notes": "Prone to patellar luxation, dental issues, eye problems; needs regular grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Yorkshireterrier_Groom.jpg/1024px-Yorkshireterrier_Groom.jpg"
    },
    "affenpinscher": {
        "short_desc": "The Affenpinscher is a small, sturdy toy dog breed known for their distinctive monkey-like face and bold personality. These intelligent, loyal dogs are excellent companions with amusing dispositions.",
        "traits": ["Bold", "Intelligent", "Loyal", "Amusing"],
        "fun_fact": "Affenpinschers are nicknamed 'monkey terriers' due to their distinctive facial expressions.",
        "origin": "Germany, 17th century",
        "size": "9-11.5 inches, 7-10 lbs",
        "temperament": "Bold, intelligent, loyal, amusing, confident despite tiny size",
        "health_notes": "Prone to patellar luxation, hip dysplasia, heart problems; needs gentle handling",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Affenpinscher.jpg/1024px-Affenpinscher.jpg"
    },
    "basenji": {
        "short_desc": "The Basenji is a small African hunting dog breed known for their independence, silence (they rarely bark), and cat-like grooming habits. These unique, intelligent dogs are excellent companions for experienced dog owners.",
        "traits": ["Independent", "Alert", "Intelligent", "Unique"],
        "fun_fact": "Basenjis are often called 'barkless dogs' as they produce minimal barking vocalizations.",
        "origin": "Central Africa, ancient times",
        "size": "16-17 inches, 24-26 lbs",
        "temperament": "Independent, alert, intelligent, unique, cat-like grooming habits",
        "health_notes": "Prone to hip dysplasia, hemolytic anemia; needs secure fencing; needs experienced owners",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Basenji_001.jpg/1024px-Basenji_001.jpg"
    },
    "basset": {
        "short_desc": "The Basset Hound is a small to medium scent hound breed known for their distinctive long, droopy ears and short legs. These gentle, stubborn dogs are excellent family companions with laid-back temperaments.",
        "traits": ["Gentle", "Stubborn", "Lazy", "Affectionate"],
        "fun_fact": "Basset Hounds have extraordinarily long ears that can drag on the ground.",
        "origin": "France, 16th century",
        "size": "12-15 inches, 40-65 lbs",
        "temperament": "Gentle, stubborn, lazy, affectionate, excellent scent followers",
        "health_notes": "Prone to hip dysplasia, ear infections, back problems; needs exercise but prefers relaxing",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Basset_Hound.jpg/1024px-Basset_Hound.jpg"
    },
    "beagle": {
        "short_desc": "The Beagle is a small scent hound breed known for their keen sense of smell (220 million scent receptors), curious nature, and friendly temperament. These pack hunters are excellent family companions.",
        "traits": ["Curious", "Friendly", "Determined", "Merry"],
        "fun_fact": "Beagles have approximately 220 million scent receptors, making them exceptional at tracking.",
        "origin": "England, medieval times",
        "size": "13-15 inches, 24-30 lbs",
        "temperament": "Curious, friendly, determined, merry, excellent scent followers",
        "health_notes": "Prone to hip dysplasia, obesity, ear infections; loves to follow scents",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Beagle_4.jpg/1024px-Beagle_4.jpg"
    },
    "black_and_tan_coonhound": {
        "short_desc": "The Black and Tan Coonhound is a large scent hound breed known for their impressive hunting abilities and distinctive coat. These intelligent, friendly dogs are excellent hunters and loyal family companions.",
        "traits": ["Intelligent", "Friendly", "Determined", "Athletic"],
        "fun_fact": "Black and Tan Coonhounds were developed in the American South specifically for hunting raccoons and possums.",
        "origin": "United States (American South), 19th century",
        "size": "23-27 inches, 65-110 lbs",
        "temperament": "Intelligent, friendly, determined, athletic, excellent hunters",
        "health_notes": "Prone to hip dysplasia, bloat; needs substantial exercise and training",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Black_and_tan_coonhound.jpg/1024px-Black_and_tan_coonhound.jpg"
    },
    "bloodhound": {
        "short_desc": "The Bloodhound is a large scent hound breed with exceptional tracking abilities and distinctive wrinkled face with long, droopy ears. These gentle giants are used extensively in search and rescue operations.",
        "traits": ["Gentle", "Determined", "Intelligent", "Dedicated"],
        "fun_fact": "Bloodhounds can track scents over 300 hours old and are used by law enforcement worldwide.",
        "origin": "Belgium/France, 10th century",
        "size": "23-27 inches, 80-110 lbs",
        "temperament": "Gentle, determined, intelligent, dedicated trackers, need experienced handlers",
        "health_notes": "Prone to hip dysplasia, bloat, ear infections; ears need regular cleaning",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Bloodhound_002.jpg/1024px-Bloodhound_002.jpg"
    },
    "bluetick": {
        "short_desc": "The Bluetick Coonhound is a large scent hound breed known for their distinctive 'bluetick' spotted coat and excellent hunting abilities. These energetic dogs are loyal, friendly companions.",
        "traits": ["Energetic", "Friendly", "Determined", "Athletic"],
        "fun_fact": "Bluetick Coonhounds have a distinctive mottled blue-gray coat with black spots.",
        "origin": "United States (Louisiana), 19th century",
        "size": "20-27 inches, 45-80 lbs",
        "temperament": "Energetic, friendly, determined, athletic, excellent hunters",
        "health_notes": "Prone to hip dysplasia; needs substantial exercise; strong hunting drive",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Bluetick_Coonhound.jpg/1024px-Bluetick_Coonhound.jpg"
    },
    "borzoi": {
        "short_desc": "The Borzoi is a large Russian sighthound breed known for their elegant, aristocratic appearance and incredible speed. These graceful, independent dogs are devoted to their families while maintaining aloof dispositions.",
        "traits": ["Elegant", "Independent", "Graceful", "Aloof"],
        "fun_fact": "Borzois can run at speeds up to 40 mph and were bred to hunt wolves in Russia.",
        "origin": "Russia, 9th century",
        "size": "26-32 inches, 60-105 lbs",
        "temperament": "Elegant, independent, graceful, aloof with strangers, devoted to family",
        "health_notes": "Prone to hip dysplasia, bloat, heart problems; sensitive dogs",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Borzoi.jpg/1024px-Borzoi.jpg"
    },
    "boxer": {
        "short_desc": "The Boxer is a medium-sized working dog breed known for their muscular build, playful temperament, and loyalty. These intelligent, energetic dogs are excellent family companions and protective guardians.",
        "traits": ["Playful", "Intelligent", "Loyal", "Energetic"],
        "fun_fact": "Boxers use their front paws to play and fight, like boxers throwing punches, hence their name.",
        "origin": "Germany, 19th century",
        "size": "21-25 inches, 60-70 lbs",
        "temperament": "Playful, intelligent, loyal, energetic, loves their family intensely",
        "health_notes": "Prone to hip dysplasia, bloat, heart problems, cancer; needs firm training",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Boxer_breed.jpg/1024px-Boxer_breed.jpg"
    },
    "briard": {
        "short_desc": "The Briard is a large, intelligent French herding dog breed known for their distinctive long coat and powerful build. These devoted dogs are excellent working companions and loyal family protectors.",
        "traits": ["Intelligent", "Devoted", "Powerful", "Loyal"],
        "fun_fact": "Briards were used as messenger dogs and mine detectors during World War I.",
        "origin": "Brie, France, ancient times",
        "size": "22-26 inches, 55-100 lbs",
        "temperament": "Intelligent, devoted, powerful, loyal, excellent working dogs",
        "health_notes": "Prone to hip dysplasia, Progressive Retinal Atrophy; needs regular grooming and exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Briard_Dog.jpg/1024px-Briard_Dog.jpg"
    },
    "bull_mastiff": {
        "short_desc": "The Bull Mastiff is a large, powerful working dog breed developed from Bulldogs and Mastiffs. Known for their loyalty, strength, and protective instincts, these noble dogs are devoted family companions.",
        "traits": ["Loyal", "Powerful", "Protective", "Calm"],
        "fun_fact": "Bull Mastiffs were bred by English gamekeepers to guard estates and catch poachers.",
        "origin": "England, 19th century",
        "size": "24-27 inches, 100-130 lbs",
        "temperament": "Loyal, powerful, protective, calm, excellent family guardians",
        "health_notes": "Prone to hip dysplasia, bloat, heart problems; needs firm training and socialization",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Bull_Mastiff_standing.jpg/1024px-Bull_Mastiff_standing.jpg"
    },
    "cairn": {
        "short_desc": "The Cairn Terrier is a small, sturdy terrier breed known for their independent spirit and fearless nature. These intelligent, enterprising dogs are excellent family companions with playful personalities.",
        "traits": ["Independent", "Fearless", "Intelligent", "Playful"],
        "fun_fact": "Cairn Terriers were originally bred to hunt small prey among Scottish Highland cairns.",
        "origin": "Scottish Highlands, 19th century",
        "size": "9-10 inches, 13-16 lbs",
        "temperament": "Independent, fearless, intelligent, playful, sometimes stubborn",
        "health_notes": "Generally healthy; prone to hip dysplasia, patellar luxation; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Cairn_Terrier_Brock.jpg/1024px-Cairn_Terrier_Brock.jpg"
    },
    "chow": {
        "short_desc": "The Chow Chow is a large, fluffy Chinese dog breed known for their distinctive blue-black tongue and aloof temperament. These sturdy, lion-like dogs are devoted to their families while remaining independent.",
        "traits": ["Independent", "Aloof", "Devoted", "Sturdy"],
        "fun_fact": "Chow Chows have blue-black tongues, which is rare among dog breeds.",
        "origin": "China, ancient times",
        "size": "17-20 inches, 45-70 lbs",
        "temperament": "Independent, aloof with strangers, devoted to family, dignified",
        "health_notes": "Prone to hip dysplasia, bloat, eye problems; needs patient training and socialization",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Chow_Chow.jpg/1024px-Chow_Chow.jpg"
    },
    "clumber": {
        "short_desc": "The Clumber Spaniel is a large, powerful sporting dog breed known for their gentle temperament and excellent hunting abilities. These loyal, devoted dogs are wonderful family companions.",
        "traits": ["Gentle", "Loyal", "Devoted", "Athletic"],
        "fun_fact": "Clumber Spaniels are the heaviest spaniel breed and were favored by British royalty.",
        "origin": "Clumber Park, England, 19th century",
        "size": "17-20 inches, 55-85 lbs",
        "temperament": "Gentle, loyal, devoted, athletic, excellent hunters and family dogs",
        "health_notes": "Prone to hip dysplasia, bloat, ear infections; needs regular exercise and grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Clumber_Spaniel.jpg/1024px-Clumber_Spaniel.jpg"
    },
    "cocker_spaniel": {
        "short_desc": "The Cocker Spaniel is a medium-sized sporting dog breed known for their beautiful coat, gentle nature, and friendly temperament. These affectionate, eager dogs are excellent family companions and hunters.",
        "traits": ["Friendly", "Gentle", "Eager", "Affectionate"],
        "fun_fact": "Cocker Spaniels were originally bred to hunt woodcock, which inspired their name.",
        "origin": "Spain/England, 14th century (modern breed 19th century)",
        "size": "13.5-15.5 inches, 25-30 lbs",
        "temperament": "Friendly, gentle, eager to please, affectionate, excellent hunters",
        "health_notes": "Prone to hip dysplasia, ear infections, eye problems; needs regular grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/English_Cocker_Spaniel.jpg/1024px-English_Cocker_Spaniel.jpg"
    },
    "collie": {
        "short_desc": "The Collie is a large herding dog breed known for their intelligence, loyalty, and graceful build. Famous from popular media, these devoted dogs make excellent family companions and working dogs.",
        "traits": ["Intelligent", "Loyal", "Graceful", "Devoted"],
        "fun_fact": "Collies were made famous by the television show and movie 'Lassie'.",
        "origin": "Scotland/England border, ancient times",
        "size": "22-26 inches, 50-75 lbs",
        "temperament": "Intelligent, loyal, graceful, devoted, sensitive to harsh correction",
        "health_notes": "Prone to hip dysplasia, progressive retinal atrophy, bloat; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Rough_Collie_portrait030213.jpg/1024px-Rough_Collie_portrait030213.jpg"
    },
    "curly_coated_retriever": {
        "short_desc": "The Curly-Coated Retriever is a large, athletic sporting dog breed with a distinctive tight, curly coat. These intelligent, eager dogs are excellent swimmers and devoted family companions.",
        "traits": ["Athletic", "Intelligent", "Eager", "Loyal"],
        "fun_fact": "Curly-Coated Retrievers have water-resistant curly coats that shed minimally.",
        "origin": "England, 19th century",
        "size": "23-27 inches, 65-100 lbs",
        "temperament": "Athletic, intelligent, eager to please, loyal, excellent swimmers",
        "health_notes": "Prone to hip dysplasia, bloat, eye problems; needs substantial exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Curly_Coated_Retriever.jpg/1024px-Curly_Coated_Retriever.jpg"
    },
    "dhole": {
        "short_desc": "The Dhole, also called the Asian Wild Dog, is a wild canine species native to Asia. These pack hunters are distinct from domestic dogs and are listed as endangered species.",
        "traits": ["Pack-Oriented", "Intelligent", "Cooperative", "Wild"],
        "fun_fact": "Dholes hunt in coordinated packs and are sometimes called 'red wolves' despite not being related.",
        "origin": "Asia (India, Southeast Asia), wild populations",
        "size": "15-21 inches, 22-33 lbs",
        "temperament": "Pack-oriented, intelligent, cooperative, wild animals",
        "health_notes": "Wild animals; endangered species; cannot be domesticated",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Dhole.jpg/1024px-Dhole.jpg"
    },
    "dingo": {
        "short_desc": "The Dingo is a wild canine native to Australia. These semi-domesticated dogs are efficient hunters adapted to Australian environments and are distinct from domestic dog breeds.",
        "traits": ["Wild", "Efficient", "Independent", "Alert"],
        "fun_fact": "Dingoes have been in Australia for thousands of years and are sometimes considered feral dogs.",
        "origin": "Australia, ancient times",
        "size": "19-24 inches, 22-33 lbs",
        "temperament": "Wild, efficient hunters, independent, alert",
        "health_notes": "Wild animals; adapted to harsh environments; not suitable as pets",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Dingo.jpg/1024px-Dingo.jpg"
    },
    "flat_coated_retriever": {
        "short_desc": "The Flat-Coated Retriever is a large, athletic sporting dog breed with a sleek black or liver coat. Known for their good humor, enthusiasm, and loyalty, they are excellent hunters and devoted family companions.",
        "traits": ["Enthusiastic", "Athletic", "Loyal", "Good-Natured"],
        "fun_fact": "Flat-Coated Retrievers are sometimes called 'Yeoman of England' due to their aristocratic heritage.",
        "origin": "England, 19th century",
        "size": "23-24 inches, 60-70 lbs",
        "temperament": "Enthusiastic, athletic, loyal, good-natured, eager to please",
        "health_notes": "Prone to hip dysplasia, cancer, bloat; needs substantial exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flat-coated_retriever.jpg/1024px-Flat-coated_retriever.jpg"
    },
    "giant_schnauzer": {
        "short_desc": "The Giant Schnauzer is a large, powerful working dog breed known for their intelligence, courage, and distinctive appearance. These devoted dogs are excellent working dogs and loyal family companions.",
        "traits": ["Intelligent", "Courageous", "Powerful", "Loyal"],
        "fun_fact": "Giant Schnauzers were originally developed to guard cattle and later used as police and military dogs.",
        "origin": "Bavaria, Germany, 19th century",
        "size": "23.5-27.5 inches, 65-100 lbs",
        "temperament": "Intelligent, courageous, powerful, loyal, needs firm training",
        "health_notes": "Prone to hip dysplasia, bloat; needs regular exercise and mental stimulation",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Giant_Schnauzer.jpg/1024px-Giant_Schnauzer.jpg"
    },
    "golden_retriever": {
        "short_desc": "The Golden Retriever is one of the most popular dog breeds, known for their friendly, intelligent, and tolerant nature. These beautiful, athletic dogs are excellent family companions and versatile working dogs.",
        "traits": ["Friendly", "Intelligent", "Tolerant", "Athletic"],
        "fun_fact": "Golden Retrievers are consistently ranked among the top 5 most popular dog breeds worldwide.",
        "origin": "Scotland, 19th century",
        "size": "20-24 inches, 55-75 lbs",
        "temperament": "Friendly, intelligent, tolerant, athletic, loves family",
        "health_notes": "Prone to hip dysplasia, heart disease, cancer; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Golden_Retriever.jpg/1024px-Golden_Retriever.jpg"
    },
    "groenendael": {
        "short_desc": "The Groenendael is a large Belgian herding dog breed with a distinctive black coat. Known for their intelligence, athleticism, and versatility, they excel as working dogs and family companions.",
        "traits": ["Intelligent", "Athletic", "Versatile", "Loyal"],
        "fun_fact": "Groenendaels are one of four Belgian Shepherd varieties and are used extensively in police work.",
        "origin": "Groenendael, Belgium, 19th century",
        "size": "22-26 inches, 55-75 lbs",
        "temperament": "Intelligent, athletic, versatile, loyal, needs substantial exercise",
        "health_notes": "Prone to hip dysplasia, bloat; needs mental and physical stimulation",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Groenendael_sitting.jpg/1024px-Groenendael_sitting.jpg"
    },
    "keeshond": {
        "short_desc": "The Keeshond is a medium-sized spitz-type dog breed known for their distinctive 'spectacles' markings and friendly nature. These intelligent, devoted dogs are excellent family companions and excellent watchdogs.",
        "traits": ["Friendly", "Intelligent", "Devoted", "Alert"],
        "fun_fact": "Keeshonds are sometimes called 'Dutch Barge Dogs' as they were kept on Dutch riverboats.",
        "origin": "Netherlands, 18th century",
        "size": "17-18 inches, 35-45 lbs",
        "temperament": "Friendly, intelligent, devoted, alert, good family dogs",
        "health_notes": "Prone to hip dysplasia, thyroid problems; needs regular grooming and exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Keeshond.jpg/1024px-Keeshond.jpg"
    },
    "kelpie": {
        "short_desc": "The Kelpie is a small to medium-sized Australian herding dog breed known for their intelligence, energy, and exceptional working abilities. These versatile dogs are still used extensively on Australian farms.",
        "traits": ["Intelligent", "Energetic", "Versatile", "Athletic"],
        "fun_fact": "Kelpies are named after a water spirit from Scottish mythology and are considered Australia's national dog.",
        "origin": "Australia, 19th century",
        "size": "17-20 inches, 25-45 lbs",
        "temperament": "Intelligent, energetic, versatile, athletic, needs substantial mental stimulation",
        "health_notes": "Generally healthy; prone to hip dysplasia; needs active lifestyle",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Kelpie_standing.jpg/1024px-Kelpie_standing.jpg"
    },
    "komondor": {
        "short_desc": "The Komondor is a large Hungarian livestock guardian dog breed with a distinctive corded white coat resembling dreadlocks. These powerful, independent dogs are devoted protectors with strong guardian instincts.",
        "traits": ["Powerful", "Independent", "Protective", "Devoted"],
        "fun_fact": "Komondors have unique corded coats that can take years to develop fully and resemble mop strings.",
        "origin": "Hungary, ancient times",
        "size": "25.5-31.5 inches, 80-100+ lbs",
        "temperament": "Powerful, independent, protective, devoted to family",
        "health_notes": "Prone to hip dysplasia, bloat; needs specialized coat care; not for first-time owners",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Komondor.jpg/1024px-Komondor.jpg"
    },
    "kuvasz": {
        "short_desc": "The Kuvasz is a large Hungarian livestock guardian dog breed with a white coat and powerful build. These loyal, protective dogs are devoted to their families while maintaining independent natures.",
        "traits": ["Loyal", "Protective", "Independent", "Powerful"],
        "fun_fact": "Kuvaszok were favored by Hungarian kings and were used to guard royal estates.",
        "origin": "Hungary, ancient times",
        "size": "26-30 inches, 100-115 lbs",
        "temperament": "Loyal, protective, independent, powerful, needs firm training",
        "health_notes": "Prone to hip dysplasia, bloat; needs firm, consistent training",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Kuvasz.jpg/1024px-Kuvasz.jpg"
    },
    "malamute": {
        "short_desc": "The Alaskan Malamute is a large, powerful Arctic sled dog breed known for their strength, endurance, and friendly nature. These massive dogs are devoted family companions that require experienced owners.",
        "traits": ["Powerful", "Friendly", "Loyal", "Energetic"],
        "fun_fact": "Alaskan Malamutes can weigh up to 100 lbs and can pull sleds with loads over 1000 lbs.",
        "origin": "Alaska (Mahlemut Inuit), ancient times",
        "size": "23-25 inches, 75-100 lbs",
        "temperament": "Powerful, friendly, loyal, energetic, pack-oriented",
        "health_notes": "Prone to hip dysplasia, bloat; needs substantial exercise; escape artists",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Alaskan_Malamute.jpg/1024px-Alaskan_Malamute.jpg"
    },
    "malinois": {
        "short_desc": "The Belgian Malinois is a large, athletic herding dog breed similar to German Shepherds but more refined. Known for their intelligence, drive, and versatility, they excel as military and police dogs.",
        "traits": ["Intelligent", "Athletic", "Driven", "Versatile"],
        "fun_fact": "Belgian Malinois are preferred over German Shepherds for many military and police roles due to their athleticism.",
        "origin": "Malines, Belgium, 19th century",
        "size": "22-26 inches, 55-75 lbs",
        "temperament": "Intelligent, athletic, driven, versatile, needs substantial mental and physical stimulation",
        "health_notes": "Prone to hip dysplasia, bloat; needs experienced owners and firm training",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Belgian_Malinois.jpg/1024px-Belgian_Malinois.jpg"
    },
    "miniature_pinscher": {
        "short_desc": "The Miniature Pinscher is a small toy dog breed with a distinctive appearance and bold personality. Despite their tiny size, these spirited dogs have fearless temperaments and are excellent companions.",
        "traits": ["Bold", "Fearless", "Spirited", "Confident"],
        "fun_fact": "Miniature Pinschers are nicknamed 'Min Pins' and are sometimes called 'Miniature Dobermans'.",
        "origin": "Germany, 19th century",
        "size": "10-12.5 inches, 8-11 lbs",
        "temperament": "Bold, fearless, spirited, confident, big personality in tiny package",
        "health_notes": "Prone to patellar luxation, hip dysplasia, heart problems; needs firm training",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/MinPin_standing.jpg/1024px-MinPin_standing.jpg"
    },
    "miniature_poodle": {
        "short_desc": "The Miniature Poodle is an intelligent toy dog breed with a hypoallergenic curly coat. Known for their trainability, cleverness, and lively personality, they are excellent companion dogs.",
        "traits": ["Intelligent", "Lively", "Clever", "Devoted"],
        "fun_fact": "Miniature Poodles are among the most trainable dog breeds and excel in obedience competitions.",
        "origin": "France/Germany, 15th century (modern size 20th century)",
        "size": "11 inches or under, 10-15 lbs",
        "temperament": "Intelligent, lively, clever, devoted, loves mental stimulation",
        "health_notes": "Prone to hip dysplasia, patellar luxation, eye problems; needs regular grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Miniature_poodle_white.jpg/1024px-Miniature_poodle_white.jpg"
    },
    "miniature_schnauzer": {
        "short_desc": "The Miniature Schnauzer is a small, sturdy terrier breed with a distinctive beard and eyebrows. Known for their intelligence, loyalty, and spirited nature, they are excellent family companions.",
        "traits": ["Intelligent", "Spirited", "Loyal", "Sturdy"],
        "fun_fact": "Miniature Schnauzers have distinctive whiskers and a beard that requires regular grooming.",
        "origin": "Germany, 19th century",
        "size": "11-14 inches, 11-20 lbs",
        "temperament": "Intelligent, spirited, loyal, sturdy, good family dogs",
        "health_notes": "Prone to hip dysplasia, pancreatitis, eye problems; needs regular grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Miniature_Schnauzer.jpg/1024px-Miniature_Schnauzer.jpg"
    },
    "otterhound": {
        "short_desc": "The Otterhound is a large, rare scent hound breed originally bred to hunt otters in England. Known for their friendliness, athleticism, and excellent swimming abilities, they are devoted family companions.",
        "traits": ["Friendly", "Athletic", "Intelligent", "Devoted"],
        "fun_fact": "Otterhounds have water-resistant double coats and webbed feet for excellent swimming.",
        "origin": "England, 12th century",
        "size": "24-27 inches, 80-115 lbs",
        "temperament": "Friendly, athletic, intelligent, devoted, loves water",
        "health_notes": "Prone to hip dysplasia, bloat; needs substantial exercise and swimming opportunities",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Otterhound.jpg/1024px-Otterhound.jpg"
    },
    "papillon": {
        "short_desc": "The Papillon is a small toy spaniel breed with distinctive large, butterfly-like ears that inspired their name. Known for their intelligence, trainability, and exceptional agility, they are excellent companion dogs.",
        "traits": ["Intelligent", "Trainable", "Agile", "Friendly"],
        "fun_fact": "Papillons are one of the most intelligent toy breeds and consistently win agility competitions.",
        "origin": "France/Belgium, 16th century",
        "size": "8-10 inches, 5-10 lbs",
        "temperament": "Intelligent, trainable, agile, friendly, loves mental stimulation",
        "health_notes": "Prone to patellar luxation, hip dysplasia; generally healthy; sensitive to harsh correction",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Papillon_2009.jpg/1024px-Papillon_2009.jpg"
    },
    "pug": {
        "short_desc": "The Pug is a small toy dog breed from China known for their distinctive wrinkled face and compact body. These charming, affectionate dogs are excellent companions for apartment living.",
        "traits": ["Charming", "Affectionate", "Playful", "Mischievous"],
        "fun_fact": "Pugs have been favored by royalty for thousands of years and are featured in Chinese art.",
        "origin": "China, ancient times",
        "size": "10-11 inches, 14-18 lbs",
        "temperament": "Charming, affectionate, playful, mischievous, loves attention",
        "health_notes": "Brachycephalic breed; prone to breathing problems, eye issues, obesity; needs heat protection",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Pug_portrait.jpg/1024px-Pug_portrait.jpg"
    },
    "redbone": {
        "short_desc": "The Redbone Coonhound is a large scent hound breed with a distinctive red coat. Known for their hunting abilities, loyalty, and friendly nature, they are excellent hunters and family companions.",
        "traits": ["Loyal", "Friendly", "Determined", "Athletic"],
        "fun_fact": "Redbone Coonhounds are known for their distinctive baying and are excellent scent trailers.",
        "origin": "United States (American South), 19th century",
        "size": "22-27 inches, 50-70 lbs",
        "temperament": "Loyal, friendly, determined, athletic, excellent hunters",
        "health_notes": "Prone to hip dysplasia; needs substantial exercise; strong hunting drive",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Redbone_Coonhound.jpg/1024px-Redbone_Coonhound.jpg"
    },
    "schipperke": {
        "short_desc": "The Schipperke is a small Belgian dog breed known for their black coat and bold personality. Originally bred as barge dogs, they are excellent companions with spirited, independent natures.",
        "traits": ["Bold", "Independent", "Spirited", "Loyal"],
        "fun_fact": "Schipperkes were originally used to guard barges on Belgian canals and were called 'little captains'.",
        "origin": "Belgium, 16th century",
        "size": "10-13 inches, 12-16 lbs",
        "temperament": "Bold, independent, spirited, loyal, good family dogs",
        "health_notes": "Generally healthy; prone to hip dysplasia, patellar luxation; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Schipperke.jpg/1024px-Schipperke.jpg"
    },
    "silky_terrier": {
        "short_desc": "The Silky Terrier is a small toy terrier breed with a distinctive long, silky coat. These spirited, devoted dogs are excellent companions for families with their friendly and playful natures.",
        "traits": ["Spirited", "Devoted", "Friendly", "Playful"],
        "fun_fact": "Silky Terriers have long, silky coats that resemble human hair and need regular grooming.",
        "origin": "Australia (Sydney), 19th century",
        "size": "9-10 inches, 8-10 lbs",
        "temperament": "Spirited, devoted, friendly, playful, good family dogs",
        "health_notes": "Generally healthy; prone to patellar luxation, hip dysplasia; needs regular grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Silky_Terrier.jpg/1024px-Silky_Terrier.jpg"
    },
    "soft_coated_wheaten_terrier": {
        "short_desc": "The Soft-Coated Wheaten Terrier is a medium-sized terrier breed with a distinctive soft, wheaten-colored coat. Known for their friendly, spirited nature and excellent temperament, they are devoted family companions.",
        "traits": ["Friendly", "Spirited", "Devoted", "Athletic"],
        "fun_fact": "Soft-Coated Wheaten Terriers are sometimes called 'Wheaten Terriers' or 'Wheatens' for short.",
        "origin": "Ireland, 19th century",
        "size": "17-19 inches, 30-40 lbs",
        "temperament": "Friendly, spirited, devoted, athletic, excellent family dogs",
        "health_notes": "Prone to hip dysplasia, bloat, kidney disease; needs regular exercise and grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Soft-coated_Wheaten_Terrier.jpg/1024px-Soft-coated_Wheaten_Terrier.jpg"
    },
    "standard_poodle": {
        "short_desc": "The Standard Poodle is a large, intelligent dog breed known for their curly coat and exceptional trainability. These elegant, athletic dogs are excellent working dogs and devoted family companions.",
        "traits": ["Intelligent", "Athletic", "Elegant", "Devoted"],
        "fun_fact": "Poodles were originally bred in Germany as water retrievers and are exceptional swimmers.",
        "origin": "Germany/France, 15th century",
        "size": "22 inches or more, 45-70 lbs",
        "temperament": "Intelligent, athletic, elegant, devoted, loves mental stimulation",
        "health_notes": "Prone to hip dysplasia, Progressive Retinal Atrophy; needs regular grooming and exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Apricot_Standard_Poodle.jpg/1024px-Apricot_Standard_Poodle.jpg"
    },
    "standard_schnauzer": {
        "short_desc": "The Standard Schnauzer is a medium-sized working dog breed with a distinctive beard and wiry coat. Known for their intelligence, loyalty, and spirited nature, they are excellent family companions.",
        "traits": ["Intelligent", "Loyal", "Spirited", "Alert"],
        "fun_fact": "Standard Schnauzers are the original schnauzer breed, from which Miniature and Giant Schnauzers were developed.",
        "origin": "Germany, 15th century",
        "size": "17.5-19.5 inches, 30-50 lbs",
        "temperament": "Intelligent, loyal, spirited, alert, good family dogs",
        "health_notes": "Generally healthy; prone to hip dysplasia, eye problems; needs regular grooming and exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Standard_Schnauzer_Cropped.jpg/1024px-Standard_Schnauzer_Cropped.jpg"
    },
    "toy_poodle": {
        "short_desc": "The Toy Poodle is a small, intelligent companion dog breed with a hypoallergenic curly coat. Known for their trainability, playfulness, and devotion, they are excellent apartment companions.",
        "traits": ["Intelligent", "Playful", "Devoted", "Lively"],
        "fun_fact": "Toy Poodles are among the smallest dog breeds and are excellent for apartment living.",
        "origin": "France/Germany, 20th century (modern size)",
        "size": "10 inches or under, 4-6 lbs",
        "temperament": "Intelligent, playful, devoted, lively, loves mental stimulation",
        "health_notes": "Prone to patellar luxation, hip dysplasia, eye problems; needs regular grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Miniature_poodle_white.jpg/1024px-Miniature_poodle_white.jpg"
    },
    "toy_terrier": {
        "short_desc": "The Toy Terrier is a small British toy breed with a distinctive black and tan coat. Known for their intelligence, loyalty, and spirited nature, they are excellent apartment companions.",
        "traits": ["Intelligent", "Loyal", "Spirited", "Alert"],
        "fun_fact": "Toy Terriers are among the smallest dog breeds and are excellent ratters despite their size.",
        "origin": "England, 19th century",
        "size": "9-12 inches, 4-9 lbs",
        "temperament": "Intelligent, loyal, spirited, alert, good family dogs",
        "health_notes": "Prone to patellar luxation, hip dysplasia; needs firm training and socialization",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/English_Toy_Terrier.jpg/1024px-English_Toy_Terrier.jpg"
    },
    "vizsla": {
        "short_desc": "The Vizsla is a medium-sized hunting dog breed known for their elegant build, short rust-colored coat, and athletic abilities. These affectionate, sensitive dogs are devoted family companions.",
        "traits": ["Elegant", "Affectionate", "Sensitive", "Athletic"],
        "fun_fact": "Vizslas are called 'velcro dogs' because they love to stick close to their owners.",
        "origin": "Hungary, 10th century",
        "size": "21-24 inches, 55-60 lbs",
        "temperament": "Elegant, affectionate, sensitive, athletic, loves family interaction",
        "health_notes": "Prone to hip dysplasia, bloat, cancer; needs substantial daily exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Vizsla_2009.jpg/1024px-Vizsla_2009.jpg"
    },
    "whippet": {
        "short_desc": "The Whippet is a medium-sized sighthound breed known for their speed, grace, and gentle nature. These athletic dogs are excellent companions for families that appreciate their quiet, calm temperaments.",
        "traits": ["Swift", "Graceful", "Gentle", "Calm"],
        "fun_fact": "Whippets can reach speeds up to 35 mph and are nicknamed 'poor man's racehorses'.",
        "origin": "England, 19th century",
        "size": "18-22 inches, 25-40 lbs",
        "temperament": "Swift, graceful, gentle, calm, excellent family dogs",
        "health_notes": "Generally healthy; prone to heart problems; sensitive to cold; needs secure fencing",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Whippet_001.jpg/1024px-Whippet_001.jpg"
    },
    "wire_haired_fox_terrier": {
        "short_desc": "The Wire-Haired Fox Terrier is a small, sturdy terrier breed with a distinctive wiry coat and bold temperament. Known for their confidence, independence, and friendly nature, they are excellent family companions.",
        "traits": ["Bold", "Independent", "Confident", "Friendly"],
        "fun_fact": "Wire-Haired Fox Terriers have distinctive wiry coats that are naturally water and dirt resistant.",
        "origin": "England, 19th century",
        "size": "15.5 inches, 17-19 lbs",
        "temperament": "Bold, independent, confident, friendly, sometimes stubborn",
        "health_notes": "Generally healthy; prone to hip dysplasia, eye problems; needs firm training",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Wire_Fox_Terrier.jpg/1024px-Wire_Fox_Terrier.jpg"
    },
}

if __name__ == "__main__":
    print(f"Total breeds in database: {len(BREED_DATABASE)}")
    print("Sample breed:", BREED_DATABASE["golden_retriever"]["short_desc"][:100] + "...")
