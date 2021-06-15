import db

db.mycursor.execute('SELECT COUNT(*) FROM lists l JOIN (SELECT list_id, COUNT(*) FROM list_items GROUP BY list_id) my ON l.list_id=my.list_id')

total_transactions = db.mycursor.fetchone()[0]

if total_transactions > 50:
    db.mycursor.execute('SELECT item_id, COUNT(*) FROM list_items GROUP BY item_id')
    occurences = db.mycursor.fetchall()
    
    frequent = list()
    min_support_transaction = 50
    min_confidence_pattern = 40
    
    for item in occurences:
        if int((item[1]/total_transactions) * 100) >= min_support_transaction:
            frequent.append(item[0])
            
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
            
            if (occur[0]/occur1) * 100 >= min_confidence_pattern:
                pattern_nums.append((item1,item2))