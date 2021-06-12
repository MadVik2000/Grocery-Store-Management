def generate_salt(username):
    
    salt = ''
    my_char_list = ['abc','def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    for char in username.lower():
        if char.isnumeric():
            salt = salt + '1'
            continue
        
        if char.isalpha():
            
            for index,words in enumerate(my_char_list):
                if char in words:
                    
                    salt = salt + str(index+2)
                    break
                
            continue
        
        salt = salt + '0'
        
        
    return salt
