import FWCore.ParameterSet.Config as cms

def customise(process):
	process.RandomNumberGeneratorService.theSource = cms.PSet(
		initialSeed = cms.untracked.uint32(123456789),
		engineName = cms.untracked.string('HepJamesRandom')
	)

	process.genParticles.abortOnUnknownPDGCode = False

	return(process)
