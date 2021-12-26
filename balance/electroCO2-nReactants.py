from utils.vectorOutput import generateOutputMatrixWithHeaders, writeOutputMatrix
from utils.specutils12 import GenerateFileList
import pdb
from utils.balanceUtils import ImportStoichiometricMatrix, BalanceStoichiometricMatrix, \
PrintStoichiometry


directory = 'input/ElectroCO2 Stoichiometric Matrices/'
outputFileName = 'output/electroCO2-nReactants.csv'




fileList = [\
'Acetic-Acetic_3HP.csv', \
'Acetic-Acetic_3HP4HB.csv', \
'Acetic-Acetic_4HB.csv', \
'Acetic-Acetic_CBB.csv', \
'Acetic-Acetic_FORM.csv', \
'Acetic-Acetic_RTCA.csv', \
'Acetic-Acetic_WL.csv', \
'Citric-Citric_3HP.csv', \
'Citric-Citric_3HP4HB.csv', \
'Citric-Citric_4HB.csv', \
'Citric-Citric_CBB.csv', \
'Citric-Citric_FORM.csv', \
'Citric-Citric_RTCA.csv', \
'Citric-Citric_WL.csv', \
'DKG-DKG_3HP.csv', \
'DKG-DKG_3HP4HB.csv', \
'DKG-DKG_4HB.csv', \
'DKG-DKG_CBB.csv', \
'DKG-DKG_FORM.csv', \
'DKG-DKG_RTCA.csv', \
'DKG-DKG_WL.csv', \
'Gluc-Gluconate_3HP.csv', \
'Gluc-Gluconate_3HP4HB.csv', \
'Gluc-Gluconate_4HB.csv', \
'Gluc-Gluconate_CBB.csv', \
'Gluc-Gluconate_FORM.csv', \
'Gluc-Gluconate_RTCA.csv', \
'Gluc-Gluconate_WL.csv' \
]


# regText = r'.*\.csv'
# regText = r'.*\_CBB\.csv'

reactantsToGet = ['ATP', 'NADH', 'Fdred', 'Sulfate', 'CO2', 'HCO3-', 'HCO2-', 'N2']

# fileList = GenerateFileList(directory=directory, regex=regText, ignoreCase=True)

startIndex = 2
endIndexOffset = 3
printIntermediates = False

# ------------------------------------------------------------------------------------------------ #
# Balance stoichiometric matrices
dictKeyArray = []
nReactantsDict = {}
nTargetsArray = []
targetsArray = []


# Initialize storage for number of reactants 
for reactant in reactantsToGet:
	nReactantsDict[reactant] = []


# Balance each stoichiometric matrix and record reactant numbers
for fileName in fileList:

	dictKey = fileName.split('-')[1]
	dictKey = dictKey.split('.')[0]
	
	print(dictKey)
	dictKeyArray.append(dictKey)


	matrix = ImportStoichiometricMatrix(directory + '/' + fileName)
	endIndex = len(matrix[0]) - endIndexOffset
	
	[sMatrix, reactions, fVectorOpt, cDotVectorOpt, cDotVectorOptNorm, reactants, ioStatus, \
	result] = \
	BalanceStoichiometricMatrix(matrix, startIndex, endIndex)
	
	#pdb.set_trace()

	PrintStoichiometry(cDotVectorOptNorm, reactants, ioStatus, \
	printIntermediates=printIntermediates)
	print()
	
	
	for reactantToGet in reactantsToGet:
		# If the reactant to query isn't in the list of reactants for this matrix, record 0
		if reactantToGet not in reactants:
			nReactantsDict[reactantToGet].append(0)
			
		# On the other hand, if it is, add the number of if to its array
		elif reactantToGet in reactants:
			reactantIndex = reactants.index(reactantToGet)
			nReactant = cDotVectorOptNorm[reactantIndex]
			nReactantsDict[reactantToGet].append(nReactant)
	
	i = 0
	while i < len(reactants):
		ioStatusReactant = ioStatus[i]
				
		if ioStatusReactant == 'Target':
			targetsArray.append(reactants[i])
			nTarget = cDotVectorOptNorm[i]
			nTargetsArray.append(nTarget)
		i += 1
	
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Output results of balancing 

headers = ['Scenario'] + reactantsToGet + ['Target Molecule', 'Target']
vectorList = [dictKeyArray]

for reactantToGet in reactantsToGet:
	vectorList.append(nReactantsDict[reactantToGet])

vectorList.append(targetsArray)
vectorList.append(nTargetsArray)

oMatrix = generateOutputMatrixWithHeaders(vectorList, headers, delimeter=',')
writeOutputMatrix(outputFileName, oMatrix)
# ------------------------------------------------------------------------------------------------ #

