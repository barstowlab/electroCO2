# ------------------------------------------------------------------------------------------------ #
def Calculate_Analytical_Concentration_from_pH(pH, pKa):
	
	# Uses the pKa equation to figure out weak acid concentration needed to achieve a particular pH.
	
	# See Buz Medium #6 pages 212-213 for derivation. 
	
	analyticalConcentration = (10**(-2*pH) + 10**(-pKa - pH))/(10**(-pKa))
	
	return analyticalConcentration
# ------------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------------ #
def Calculate_pH_Curve(pKa, pHArray=None, outputConcOnly=False):
	
	from numpy import arange
	
	if pHArray == None:
		pHArray = arange(1,5,0.1)
	
	analyticalConcArray = []
	resultArray = []

	i = 0
	while i < len(pHArray):
		analyticalConc = Calculate_Analytical_Concentration_from_pH(pHArray[i], pKa)
		analyticalConcArray.append(analyticalConc)
		resultArray.append([pHArray[i], analyticalConc])
	
		i += 1
		

	sortedResultArray = sorted(resultArray, key=lambda x: x[1])
	
	if outputConcOnly == False:
		outputArray = sortedResultArray
	else:
		outputArray = analyticalConcArray
	
	return(outputArray)
# ------------------------------------------------------------------------------------------------ #


from utils.vectorOutput import generateOutputMatrixWithHeaders, writeOutputMatrix
from utils.specutils12 import ensure_dir



gluconicArray = Calculate_pH_Curve(3.72)
aceticArray = Calculate_pH_Curve(4.76)
citricArray = Calculate_pH_Curve(3.1)


figure()
semilogy(transpose(gluconicArray)[0], transpose(gluconicArray)[1], label="Gluconic, pKa = 3.72")
semilogy(transpose(aceticArray)[0], transpose(aceticArray)[1], label="Acetic, pKa = 4.76")
semilogy(transpose(citricArray)[0], transpose(citricArray)[1], label="Citric, pKa = 3.1")

legend()
grid()
xlabel("Desired pH")
ylabel("Analytical Concentration Required (M)")
show()



pKaArray = [3.1, 3.72, 4.76]
pHArrayShort = [1.5, 1.8, 2.0, 2.2, 2.5, 3.0]
pHCurveArray = []

for pKa in pKaArray:
	pHCurve = Calculate_pH_Curve(pKa, pHArray=pHArrayShort, outputConcOnly=True)
	pHCurveArray.append(pHCurve)
	
vectorList = []
vectorList.append(pHArrayShort)
for pHCurve in pHCurveArray:
	vectorList.append(pHCurve)

headers = ['pH']
for pKa in pKaArray:
	headers.append(str(pKa))


oMatrix = generateOutputMatrixWithHeaders(vectorList, headers, delimeter=',')

outputFileName = 'output/acidConcentrations.csv'

ensure_dir(outputFileName)

writeOutputMatrix(outputFileName, oMatrix)
