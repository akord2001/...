lisr2=[1,2,3]
lisr3=[1,2,3,4]
def sublist(lisr2,lisr3):
    xyz="".join(str(i)for i in lisr2)
    xs="".join(str(i)for i in lisr3)
    if xyz in xs or xs in xyz:
        print ("essa")
    else:
        print("JD")
sublist(lisr2,lisr3)

    