from utils.vectorOutput import generateOutputMatrixWithHeaders, writeOutputMatrix
from utils.nLixiviantUtils import Calculate_Lixiviant_Mass
from utils.specutils12 import ensure_dir




# ------------------------------------------------------------------------------------------------ #
# massCarbon: Mass of carbon to be sequestered (in grams of carbon). I'm going to put in the number
# corresponding to 20 GtCO2 per year
mCarbon = (12/44) * 20 * 1e15

# MWForsterite: Molecular weight of magnesium olivine (usually ≈ 140 grams per mole)
MWForsterite = 141

# MWCarbon: Molecular weight of just the carbon atom (12 grams per mole)
MWCarbon = 12

# nCarbonOlivine: Number of carbon atoms sequestered by dissolution of a single asymmetric unit 
# of olivine (2 at most)
nCarbonForsterite = 2


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

# Cost of solar electricity (Dollars per joule)
CelecSunShot = 8.3333e-9
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Next, let's calculate an optimistic and a pessimistic value for zeta
# zeta = Concentration of lixiviant in moles per cubic meter / 
# (extraction efficiency * precipitation efficiency * pulp density)

concentrationLixOpt = 100e-3
concentrationLixOptMolPerCubicMeter = concentrationLixOpt*1000

extractionEfficiencyVOptimistic = 1
precipitationEfficiencyVOptimistic = 1
densityPulpOptimistic = 50

zetaOptimistic = concentrationLixOptMolPerCubicMeter / \
(extractionEfficiencyVOptimistic * precipitationEfficiencyVOptimistic * 1e4 * densityPulpOptimistic)

concentrationLixPessim = 100e-3
concentrationLixPessimPerCubicMeter = concentrationLixPessim*1000

extractionEfficiencyPessimistic = 0.1
precipitationEfficiencyPessimistic = 1
densityPulpPessimistic = 10

zetaPessimistic = concentrationLixPessimPerCubicMeter / \
(extractionEfficiencyPessimistic * precipitationEfficiencyPessimistic * 1e4* densityPulpPessimistic)


# Print out the optmistic and pessimistic values of zeta
print("Optimistic estimate of zeta: " + str(zetaOptimistic))
print("Pessimistic estimate of zeta: " + str(zetaPessimistic))
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Now that we've got the way points for zeta, we can calculate the lixiviant mass for a wide 
# range of zeta values

zetaArray = logspace(-5, 0, num=50)

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

mLixArray_Ace_Gt = array(mLixArray_Ace)/1e15
mLixArray_Cit_Gt = array(mLixArray_Cit)/1e15
mLixArray_DKG_Gt = array(mLixArray_DKG)/1e15
mLixArray_Gluc_Gt = array(mLixArray_Gluc)/1e15
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
figure()
loglog(zetaArray, mLixArray_Ace_Gt, label='Acetic Acid')
loglog(zetaArray, mLixArray_Cit_Gt, label='Citric Acid')
loglog(zetaArray, mLixArray_DKG_Gt, label='2,5-DKG Acid')
loglog(zetaArray, mLixArray_Gluc_Gt, label='Gluconic Acid')

xlabel("Mineralization Efficiency, zeta (Moles per gram)")
ylabel("Lixiviant Mass Needed to Mineralized 20 GtCO2(Gigatonnes)")
grid()
legend()
show()
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Output the results of the code	

vectorList = [zetaArray, mLixArray_Ace_Gt, mLixArray_Cit_Gt, mLixArray_DKG_Gt, mLixArray_Gluc_Gt]
headers = ['Zeta', 'Acetic', 'Citric', 'DKG', 'Gluconic']

oMatrix = generateOutputMatrixWithHeaders(vectorList, headers, delimeter=',')

outputFileName = 'output/nLixiviant.csv'

ensure_dir(outputFileName)

writeOutputMatrix(outputFileName, oMatrix)
# ------------------------------------------------------------------------------------------------ #















