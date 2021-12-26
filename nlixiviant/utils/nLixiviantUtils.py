# ------------------------------------------------------------------------------------------------ #
def Calculate_Lixiviant_Mass_with_Unknown_Quantities(massCarbon, MWOlivine, MWLix, MWCarbon, \
nCarbonOlivine, densityOlivine, zeta):

	# massCarbon: Mass of carbon to be sequestered (in gigatonnes of carbon)
	# MWOlivine: Molecular weight of olivine (usually ≈ 140 grams per mole)
	# MWLix: Molecular weight of the lixiviant (for gluconic acid, this 196 grams per mole)
	# MWCarbon: Molecular weight of just the carbon atom (12 grams per mole)
	# nCarbonOlivine: Number of carbon atoms sequestered by dissolution of a single asymmetric unit 
	# of olivine (2 at most)
	# densityOlivine: Density of olivine (usually 2.5 x 10^6 grams per cubic meter)
	
	# zeta: the product of unknown quantities
	# zeta = Concentration of lixiviant in moles per cubic meter / 
	# (extraction efficiency * precipitation efficiency * pulp density)
	
	
	massCarbonGrams = 1e15 * massCarbon
	
	massLixiviantGrams = ( (massCarbonGrams * MWOlivine * MWLix) / \
	(MWCarbon * nCarbonOlivine * densityOlivine) ) * zeta
	
	massLixiviantGigatonnes = massLixiviantGrams / 1e15
	
	return massLixiviantGigatonnes
# ------------------------------------------------------------------------------------------------ #
