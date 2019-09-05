from matplotlib import pyplot as plt
import json

if __name__ == '__main__':
    with open('9 nov 12 shift.json') as f:
        employees = json.loads(f.read())

    with open('9 nov 12 dm.json') as f:
        distance_matrix = json.loads(f.read())

        cab_types = ['INDICA', 'SUMO', 'TRAVELLER']
    price = [15, 15, 20]
    with open('9 nov 12 h2o.json') as f:
        home_to_office_dist = json.loads(f.read())
    employee_count = len(employees)


    def get_seat(cab):
        if cab is 'INDICA':
            return 4
        elif cab is 'SUMO':
            return 6
        else:
            return 12





    def get_cab(n):
        if n <= 4:
            return 'INDICA'
        elif n <= 6:
            return 'SUMO'
        else:
            return 'TRAVELLER'
    def cab_occupancy(poools):
        # pool_count_with_types
        empcnt = 0
        pool_cnts = {}
        for pool in poools:
            if len(pool) not in pool_cnts:
                pool_cnts[len(pool)] = 0
            pool_cnts[len(pool)] += 1
        ret = [0, 0, 0]
        for k, val in pool_cnts.items():
            print("{}           => {}".format(str(k), str(val)))
            if k <= 4:
                ret[0] += k * val
            elif k <= 6:
                ret[1] += k * val
            else:
                ret[2] += k * val
        return ret


    def cab_occupancy(poools):
        # pool_count_with_types
        empcnt = 0
        pool_cnts = {}
        for pool in poools:
            if len(pool) not in pool_cnts:
                pool_cnts[len(pool)] = 0
            pool_cnts[len(pool)] += 1
        ret = [0, 0, 0]
        for k, val in pool_cnts.items():
            print("{}           => {}".format(str(k), str(val)))
            if k <= 4:
                ret[0] += k * val
            elif k <= 6:
                ret[1] += k * val
            else:
                ret[2] += k * val
        return ret


    def droute_dist(pool, employee_dists, employee_droute, employee_cabs):
        rev = pool[::-1]
        cur = rev[0]
        idd = employees.index(cur)
        total_dist = home_to_office_dist[idd]
        employee_dists[idd] = total_dist
        employee_droute[idd] = 1
        droutes = [1]
        cab = get_cab(len(pool))
        employee_cabs[idd] = cab
        for pick in rev[1:]:
            idx = employees.index(cur)
            p = employees.index(pick)
            dis = distance_matrix[p][idx]
            total_dist += dis
            x = home_to_office_dist[p]
            droute = (total_dist * 1.0) / x
            cur = pick
            employee_dists[p] = total_dist
            employee_droute[p] = droute
            employee_cabs[p] = cab
            droutes.append(droute)
        return max(droutes), total_dist


    with open('result 9 nov 12.json') as f:
        our_result = json.loads(f.read())
    our_pools = [list(map(lambda i: employees[i], pool)) for pool in our_result]
    our_count = len(our_pools)
    our_cabs = list(map(lambda pool: get_cab(len(pool)), our_pools))
    our_cab_count = [our_cabs.count('INDICA'), our_cabs.count('SUMO'), our_cabs.count('TRAVELLER')]

    our_cab_wise_droutes = [[], [], []]
    our_cab_wise_dists = [0, 0, 0]
    our_employee_wise_droute = [0] * employee_count
    our_employee_wise_dists = [0] * employee_count
    our_employee_wise_cabs = [''] * employee_count
    for pool in our_pools:
        droute, total_dist = droute_dist(pool, our_employee_wise_dists, our_employee_wise_droute,
                                         our_employee_wise_cabs)
        if len(pool) <= 4:
            i = 0
        elif len(pool) <= 6:
            i = 1
        else:
            i = 2
        our_cab_wise_droutes[i].append(droute)
        our_cab_wise_dists[i] += total_dist

    their_pools = []
    prev = employees[0]
    cur = [prev]
    for emp in employees[1:]:
        if prev['Serial No.'] >= emp['Serial No.']:
            their_pools.append(cur)
            prev = emp
            cur = [emp]
        else:
            cur.append(emp)

    if cur:
        their_pools.append(cur)

    their_count = len(their_pools)
    their_cabs = list(map(lambda pool: get_cab(len(pool)), their_pools))
    their_cab_count = [their_cabs.count('INDICA'), their_cabs.count('SUMO'), their_cabs.count('TRAVELLER')]

    their_cab_wise_droutes = [[], [], []]
    their_cab_wise_dists = [0, 0, 0]
    their_employee_wise_droute = [0] * employee_count
    their_employee_wise_dists = [0] * employee_count
    their_employee_wise_cabs = [''] * employee_count
    for pool in their_pools:
        droute, total_dist = droute_dist(pool, their_employee_wise_dists, their_employee_wise_droute,
                                         their_employee_wise_cabs)
        if len(pool) <= 4:
            i = 0
        elif len(pool) <= 6:
            i = 1
        else:
            i = 2
        their_cab_wise_droutes[i].append(droute)
        their_cab_wise_dists[i] += total_dist

    their_stats = {}
    our_stats = {}

    print("Their Cab Stats")
    their_stats['cab_count'] = {}
    for tp, cnt in zip(cab_types, their_cab_count):
        their_stats['cab_count'][tp] = cnt
        print('{} :{}'.format(tp, cnt))

    print("Our Cab Stats")
    our_stats['cab_count'] = {}
    for tp, cnt in zip(cab_types, our_cab_count):
        our_stats['cab_count'][tp] = cnt
        print('{} :{}'.format(tp, cnt))
    print()

    print("~~~~~~~~~~~~~~~~~~TOTAL DISTANCE COVERED BY THEM FOR DIFFERENT CAB TYPES~~~~~~~~~~~~~~~~~")
    their_stats['cab_wise_distance'] = {}
    for tp, dist in zip(cab_types, their_cab_wise_dists):
        print('{} :{}'.format(tp, dist / 1000.0))
        their_stats['cab_wise_distance'][tp] = dist / 1000.0

    print("~~~~~~~~~~~~~~~~~~TOTAL DISTANCE COVERED BY US FOR DIFFERENT CAB TYPES~~~~~~~~~~~~~~~~~")
    our_stats['cab_wise_distance'] = {}
    for tp, dist in zip(cab_types, our_cab_wise_dists):
        print('{} :{}'.format(tp, dist / 1000.0))
        our_stats['cab_wise_distance'][tp] = dist / 1000.0

    print("~~~~~~~~~~~~~~~~~~AVERAGE DISTANCE COVERED BY THEIR SINGLE CAB OF DIFFERENT TYPES~~~~~~~~~~~~~~~~~")
    their_stats['cab_wise_avg_distance'] = {}
    for i in range(3):
        pass
        print('{} :{}'.format(cab_types[i], their_cab_wise_dists[i] / (1000.0 * their_cab_count[i])))
        their_stats['cab_wise_avg_distance'][cab_types[i]] = their_cab_wise_dists[i] / (1000.0 * their_cab_count[i])

    print("~~~~~~~~~~~~~~~~~~AVERAGE DISTANCE COVERED BY OUR SINGLE CAB OF DIFFERENT TYPES~~~~~~~~~~~~~~~~~")
    our_stats['cab_wise_avg_distance'] = {}
    for i in range(3):
        print('{} :{}'.format(cab_types[i], our_cab_wise_dists[i] / (1000.0 * our_cab_count[i])))
        our_stats['cab_wise_avg_distance'][cab_types[i]] = our_cab_wise_dists[i] / (1000.0 * our_cab_count[i])

    print("~~~~~~~~~~~~~~~~~~TOTAL Price Paid by THEM For DIFFERENT CAB TYPES~~~~~~~~~~~~~~~~~")
    their_stats['cab_type_price'] = {}
    their_total_price = 0
    for i in range(3):
        prc = price[i] * (their_cab_wise_dists[i] / 1000.0)
        print('{} :{}'.format(cab_types[i], prc))
        their_stats['cab_type_price'][cab_types[i]] = prc
        their_total_price += prc
    their_stats['total_price'] = their_total_price
    print('Their Total Price: :{}'.format(their_total_price))

    print("~~~~~~~~~~~~~~~~~~TOTAL Price Paid By us For DIFFERENT CAB TYPES~~~~~~~~~~~~~~~~~")
    our_total_price = 0
    our_stats['cab_type_price'] = {}
    for i in range(3):
        prc = price[i] * (our_cab_wise_dists[i] / 1000.0)
        our_stats['cab_type_price'][cab_types[i]] = prc
        print('{} :{}'.format(cab_types[i], prc))
        our_total_price += prc
    our_stats['total_price'] = our_total_price
    print('Our Total Price: :{}'.format(our_total_price))

    price_efficiency = their_total_price / our_total_price - 1
    print("Price Efficiency: {}".format(price_efficiency))

    print("~~~~~~~~~~~~~~~~~~Their Cab wise average droutes~~~~~~~~~~~~~~~~~")
    their_stats['cab_wise_avg_droutes'] = {}
    for typ, droutes in zip(cab_types, their_cab_wise_droutes):
        print("{}:     {}".format(typ, sum(droutes) / len(droutes)))
        their_stats['cab_wise_avg_droutes'][typ] = sum(droutes) / len(droutes)

    print("~~~~~~~~~~~~~~~~~~Our Cab wise average droutes~~~~~~~~~~~~~~~~~")
    our_stats['cab_wise_avg_droutes'] = {}
    for typ, droutes in zip(cab_types, our_cab_wise_droutes):
        print("{}:     {}".format(typ, sum(droutes) / len(droutes)))
        our_stats['cab_wise_avg_droutes'][typ] = sum(droutes) / len(droutes)

    print("Cab Type: INDICA")
    plt.bar(range(len(their_cab_wise_droutes[0])), their_cab_wise_droutes[0])
    plt.show()
    print("Cab Type: SUMO")
    plt.bar(range(len(their_cab_wise_droutes[1])), their_cab_wise_droutes[1])
    plt.show()
    print("Their pool size:     people count")
    their_occupancy = cab_occupancy(their_pools)

    print("our Occupancy")
    our_stats['occupancy'] = {}
    our_stats['people_by_cab'] = {}
    for i in range(3):
        our_stats['people_by_cab'][cab_types[i]] = our_occupancy[i]
        our_stats['occupancy'][cab_types[i]] = our_occupancy[i] / (get_seat(cab_types[i]) * our_cab_count[i])
        print("CAB TYPE: {}       => {}".format(cab_types[i],
                                                our_occupancy[i] / (get_seat(cab_types[i]) * our_cab_count[i])))


    print("Their Occupancy")
    their_stats['occupancy'] = {}
    their_stats['people_by_cab'] = {}
    for i in range(3):
        their_stats['people_by_cab'][cab_types[i]] = their_occupancy[i]
        their_stats['occupancy'][cab_types[i]] = their_occupancy[i] / (get_seat(cab_types[i]) * their_cab_count[i])
        print("CAB TYPE: {}       => {}".format(cab_types[i],
                                                their_occupancy[i] / (get_seat(cab_types[i]) * their_cab_count[i])))

    print("Employee Wise droute:Ours-Red, Theirs-Blue")
    plt.bar(range(len(their_employee_wise_droute)), their_employee_wise_droute)
    plt.bar(range(len(our_employee_wise_droute)), our_employee_wise_droute, color='red')

    good = 0
    for i in range(len(employees)):
        if their_employee_wise_droute[i] >= our_employee_wise_droute[i]:
            good += 1
    print("Employee Wise Distance: Ours:Red, Theirs: Blue")
    plt.bar(range(len(their_employee_wise_dists)), their_employee_wise_dists)
    plt.bar(range(len(our_employee_wise_dists)), our_employee_wise_dists, color='red')



    '''with open('our 9 nov 12.json', 'w') as f:
        f.write(json.dumps(our_stats))
    with open('their 9 nov 12.json', 'w') as f:
        f.write(json.dumps(their_stats))'''
