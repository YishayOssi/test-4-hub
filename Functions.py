def Caesar1(text:str, num:int):
    List_of_letters = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""
    for ch in text:
        if ch in List_of_letters:
         for i, che in enumerate (List_of_letters):
           if ch in List_of_letters:
             if ch == che:
              index_of_list = List_of_letters[(i+num)%26]
              encrypted_text += index_of_list
        else: 
             encrypted_text += ch
    return encrypted_text



            
def Caesar2(text:str, num:int):
    List_of_letters = "abcdefghijklmnopqrstuvwxyz"
    Returned_text = ""
    for ch in text:
        if ch in List_of_letters:
         for i, che in enumerate (List_of_letters):
           if ch in List_of_letters:
             if ch == che:
              index_of_list = List_of_letters[(i-num)%26]
              Returned_text += index_of_list
        else: 
             Returned_text += ch
    return Returned_text




def fence(text:str):
   List_of_letters = "abcdefghijklmnopqrstuvwxyz"
   new_text = ""
   for ch in text:
      if ch in List_of_letters:
         new_text += ch


   text1 = ""
   text2 = ""
   for i, che in enumerate (new_text):
      if i%2 == 0:
         text1 += che
      else:
         text2 += che
   return text1 + text2


   
   


            
          


    
 
    






# def fence();
