import FWCore.ParameterSet.Config as cms
from GeneratorInterface.ThePEGInterface.herwigDefaults_cff import *

def customise(process):
	process.RandomNumberGeneratorService.generator = \
		process.RandomNumberGeneratorService.theSource

	for i in [
		'genParticles.src',
		'genParticleCandidates.src',
		'genEventWeight.src',
		'genEventScale.src',
		'genEventPdfInfo.src',
		'genEventProcID.src',
		'VtxSmeared.src',
		'g4SimHits.Generator.HepMCProductLabel',
		'famosSimHits.SourceLabel'
	]:
		try:
			obj = reduce(lambda x, y: getattr(x, y),
			             i.split('.')[:-1], process)
			setattr(obj, i.split('.')[-1], 'generator')
		except:
			pass

        try:
                process.mergedtruth.HepMCDataLabels.append('generator')
        except:
                pass

	process.output.outputCommands.append('keep *_generator_*_*')

	process.genParticles.abortOnUnknownPDGCode = False

	return process
