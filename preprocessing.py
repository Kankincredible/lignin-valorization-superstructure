# Compute key parameters of MIP model formulation


# number of the feedstock, final products and intermediate products
num_b = len(b)
num_fp = len(fp)
num_ip1 = len(ip1)
num_ip1 = len(ip2)


# compute the number of process at each stage
num_fra = len(fra)
num_dpl = len(dpl)
num_upg = len(upg)

# Define the dimension of the flow (continuous) variables by the indexes

# fractionation
# inlet flow, utility, additional chemical, byrpoduct flow and waste
prod_fra = list(product(range(num_b), range(num_fra)))
# outlet flow
prodout_fra = list(product(range(num_fra), range(num_ip1)))

# depolymerization
# inlet flow, utility, additional chemical, byrpoduct flow and waste
prod_dpl = list(product(range(num_ip1), range(num_dpl)))
# outlet flow
prodout_dpl = list(product(range(num_dpl), range(num_ip2)))

# upgrading
# inlet flow, utility, additional chemical, byrpoduct flow and waste
prod_upg = list(product(range(num_ip2), range(num_upg)))
# outlet flow
prodout_upg = list(product(range(num_upg), range(num_fp)))
