def binary_search(a_list, an_item):
    first = 0
    last= len(a_list) -1

    while first <= last:
        mid_point = (first + last ) //2
        if a_list [mid_point] == an_item:
            return True
        else:
            if an_item < a_list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1
    return False

def binary_search_rec(a_list, first, last, an_item):
    if len(a_list) == 0:
            return False
    else:
         mid_point = (first + last) //2
         if a_list[mid_point] == an_item:
              return True
         else:
              if an_item < a_list[mid_point]:
                   last = mid_point - 1
                   return binary_search_rec(a_list, first, last, an_item)
              else:
                   first = mid_point + 1
                   return binary_search_rec(a_list, first, last, an_item)
    print('binary_search:', binary_search(a_list, 4))
    print('binary_search_recursive:',binary_search_rec(a_list, 0, len(a_list) -1, 4))