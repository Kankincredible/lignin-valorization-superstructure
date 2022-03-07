# Parameters

#name of the feedstock and products
b= ["hardwood","softwood","harbacous"] #feedstock
fp = ["Lipid", "PHA", "Muconic_acid", "Vanillin"] #final product
ip1 = ["lignin", "hardwood","softwood","harbacous"] #intermediate products from fractionation to depolyermization
ip2 = ["monomers", "lignin"] #intermediate products from depolyermization to upgrading
bp = ["ethanol",...] #by-products


# name of the process
fra= [""] #fractionation
dpl=[""] #depolymerization
upg=[""] #upgrading


# feedstock_composition = ["Lignin", "Cellulose", "Hemicellulose"]

# feedstock_composition = {"Lignin": (0.1, 0.15),
#                        "Cellulose": (0.2, 0.25),
#                       "Hemicellulose": (0.2, 0.18)}

# the relationship of process
# 2-dimention; whether there is a connection or not
# for example, let b[0] represent hardwood, fra[0] represent RCF
# x_b_fra[0,0]=1 means there is a connection bewteen b[0](hardwood) and fra[0](RCF)
x_b_fra = np.array([[1,1,1],[1,1,1],[1,1,1]])
x_fra_dpl = np.array([[1,1,1],[1,1,1],[1,1,1]])
x_dpl_upg = np.array([[1,1,1],[1,1,1],[1,1,1]])
x_upg_fp = np.array([[1,0,0],[0,1,0],[0,0,1]])


# the relationship of process and products
# 1: there is a link; 0: there is no link

# from fractionation; 
# 3-dimention, y_fra[ip1,b,fra]
# for each ip1, whether it could come from b in fractionation. 
# for example, let ip1[0] represent lignin, b[0] represent hardwood, fra[0] represent RCF, fra[4] represent no process
# y_fra[0,0,0]=1 means ip[0](lignin) could come from b[0](hardwood) in fra[0](RCF)
# y_fra[0,0,4]=0 means ip[0](lignin) could not come from b[0](hardwood) in fra[4](no process)

y_fra = np.array([[[1,1,1],[0,...]],[[1,1,1],[0,...]]]) 

# from depolymerization; 
# 3-dimention, y_ip2_dpl[ip2,ip1,dpl]
# for each ip2, whether it could come from ip1 in depolymerziation. 
# for example, let ip2[0] represent monomer, ip2[1] represent lignin, ip1[0] represent lignin, dpl[4] represent no process
# y_dpl[0,0,4]=0 means ip2[0](monomer) could not come from ip1[0](lignin) after dpl[4] (no process)
# y_dpl[1,0,4]=0 means ip2[1](lignin) could come from ip1[0](lignin) after dpl[4] (no process)

y_dpl = np.array([[[1,1,1],[0,...]],[[1,1,1],[0,...]]]) 

# from upgrading
# 3-dimention, y_fp_upg[fp,ip2,upg]
# for each final product, whether it could come from the ip2 in upgrading. 
# for example, let fp[0] represent lipid, ip2[0] represent monomer, upg[1] represent fermenation(R opacus)
# y_upg[0,0,1]=1 means fp[0](lipid) could come from ip2[0](monomer) after upg[1] (fermenation(R opacus))

y_upg = np.array([[[1,1,1],[0,...]],[[1,1,1],[0,...]]]) 



# utility consumption of each process
u_fra = []
u_dpl = []
u_upg = []

# chemical consumption of each process
c_fra = []
c_dpl = []
c_upg = []

# yield
# 2-dimention, for each input, the yield of the process

# main product yield
theta_fra = np.array([[],[]]) #theta_fra[b,fra]
theta_dpl = np.array([[],[]]) #theta_dpl[ip1,dpl]
theta_upg = np.array([[],[]]) #theta_upg[ip2,upg]

# byproduct yield
phi_fra = np.array([[],[]]) #phi_fra[b,fra]
phi_dpl = np.array([[],[]]) #phi_dpl[ip1,dpl]
phi_upg = np.array([[],[]]) #phi_upg[ip2,upg]



# profit calculation
p_b = [] #feedstock price
p_BP_fra = [] #byproduct price of fractionation
p_BP_dpl = [] #byproduct price of depolymerization
p_BP_upg = [] #byproduct price of upgrading
p_fp = [] #final product price

p_u = 1 #utility price
p_c = 1 #additional chemical price
p_w = 1 #waste treatment unit price

# capital cost on the base of Q=1000
Cost_fra=[] # capital cost of fractionation 
Cost_dpl=[] # capital cost of depolymerization
Cost_upg=[] # capital cost of upgrading


#time value of money
tax=
t=5   #time
ir=   #interest rate
d=   #depreciation

#quantity of the feedstock
Q = 1000