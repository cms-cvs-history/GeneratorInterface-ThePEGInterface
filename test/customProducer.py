import FWCore.ParameterSet.Config as cms
from GeneratorInterface.ThePEGInterface.herwigDefaults_cff import *

def customise(process):
	process.RandomNumberGeneratorService.generator = cms.PSet(
		initialSeed = cms.untracked.uint32(123456789),
		engineName = cms.untracked.string('HepJamesRandom')
	)

	process.genParticles.abortOnUnknownPDGCode = False
	process.genParticles.src = 'generator'
	process.genParticleCandidates.src = 'generator'
	process.genEventWeight.src = 'generator'
	process.genEventScale.src = 'generator'
	process.genEventPdfInfo.src = 'generator'

	process.VtxSmeared.src = 'generator'

	process.output.outputCommands.append('keep *_generator_*_*')

	return(process)
