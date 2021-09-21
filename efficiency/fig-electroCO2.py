#!/opt/local/bin/python3.7

# ------------------------------------------------------------------------------------------------ #
# fig-co2_reactants.py
# ------------------------------------------------------------------------------------------------ #


from rewiredcarbon.scenario import ImportScenarioTable, CalculateScenarioEfficiencies, \
Plot_Efficiency_Bargraph, Generate_EfficienciesDict_Keys_Sorted_by_Efficiency, \
Export_Efficiency_Bargraph

from rewiredcarbon.utils import ensure_dir



scenarioTableFileName = 'input/fig-electroCO2.csv'
outputFilenameEff = 'output/fig-electroCO2.csv'
outputFilenameFuelMassEff = 'output/fig-electroCO2_mass_eff.csv'

ensure_dir(outputFilenameEff)
ensure_dir(outputFilenameFuelMassEff)

scenarioDict = ImportScenarioTable(scenarioTableFileName)

efficienciesDict = CalculateScenarioEfficiencies(scenarioDict)



keysArray = list(efficienciesDict.keys())

Plot_Efficiency_Bargraph(efficienciesDict, 'effTotalElectricalToFuel', \
'effTotalElectricalToFuel_lowerError', 'effTotalElectricalToFuel_upperError', keysToPlot=keysArray)


Plot_Efficiency_Bargraph(efficienciesDict, 'effTotalElectricalFuelMassEfficiency', \
'effTotalElectricalFuelMassEfficiency_lowerError', \
'effTotalElectricalFuelMassEfficiency_upperError', keysToPlot=keysArray)


Export_Efficiency_Bargraph(outputFilenameEff, efficienciesDict, scenarioDict, \
'effTotalElectricalToFuel', 'effTotalElectricalToFuel_lowerError', \
'effTotalElectricalToFuel_upperError', keysToPlot=keysArray)

Export_Efficiency_Bargraph(outputFilenameFuelMassEff, efficienciesDict, scenarioDict, \
'effTotalElectricalFuelMassEfficiency', 'effTotalElectricalFuelMassEfficiency_lowerError', \
'effTotalElectricalFuelMassEfficiency_upperError', keysToPlot=keysArray)
