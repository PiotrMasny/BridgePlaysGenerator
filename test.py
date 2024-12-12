
def sub_tab(tab: list):
    sub_sub_tab = []
    for i in range(0, 5):
        sub_sub_tab.append(i)
    tab.append(sub_sub_tab)


tab = []
for i in range(0, 100):
    sub_tab(tab)

print(tab)