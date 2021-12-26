from utils.vectorOutput import generateOutputMatrixWithHeaders, writeOutputMatrix
from utils.specutils12 import ensure_dir

# Calculate the amount of biomass that can be sourced from the biosphere.

# Global bioenergy supply potential (in Joules per year)
bioEnergyPotentialArray = [100e18, 300e18, 600e18, 1200e18]

# Energy density of dry biomass (in Joules per gram, from https://en.wikipedia.org/wiki/Energy_content_of_biofuel)
biomassEnergyDensity = 15e3


# Biomass Potential (in gigatonnes per year)
bioMassPotentialGtArray = []

i = 0
while i < len(bioEnergyPotentialArray):
	bioEnergyPotential = bioEnergyPotentialArray[i]
	bioMassPotential = bioEnergyPotential / biomassEnergyDensity
	bioMassPotentialGigatonnes = bioMassPotential / 1e15
	bioMassPotentialGtArray.append(bioMassPotentialGigatonnes)
	i += 1
	
headers = ['Biomass Potential Energy (J)', 'Biomass Potential (Gigatonnes)']

vectorList = [bioEnergyPotentialArray, bioMassPotentialGtArray]

oMatrix = generateOutputMatrixWithHeaders(vectorList, headers, delimeter=',')

outputFileName = 'output/biomass-thresholds.csv'

ensure_dir(outputFileName)

writeOutputMatrix(outputFileName, oMatrix)
