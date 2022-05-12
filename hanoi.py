# import sys
#
#
# def create_pre(disk_index, from_peg, to_peg):
#     disk_on_from_peg = ["d_" + str(disk_index) + from_peg]
#     others_not_on_from_peg = []
#     others_not_on_to_peg = []
#     d_on_d = []
#     for i in range(disk_index):
#         others_not_on_from_peg.append("d_" + str(i) + from_peg)
#         others_not_on_to_peg.append("d_" + str(i) + to_peg)
#         # for j in range(i+1, disk_index):
#
#
#     all_pres = disk_on_from_peg + others_not_on_from_peg + others_not_on_to_peg
#
#     all_pres_string = ' '.join(all_pres)
#     return all_pres_string
#
#
# def create_domain_file(domain_file_name, n_, m_):
#     disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
#     pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
#     domain_file = open(domain_file_name,
#                        'w')  # use domain_file.write(str) to write to domain_file
#     "*** YOUR CODE HERE ***"
#     domain_file.write("Propositions:\n")
#     disks_on_pegs_list = []
#     disks_not_on_pegs_list = []
#     disks_on_disks = []
#     # for single_disk in disks:
#     for first_disk in range(n):
#         for single_peg in pegs:
#             disks_on_pegs_list.append(disks[first_disk] + single_peg)
#             # disks_not_on_pegs_list.append("n" + single_disk + single_peg)
#         for second_disk in range(first_disk+1,n):
#                 disks_on_disks.append(disks[first_disk] + disks[second_disk])
#
#     domain_file.write(' '.join(disks_on_pegs_list + disks_not_on_pegs_list + disks_on_disks) + '\n')
#
#     domain_file.write("Actions:\n")
#     for disk_index in range(n):
#         for p0 in pegs:
#             for p1 in pegs:
#                 if p0!= p1:
#                     name = "Name: " + "M" + "d_" + str(disk_index) + p0 + p1 + "\n"
#                     pre = "pre: " + create_pre(disk_index, p0, p1) + "\n"
#                     add = "add: " + "d_" + str(disk_index) + p1 + "\n"
#                     delete = "delete: " + "d_" + str(disk_index) + p0 + "\n"
#                     action = name + pre + add + delete
#                     domain_file.write(action)
#
#     domain_file.close()
#
#
# def create_problem_file(problem_file_name_, n_, m_):
#     disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
#     pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
#     problem_file = open(problem_file_name_,
#                         'w')  # use problem_file.write(str) to write to problem_file
#     "*** YOUR CODE HERE ***"
#
#     problem_file.close()
#
#
# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         print('Usage: hanoi.py n m')
#         sys.exit(2)
#
#     n = int(float(sys.argv[1]))  # number of disks
#     m = int(float(sys.argv[2]))  # number of pegs
#
#     domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
#     problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)
#
#     create_domain_file(domain_file_name, n, m)
#     create_problem_file(problem_file_name, n, m)


import sys


def create_pre(disk_index, from_peg, to_peg):
    disk_on_from_peg = ["d_" + str(disk_index) + from_peg]
    others_not_on_from_peg = []
    others_not_on_to_peg = []
    for i in range(disk_index):
        others_not_on_from_peg.append("d_" +  str(i) + "notON" +from_peg)
        others_not_on_to_peg.append("d_"  + str(i) + "notON"+ to_peg)

    all_pres = disk_on_from_peg + others_not_on_from_peg + others_not_on_to_peg
    all_pres_string = ' '.join(all_pres)
    return all_pres_string


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    "*** YOUR CODE HERE ***"
    domain_file.write("Propositions:\n")
    disks_on_pegs_list = []
    disks_not_on_pegs_list = []
    for single_disk in disks:
        for single_peg in pegs:
            disks_on_pegs_list.append(single_disk + single_peg)
            disks_not_on_pegs_list.append(single_disk + "notON" + single_peg)
    domain_file.write(' '.join(disks + pegs + disks_on_pegs_list + disks_not_on_pegs_list) + '\n')

    domain_file.write("Actions:\n")
    for disk_index in range(n):
        for p0 in pegs:
            for p1 in pegs:
                if p0 != p1:
                    name = "Name: " + "M" + "d_" + str(disk_index) + p0 + p1 + "\n"
                    pre = "pre: " + create_pre(disk_index, p0, p1) + "\n"
                    add = "add: " + "d_" + str(disk_index) + p1 + " " + "d_" + str(disk_index) + "notON" + p0 + "\n"
                    delete = "delete: " + "d_" + str(disk_index) + p0 + " " + "d_" + str(disk_index) + "notON" + p1 + "\n"
                    action = name + pre + add + delete
                    domain_file.write(action)
    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_,
                        'w')  # use problem_file.write(str) to write to problem_file
    "*** YOUR CODE HERE ***"
    init_lst = []
    problem_file.write("Initial state: ")
    for disk_index in range(n):

    problem_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)
