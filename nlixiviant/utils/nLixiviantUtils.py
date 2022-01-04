# ------------------------------------------------------------------------------------------------ #
def Calculate_Lixiviant_Mass_with_Unknown_Quantities(massCarbonGrams, MWForsterite, MWLix, \
MWCarbon, nCarbonForsterite, zeta):

	# massCarbon: Mass of carbon to be sequestered (in grams of carbon)
	# MWForsterite: Molecular weight of forsterite (usually ≈ 140 grams per mole)
	# MWLix: Molecular weight of the lixiviant (for gluconic acid, this 196 grams per mole)
	# MWCarbon: Molecular weight of just the carbon atom (12 grams per mole)
	# nCarbonForsterite: Number of carbon atoms sequestered by dissolution of a single 
	# asymmetric unit of forsterite (2 at most)
	
	# zeta: the product of unknown quantities
	# zeta = Concentration of lixiviant in moles per cubic meter / 
	# (extraction efficiency * precipitation efficiency * 10^4 * pulp density)
	
	
	
	massLixiviantGrams = ( (massCarbonGrams * MWForsterite * MWLix) / \
	(MWCarbon * nCarbonForsterite) ) * zeta
	
	
	return massLixiviantGrams
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
def Calculate_Lixiviant_Mass(massCarbonGrams, MWLix, zetaArray, CELix, Celec, \
MWCarbon=12, MWForsterite=141, nCarbonForsterite=2):
	
	# Inputs

	# massCarbon: Mass of carbon to be sequestered (in grams of carbon)
	# MWOlivine: Molecular weight of olivine (usually ≈ 140 grams per mole)
	# MWLix: Molecular weight of the lixiviant (for gluconic acid, this 196 grams per mole)
	# MWCarbon: Molecular weight of just the carbon atom (12 grams per mole)
	# nCarbonOlivine: Number of carbon atoms sequestered by dissolution of a single asymmetric unit 
	# of olivine (2 at most)
	# zetaArray: combined unknown quantities (in grams per mole)
	# CELix: electrical cost of making a unit of lixiviant (joules per gram)
	# Celec: cost of solar electricity (dollars per joule)

	mLixArray = []
	totalCostELixArray = []
	totalDollarCostArray = []

	i = 0
	while i < len(zetaArray):

		zeta = zetaArray[i]
	
		mLixGrams = \
		Calculate_Lixiviant_Mass_with_Unknown_Quantities(massCarbonGrams, MWForsterite, MWLix, \
		MWCarbon, nCarbonForsterite, zeta)
	
		# Calculate the energy cost of making mLixGrams
		totalCostELix = mLixGrams * CELix
		
		# Calculate the financial cost of making mLixGrams
		totalDollarCost = totalCostELix * Celec
		
	
		mLixArray.append(mLixGrams)
		totalCostELixArray.append(totalCostELix)
		totalDollarCostArray.append(totalDollarCost)
	
		i += 1
		
	return [mLixArray, totalCostELixArray, totalDollarCostArray]
# ------------------------------------------------------------------------------------------------ #
