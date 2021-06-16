import db
import time,os

db.mycursor.execute('SELECT COUNT(*) FROM lists l JOIN (SELECT list_id, COUNT(*) FROM list_items GROUP BY list_id) my ON l.list_id=my.list_id')

total_transactions = db.mycursor.fetchone()[0]

if total_transactions > 50:
    db.mycursor.execute('SELECT item_id, COUNT(*) FROM list_items GROUP BY item_id')
    occurences = db.mycursor.fetchall()
    
    frequent = list()
    single_offer = list()
    
    #For An Item To Be Considered For Offer
    min_support_transaction = 50
    
    #For Single Item Purchase
    min_confidence_pattern1 = 65
    
    #For Two Item Combo Purchase
    min_confidence_pattern2 = 40
    
    for item in occurences:
        if int((item[1]/total_transactions) * 100) >= min_support_transaction:
            frequent.append(item[0])
            
        if int((item[1]/total_transactions) * 100) >= min_confidence_pattern1:
            single_offer.append(item[0])
            
    pattern_nums = list()       
    for index, item1 in enumerate(frequent):

        for ind, item2 in enumerate(frequent):
            if ind <= index:
                continue
            
            
            db.mycursor.execute(
                'SELECT COUNT(*) FROM list_items l1 CROSS JOIN list_items l2 WHERE l1.item_id=%s AND l2.item_id=%s AND l1.list_id=l2.list_id', [item1, item2])
            
            occur = db.mycursor.fetchone()
            if not occur[0]:
                continue
            
            db.mycursor.execute('select count(*) from list_items where item_id = %s', [item1])
            occur1 = db.mycursor.fetchone()[0]
            
            if (occur[0]/occur1) * 100 >= min_confidence_pattern2:
                pattern_nums.append((item1,item2))
        
    for item in single_offer:
        db.mycursor.execute('insert into offers (item_id1) values (%s);', [item])
                    

    for pattern in pattern_nums:
        db.mycursor.execute('insert into offers (item_id1, item_id2) values (%s, %s);', [pattern[0], pattern[1]])
    
    



def show_offers():
    db.mycursor.execute('select * from offers;')
    offers = db.mycursor.fetchall()

    for offer in offers:
        db.mycursor.execute(
            'select item_name from items where item_id = %s;', [offer[1]])
        item1_name = db.mycursor.fetchone()[0]

        if not offer[2]:
            print(f"{offer[0]}. {item1_name} at a discounted rate of 20 percent.\n")
            continue

        db.mycursor.execute(
            'select item_name from items where item_id = %s;', [offer[2]])
        item2_name = db.mycursor.fetchone()[0]

        print(
            f"{offer[0]}. {item1_name} and {item2_name} together at a discount rate of 25 percent.\n")
        
        
    input("Press Enter To Continue")
    os.system('cls')
    
    
    
def show_selected_offers(item_id):
    db.mycursor.execute('select * from offers where %s in (item_id1, item_id2);', [item_id])
    offers = db.mycursor.fetchall()

    for offer in offers:
        db.mycursor.execute(
            'select item_name from items where item_id = %s;', [offer[1]])
        item1_name = db.mycursor.fetchone()[0]

        if not offer[2]:
            continue

        db.mycursor.execute(
            'select item_name from items where item_id = %s;', [offer[2]])
        item2_name = db.mycursor.fetchone()[0]

        print(
            f"{offer[0]}. {item1_name} and {item2_name} together at a discount rate of 25 percent.\n")
    
    
def check_offer(offer_id, item_id):
    db.mycursor.execute("select * from offers where offers_id = %s;", [offer_id])
    result = db.mycursor.fetchone()
    
    if not result:
        return False
    
    if not result[2]:
        print("This Offer Is Only Valid On Single Purchases!")
        return False
    
    if result[1] == item_id or result[2] == item_id:
        return True
    
    return False


def get_prices(offer_id):
    db.mycursor.execute("select * from offers where offers_id = %s;", [offer_id])
    result = db.mycursor.fetchone()
    
    db.mycursor.execute("select item_price from items where item_id = %s", [result[1]])
    price1 = db.mycursor.fetchone()[0]
    
    db.mycursor.execute("select item_price from items where item_id = %s", [result[2]])
    price2 = db.mycursor.fetchone()[0]
    
    return (result[1], result[2], price1*0.75, price2*0.75)
