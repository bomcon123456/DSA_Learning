def towerOfHanoi(disks, frm, to, tmp):
    if disks == 1:
        print("Move disk 1 from {} to {}".format(frm, to))
        return
    towerOfHanoi(disks - 1, frm, tmp, to)
    print("Move disk {} from {} to {}".format(disks, frm, to))
    towerOfHanoi(disks - 1, tmp, to, frm)


towerOfHanoi(4, "A", "C", "B")

