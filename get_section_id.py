def get_section_id(scroll, sizes):
    
    current_star = 0

    for index, size in enumerate(sizes):
        
        current_end = current_star + size
        if current_star <= scroll < current_end:
            return index
        current_star = current_end

    return -1
    



print(get_section_id(300, [300, 200, 400, 600, 100]))