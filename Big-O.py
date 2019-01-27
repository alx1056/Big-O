#Big-O notation algorithms

#O(n)
list_1 = ("squash", "asparugus", "kale")

def item_in_list(to_check, the_list):
    for item in the_list:
        if to_check == item:
          return print("That item is in your list!")
    return print("That item is not in your list!!!")

item_in_list("squash", list_1)






#O(n^2)
list_2 = [1,2,3]

def all_combinations(the_list):
   results = []
   for item in the_list:
       for inner_item in the_list:
           results.append((item, inner_item))
   return results



one = all_combinations(list_2)