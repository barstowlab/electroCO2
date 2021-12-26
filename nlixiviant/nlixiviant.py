from utils.vectorOutput import generateOutputMatrix, writeOutputMatrix
from utils.nLixiviantUtils import Calculate_Lixiviant_Mass_with_Unknown_Quantities
from utils.specutils12 import ensure_dir
	
# ------------------------------------------------------------------------------------------------ #
# Here we will run an actual calculation

# massCarbon: Mass of carbon to be sequestered (in gigatonnes of carbon)
massCarbon = 10

# MWOlivine: Molecular weight of olivine (usually ≈ 140 grams per mole)
MWOlivine = 140

# MWLix: Molecular weight of the lixiviant (for gluconic acid, this 196 grams per mole)
MWLix = 196

# MWCarbon: Molecular weight of just the carbon atom (12 grams per mole)
MWCarbon = 12

# nCarbonOlivine: Number of carbon atoms sequestered by dissolution of a single asymmetric unit 
# of olivine (2 at most)
nCarbonOlivine = 2

# densityOlivine: Density of olivine (usually 2.5 x 10^6 grams per cubic meter)
densityOlivine = 2.5e6


# Next, let's calculate an optimistic and a pessimistic value for zeta
# zeta = Concentration of lixiviant in moles per cubic meter / 
# (extraction efficiency * precipitation efficiency * pulp density)

concentrationLixOpt = 25e-3
concentrationLixOptMolPerCubicMeter = concentrationLixOpt*1000

extractionEfficiencyVOptimistic = 1
precipitationEfficiencyVOptimistic = 1
densityPulpOptimistic = 0.3

zetaOptimistic = concentrationLixOptMolPerCubicMeter / \
(extractionEfficiencyVOptimistic * precipitationEfficiencyVOptimistic * densityPulpOptimistic)

concentrationLixPessim = 1000e-3
concentrationLixPessimPerCubicMeter = concentrationLixPessim*1000

extractionEfficiencyPessimistic = 0.01
precipitationEfficiencyPessimistic = 0.01
densityPulpPessimistic = 0.1

zetaPessimistic = concentrationLixPessimPerCubicMeter / \
(extractionEfficiencyPessimistic * precipitationEfficiencyPessimistic * densityPulpPessimistic)


# Print out the optmistic and pessimistic values of zeta
print("Optimistic estimate of zeta: " + str(zetaOptimistic))
print("Pessimistic estimate of zeta: " + str(zetaPessimistic))


# Now that we've got the way points for zeta, we can calculate the lixiviant mass for a wide 
# range of zeta values

#zetaArray = arange(1, 100000000, 10)
zetaArray = logspace(0, 8, num=50)

mLixArray = []

i = 0
while i < len(zetaArray):

	zeta = zetaArray[i]
	
	mLixGigatonnes = \
	Calculate_Lixiviant_Mass_with_Unknown_Quantities(massCarbon, MWOlivine, MWLix, \
	MWCarbon, nCarbonOlivine, densityOlivine, zeta)
	
	
	mLixArray.append(mLixGigatonnes)
	
	i += 1

# ------------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------------ #
figure()
loglog(zetaArray, mLixArray)
xlabel("Zeta")
ylabel("Lixiviant Mass (Gigatonnes)")



# ------------------------------------------------------------------------------------------------ #



# ------------------------------------------------------------------------------------------------ #
# Output the results of the code	

vectorList = [zetaArray, mLixArray]

oMatrix = generateOutputMatrix(vectorList, delimeter=',')

outputFileName = 'output/nLixiviant.csv'

ensure_dir(outputFileName)

writeOutputMatrix(outputFileName, oMatrix)
# ------------------------------------------------------------------------------------------------ #















