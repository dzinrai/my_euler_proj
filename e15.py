from collections import deque

quads = []
quad1 = [[0,0,0],
         [0,0,0],
         [0,0,0]]
quad1_temp = [[0,0,0],
              [0,0,0],
              [0,0,0]]

all_routs = []

def draw_right_route(quad,enter=[0,0]):

    qi = enter[0]
    qj = enter[1]

    next_q = deque()
    #next_q += [qi,qj]
    next_q.appendleft([qi,qj])

    print("next_q=",next_q)
    pathed = []
    while next_q:
        print("before pop next_q=", next_q)
        cell = next_q.popleft()
        print("next_q=",next_q)
        print("cell=", cell)
        #i = input()
        print("pathed=", pathed)
        if not cell in pathed:
            pathed.append(cell)
            print("pathed=", pathed)
            if cell[0] < len(quad)-1:
                next_q.appendleft([cell[0]+1,cell[1]])

            if cell[1] < len(quad)-1:
                next_q.appendleft([cell[0],cell[1]+1])


            if cell[0] == len(quad)-1 and cell[1] == len(quad)-1:
                print("end pathed=", pathed,"qi and qj=",qi,qj)
                next_q.appendleft([qi, qj])
                pathed.append(cell)
                all_routs.append(pathed)
                return True

    return False


#draw_right_route(quad1, [0, 0])
#print(all_routs)

marchs = []
# [[0,0],[0,0]]
def draw_marchs(quad,e=[0,0]):
    route = []
    cell = e
    cell_next = []
    reverse_bool = False
    while True:
        i = input()
        print('reverse_bool ={}'.format(reverse_bool))
        if route == []:
            route.append(cell)
        else:
            cell = route[-1]
            if cell[0]+1==len(quad)-1 and cell[1]+1==len(quad)-1:
                print('маршрут окончен')
                route = []
                cell = [0,0]
                cell_next = []
                if reverse_bool:
                    reverse_bool = False
                    print('reverse_bool ={}'.format(reverse_bool))
                else:
                    reverse_bool = True
                    print('reverse_bool ={}'.format(reverse_bool))
            else:
                if reverse_bool:
                    if cell[0]+1<len(quad)-1:
                        cell_next = [cell[0] + 1, cell[1]]
                        route.append(cell_next)
                    else:
                        reverse_bool = False
                        print('reverse_bool ={}'.format(reverse_bool))
                else:
                    if cell[1]+1<len(quad)-1:
                        cell_next = [cell[0], cell[1] + 1]
                        route.append(cell_next)
                    else:
                        reverse_bool = True
                        print('reverse_bool ={}'.format(reverse_bool))

        print('cell ={} cell_next ={}'.format(cell,cell_next))
        if not route in marchs:
            marchs.append(route)

        print('route ={} marchs ={}'.format(route,marchs))
        # route = [[0,0]]
        #marchs = [[[0,0]]]





    print(marchs)
    return False

draw_marchs(quad1)