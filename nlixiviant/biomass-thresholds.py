from utils.vectorOutput import generateOutputMatrixWithHeaders, writeOutputMatrix
from utils.specutils12 import ensure_dir

# Calculate the amount of biomass that can be sourced from the biosphere.

# Global bioenergy supply potential (in Joules per year)
bioEnergyPotentialArray = [100e18, 300e18, 600e18, 1200e18]

# Energy density of dry biomass (in Joules per gram, from https://en.wikipedia.org/wiki/Energy_content_of_biofuel)
biomassEnergyDensity = 15e3

# Parameters for conversion of biomass potential to corresponding zeta
massCarbonGrams = (12/44) * 20 * 1e15
MWForsterite = 141
MWGluc = 196.16
MWCarbon = 12
nCarbonForsterite = 2
conversionFactor = (MWCarbon * nCarbonForsterite) / (massCarbonGrams * MWForsterite * MWGluc)


# Biomass Potential (in gigatonnes per year)
bioMassPotentialGtArray = []
zetaArray = []

i = 0
while i < len(bioEnergyPotentialArray):
	bioEnergyPotential = bioEnergyPotentialArray[i]
	bioMassPotential = bioEnergyPotential / biomassEnergyDensity
	bioMassPotentialGigatonnes = bioMassPotential / 1e15
	bioMassPotentialGtArray.append(bioMassPotentialGigatonnes)
	zeta = bioMassPotential * conversionFactor
	zetaArray.append(zeta)
	i += 1


# Add some direct biomasses to the bioMassPotentialGtArray

headers = ['Biomass Potential Energy (J)', 'Biomass Potential (Gigatonnes)', 'Zeta (grams per mole)']

vectorList = [bioEnergyPotentialArray, bioMassPotentialGtArray, zetaArray]

oMatrix = generateOutputMatrixWithHeaders(vectorList, headers, delimeter=',')

outputFileName = 'output/biomass-thresholds.csv'

ensure_dir(outputFileName)

writeOutputMatrix(outputFileName, oMatrix)
