from utils.vectorOutput import generateOutputMatrixWithHeaders, writeOutputMatrix
from utils.nLixiviantUtils import Calculate_Lixiviant_Mass
from utils.specutils12 import ensure_dir

# ------------------------------------------------------------------------------------------------ #
zetaArray = logspace(-5, 0, num=50)
zetaArray = list(zetaArray)
zetaArray += [2e-4, 2.23e-4, 1.06e-3, 3.18e-3, 6.36e-3, 1.27e-2]

# Mass of carbon to be sequestered (in grams), in this case it corresponds to 1 tonne of CO2. 
mCarbon = (12/44)*1e6

# Acids, Calvin Cycle, H2 cost (Joules per gram)
CELix_Acetic_CBB_H2 = 35347.3205864527
CELix_Citric_CBB_H2 = 25110.1714595505
CELix_DKG_CBB_H2 = 30290.4975815907
CELix_Gluconic_CBB_H2 = 31479.7166818576

# Molecular weights of acids
MW_Ace = 60.052
MW_Cit = 192.124
MW_DKG = 191.12
MW_Gluc = 196.16

# MWForsterite: Molecular weight of magnesium olivine (usually ≈ 140 grams per mole)
MWForsterite = 141

# MWCarbon: Molecular weight of just the carbon atom (12 grams per mole)
MWCarbon = 12


# nCarbonOlivine: Number of carbon atoms sequestered by dissolution of a single asymmetric unit 
# of olivine (2 at most)
nCarbonForsterite = 2


# Cost of solar electricity (Dollars per joule)
CelecSunShot = 8.3333e-9

[mLixArray_Ace, totalCostELixArray_Ace, totalDollarCostArray_Ace] = \
Calculate_Lixiviant_Mass(mCarbon, MW_Ace, zetaArray, CELix_Acetic_CBB_H2, CelecSunShot, \
MWCarbon=MWCarbon, MWForsterite=MWForsterite, nCarbonForsterite=nCarbonForsterite)

[mLixArray_Cit, totalCostELixArray_Cit, totalDollarCostArray_Cit] = \
Calculate_Lixiviant_Mass(mCarbon, MW_Cit, zetaArray, CELix_Citric_CBB_H2, CelecSunShot, \
MWCarbon=MWCarbon, MWForsterite=MWForsterite, nCarbonForsterite=nCarbonForsterite)

[mLixArray_DKG, totalCostELixArray_DKG, totalDollarCostArray_DKG] = \
Calculate_Lixiviant_Mass(mCarbon, MW_DKG, zetaArray, CELix_DKG_CBB_H2, CelecSunShot, \
MWCarbon=MWCarbon, MWForsterite=MWForsterite, nCarbonForsterite=nCarbonForsterite)

[mLixArray_Gluc, totalCostELixArray_Gluc, totalDollarCostArray_Gluc] = \
Calculate_Lixiviant_Mass(mCarbon, MW_Gluc, zetaArray, CELix_Gluconic_CBB_H2, CelecSunShot, \
MWCarbon=MWCarbon, MWForsterite=MWForsterite, nCarbonForsterite=nCarbonForsterite)
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
figure()
loglog(zetaArray, mLixArray_Ace, label='Acetic')
loglog(zetaArray, mLixArray_Cit, label='Citric')
loglog(zetaArray, mLixArray_DKG, label='DKG')
loglog(zetaArray, mLixArray_Gluc, label='Gluconic')

grid()
legend()
xlabel("Zeta (Moles per gram)")
ylabel("Lixiviant Mass (grams)")
show()
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
figure()
loglog(zetaArray, totalCostELixArray_Ace, label='Acetic')
loglog(zetaArray, totalCostELixArray_Cit, label='Citric')
loglog(zetaArray, totalCostELixArray_DKG, label='DKG')
loglog(zetaArray, totalCostELixArray_Gluc, label='Gluconic')

grid()
legend()
xlabel("Zeta (Moles per gram)")
ylabel("Total Electricity Cost (Joules)")
show()
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
figure()
loglog(zetaArray, totalDollarCostArray_Ace, label='Acetic')
loglog(zetaArray, totalDollarCostArray_Cit, label='Citric')
loglog(zetaArray, totalDollarCostArray_DKG, label='DKG')
loglog(zetaArray, totalDollarCostArray_Gluc, label='Gluconic')

grid()
legend()
xlabel("Zeta (Moles per gram)")
ylabel("Total Electricity Cost (Dollars)")
show()
# ------------------------------------------------------------------------------------------------ #



# ------------------------------------------------------------------------------------------------ #
# Output the results of the code	

vectorList = [zetaArray, \
totalCostELixArray_Ace, totalCostELixArray_Cit, totalCostELixArray_DKG, totalCostELixArray_Gluc, \
totalDollarCostArray_Ace, totalDollarCostArray_Cit, totalDollarCostArray_DKG, \
totalDollarCostArray_Gluc\
]

headers = ['zeta', 'CELix_Ace', 'CELix_Cit', 'CELix_DKG', 'CELix_Gluc', \
'Dollar_Ace', 'Dollar_Cit', 'Dollar_DKG', 'Dollar_Gluc' ]

oMatrix = generateOutputMatrixWithHeaders(vectorList, headers, delimeter=',')

outputFileName = 'output/cLixiviant.csv'

ensure_dir(outputFileName)

writeOutputMatrix(outputFileName, oMatrix)
# ------------------------------------------------------------------------------------------------ #

