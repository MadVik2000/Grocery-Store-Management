ITEMS = ["Fruits", "Vegetables", "Rice / Grains / Pulses", "Salt / Sugar / Spices",
         "Flours / Semolina (Rava) / Processed Grains", "Ground Spices / Masalas", "Dairy / Frozen Food",
         "Bread / Poultry / Cereals / Snacks", "Beverages", "Accompaniments", "Sweets / Dry Fruits", 
         "Baking & Dessert Preparation", "Oil/ Ghee"]

FRUITS = [(1, 'Apple', 30), (1, 'Banana', 50), (1, 'Grapes', 60), (1, 'Guava', 40), (1, 'Litchi', 70), (1, 'Mango', 120),
          (1, 'Orange', 50), (1, 'Papapya', 60), (1, 'Pear',30), (1, 'Pineapple', 80), (1, 'Pomegranate', 70),
          (1, 'Watermelon', 80)]

VEGETABLES = []

RICEGRAINPULSES = [
    (3, 'Rice - Boiled', 250),  (3, 'Rice - Basmati', 350),  (3, 'Dosa Rice', 200),
    (3, 'Sago Rice[Sabu Dana]', 150),  (3, 'Split Red Gram[Toor Dal]', 200),
    (3, 'Green Gram[Moong Sabut]', 180),  (3, 'Green Gram Split[Moong Dal]', 200),
    (3, 'Black Gram[Urad Gota]', 150),  (3, 'Black Gram Split[Urad Dal]', 170),
    (3, 'Bengal Gram[Chana]', 160),  (3, 'Bengal Gram Split[Chana Dal]', 75),
    (3, 'Horse Gram[Kulthi]', 150),  (3, 'Red Lentil[Masoor Dal]', 200),
    (3, 'Green Chickpea[Hara Chana]', 120),  (3, 'Fried Gram', 135),
    (3, 'Black-Eyed Pea[Chowli]', 140),  (3, 'Chickpeas[Kabuli Chana]', 160),
    (3, 'Ground Nut[Moongfalli]', 80),  (3, 'Kidney Beans[Rajma]', 210),
    (3, 'Turkish Gram[Mott / Matki]', 150),  (3, 'Wheat[Gehu]', 100),  (3, 'Finger Millet[Ragi]', 120),
    (3, 'Green Peas Dry[Sukha Matar]', 100)
]

SALTSUGARSPICES = [
    (4, 'Rock Salt', 20),  (4, 'Sugar', 60),  (4, 'Sugar Free', 90),
    (4, 'Crystal Sugar', 50),  (4, 'Jaggery[Gud]', 120),  (4, 'Tamarind[Imli]', 60),
    (4, 'Dry Chilli[Sukha Mirchi]', 50),  (4, 'CorianderSeeds[Dhaniya]', 40),
    (4, 'Fenugreek Seeds[Methi]', 70),  (4, 'Mustard Seeds[Sarson]', 40),
    (4, 'Sesame Seeds[Til]', 40),  (4, 'Peppercorn[Kali Mirch]', 55),
    (4, 'Cumin[Jeera]', 45),  (4, 'Caraway Seeds[Shah Jeera]', 50),
    (4, 'Poppy Seeds[Khus Khus]', 60),  (4, 'Cardamom[Elaichi]', 80),
    (4, 'Black Cardamom[Badi Elaichi]', 120),  (4, 'Clove[Laung]', 100),
    (4, 'Fennel[Saunf]', 60),  (4,'Bay Leaf[Tez Patta]', 60),  (4, 'Cinnamon[Dalchini]', 120),
    (4, 'Mace[Javitri]', 100),  (4, 'Fenugreek Leaves[Kasuri Methi]', 70),
    (4, 'Nutmeg[Jaiphal]', 80),  (4, 'Star Anise[Ananas ka pool]', 120),
    (4, 'Carom Seeds[Ajwain]', 50),  (4, 'White Pepper[Safed mirchi]', 85),
    (4, 'Saffron[Kesar]', 240),  (4, 'Turmeric Sticks[Haldi Gota]', 150),
    (4, 'Turmeric Powder[Haldi]', 100),  (4, 'Nigella Seeds[Kalonji]', 60),
    (4, 'Cumin Powder[Jeera Powder]', 50),  (4, 'Fenugreek Powder[Dhaniya Powder]', 50),
    (4, 'Pepper Powder[Kalimirch Powder]', 40),  (4, 'Asafoetida[Heeng]', 60),
    (4, 'Dried Mango Powder[Amchur]', 75),  (4, 'Dried Ginger[Sonth]', 110),  (4, 'Garcinia[Kokum]', 130)
]


