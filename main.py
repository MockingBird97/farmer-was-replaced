CROPS = [
    [Entities.Grass, Items.Hay],
    [Entities.Bush, Items.Wood],
    [Entities.Carrot, Items.Carrot]
]

clear()

def goto(x, y):
    while get_pos_x() != tx or get_pos_y != ty:
        current_x = get_pos_x
        current_y = get_pos_y

        if tx >= current_x:
            x_direct = tx - current_x
        else:
            x_direct = current_x - tx

        if ty >= current_y:
            y_direct = ty - current_y
        else:
            y_direct = current_y - ty

        x_wrap = get_world_size() - x_direct
        y_wrap = get_world_size() - y_direct

        if x_direct <= x_wrap:
            if tx > current_x:
                move(East)
            elif tx < current_x:
                move(West)
        else:
            if tx > current_x:
                move(West)
            elif tx < current_x:
                move(East)

        if y_direct <= y_wrap:
            if ty > current_y:
                move(North)
            elif ty < current_y:
                move(South)
        else:
            if ty > current_y:
                move(South)
            elif ty < current_y:
                move(North)

def handle_cell(entity):
    if get_ground_type()!= Grounds.Soil:
        till()
    if get_water() < 0.5 and num_items(Items.Water) > 0:
        use_item(Items.Water)
    if entity == Entities.Bush and (get_pos_x() + get_pos_y()) % 2 == 0:
        entity = Entities.Tree
    if can_harvest():
        harvest()
    plant(entity)

def choose_plant():
    best = CROPS[0]
    best_count = num_items(best[1])
    for pair in CROPS:
        count = num_items(best[1])
        if count < best_count:
            best = pair
            best_count = count
    return best[0]

def main():
    while True:
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                goto(x, y)
                entity = choose_plant()
                handle_cell(entity)

main()

