p_str = input("Enter Principal amount: ")
r_str = input("Enter Rate of interest: ")
t_str = input("Enter Time in years: ")


p_num = float(p_str)
r_num = float(r_str)
t_num = float(t_str)

si_num = (p_num * r_num * t_num) / 100
total_num = p_num + si_num

print("Simple Interest (SI): " + str(si_num))
print("Total Amount: " + str(total_num))