FLOURSEMOLINAPROCESSEDGRAINS = [
    (5, 'Wheat Flour[Gehu ka Atta]', 310),  (5, 'Rice Flour[Chaval ka Atta]', 350),
    (5, 'All-Purpose Flour[Maida]', 100),  (5, 'Gram Flour[Besan]', 80),
    (5, 'Cornflour[Makke ka Atta]', 150),  (5, 'Wheat Semolina[Upma Rava]', 70),
    (5, 'Rice Semolina[Rice/Idli Rava]', 80),  (5, 'Broken Wheat[Daliya]', 50),
    (5, 'Finger Millet Flour[Ragi Flour]', 150),  (5, 'Bansi Rava[Bangalore Rava]', 180),
    (5, 'Beaten Rice[Poha]', 40),  (5, 'Puffed Rice[Murmura]', 30),
    (5, 'Semolina[Semiya]', 50),  (5, 'Roasted Rava', 80)
]

GROUNDSPICES = [
    (6, 'Kesar Milk Powder', 60),  (6, 'Tea Masala', 50),  (6, 'Garam Masala', 70),
    (6, 'Kitchen King', 70),  (6, 'Pav Bhaji Masala', 70),  (6, 'Cholle Masala', 70),
    (6, 'Rajma Masala', 80),  (6, 'Sabzi Masala', 50),  (6, 'Biryani/Pulav Masala', 80),
    (6, 'Fish Curry Masala', 100),  (6, 'Egg Curry Masala', 90),  (6, 'Chicken Masala', 100),
    (6, 'Meat Masala', 120),  (6, 'Jaljira Powder', 20),  (6, 'Chat Powder', 40),
    (6, 'Sambar Powder', 70),  (6, 'Rasam Powder', 70)
]

DAIRYFROZENFOOD = [
    (7, 'Milk', 60), (7, 'Milk Powder', 70), (7, 'Butter', 100), (7, 'Cheese', 140),
    (7, 'Khoya', 60), (7, 'Fresh Cream', 50), (7, 'Curds', 75), (7, 'Paneer', 420),
    (7, 'Ice Cream', 60), (7, 'Frozen Peas', 120), (7, 'Frozen Vegetables', 90),
    (7, 'Frozen Ready-To-Eat', 240), (7, 'Frozen Chicken/Meat/Fish', 350)
    ]

BREADPOULTRYCEREALSSNACKS = [
    (8, 'Bread', 35),  (8, 'Eggs/Chicken', 120),  (8, 'Mixtures', 80),
    (8, 'Biscuits', 80),  (8, 'Cake', 150),  (8, 'Noodles', 60),
    (8, 'Pasta', 120),  (8, 'Cornflakes', 70),  (8, 'Oats', 90),
    (8, 'Muesli', 100)
]

BEVERAGES = [
    (9, 'Tea Leaves/Powder', 80),  (9, 'Coffee(Ground/Seeds)', 150),  (9, 'Infant/Kids Drink', 30),
    (9, 'Soft Drink', 50),  (9, 'Juice', 40),  (9, 'Chocolate/Flavoured Syrups', 70)
]

ACCOMPANIMENTS = [
    (10, 'Jams/Marmalades', 70),  (10, 'Sauce/Ketchup', 1110),  (10, 'Pickle', 60),
    (10, 'Condensed Milk', 70),  (10, 'Honey', 210),  (10, 'Vinegar', 50),
    (10, 'Papad', 20)
]

SWEETSDRYFRUITS = [
    (11, 'Indian Sweets', 220),  (11, 'Chocolates/Toffees/Candies', 60),  (11, 'Pistachio[Pista]', 90),
    (11, 'Almonds[Badam]', 160),  (11, 'Figs[Anjeer]', 100),  (11, 'Apricots[Khumani]', 80),
    (11, 'Dates[Khajoor]', 100),  (11, 'Raisins[Kismis]', 80),  (11, 'Walnuts[Akhrot]', 80)
]

BAKINGDESSERTPREPERATION = [
    (12, 'Baking Soda', 30),  (12, 'Baking Powder', 50), (12, 'Food Colour/Essence/Flavoring Agents', 40),
    (12, 'Custard Powder', 120),  (12, 'Jelly Mix', 60),  (12, 'Cocoa Powder', 80)
]

OILGHEE = [
    (13, 'Refined Oil', 210),  (13, 'Vegetable Oil', 180),  (13, 'Ghee', 350),
    (13, 'Vanaspati', 210),  (13, 'Coconut Oil', 220),  (13, 'Pooja Oil', 120)
]
