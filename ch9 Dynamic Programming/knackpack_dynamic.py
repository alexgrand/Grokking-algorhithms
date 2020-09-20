items = {}
items['guitar'] = {}
items['guitar']['cost'] = 1500
items['guitar']['weight'] = 1
items['stereo'] = {}
items['stereo']['cost'] = 3000
items['stereo']['weight'] = 4
items['laptop'] = {}
items['laptop']['cost'] = 2000
items['laptop']['weight'] = 3
items['iphone'] = {}
items['iphone']['cost'] = 2000
items['iphone']['weight'] = 1
items['mp3'] = {}
items['mp3']['cost'] = 1000
items['mp3']['weight'] = 1


def knackpack(items, pounds):
    cells = {}
    row = 1

    for item in items:
        cells[row] = {}

        i_cost = items[item]['cost']
        i_weight = items[item]['weight']

        for col in range(1, pounds + 1):
            cell_weight = col
            cells[row][col] = {}
            cells[row][col]['cost'] = 0
            cells[row][col]['items'] = []

            if row == 1 and i_weight <= cell_weight:
                cells[row][col]['cost'] = i_cost
                cells[row][col]['items'] = [item]
                continue
            
            elif i_weight <= cell_weight:
                old_cost = cells[row - 1][col]['cost']
                new_cost = i_cost
                weight_dif = cell_weight - i_weight

                if weight_dif == 0 and new_cost > old_cost:
                    cells[row][col]['cost'] = new_cost
                    cells[row][col]['items'] = [item]
                elif weight_dif >=1:
                    new_cost += cells[row - 1][weight_dif]['cost']
                    
                    if new_cost > old_cost:
                        cells[row][col]['cost'] = new_cost
                        cells[row][col]['items'] += [item]
                        cells[row][col]['items'] += cells[row - 1][weight_dif]['items']
                    else:
                        cells[row][col]['cost'] = old_cost
                        cells[row][col]['items'] = cells[row - 1][col]['items']
                else:
                    cells[row][col]['cost'] = old_cost
                    cells[row][col]['items'] = cells[row - 1][col]['items']

            else:
                cells[row][col]['cost'] = cells[row - 1][col]['cost']
                cells[row][col]['items'] = cells[row - 1][col]['items']

                
        row += 1
    return cells



def print_knackpack():
    global items

    cells = knackpack(items, 4)
    items_keys = list(items.keys())
    i = 0

    for cell in cells:
        print(f"\n---row_{cell}---({items_keys[i]})\n")
        for col in cells[cell]:
            print(f"\t---col_{col}---")
            print(f"\t\t{cells[cell][col]}")
        i += 1


print_knackpack()