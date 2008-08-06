#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms

process = cms.Process("GenSimDigiL1Raw")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))

process.configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('alpha'),
	name = cms.untracked.string('ThePEG'),
	annotation = cms.untracked.string('Herwig++ ttbar via LHE')
)

process.load("Configuration.StandardSequences.Services_cff")
process.RandomNumberGeneratorService.generator = cms.PSet(
	initialSeed = cms.untracked.uint32(123456789),
	engineName = cms.untracked.string('HepJamesRandom')
)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'

process.load("GeneratorInterface.ThePEGInterface.herwigDefaults_cff")
process.source = cms.Source("LHESource",
	fileNames = cms.untracked.vstring('file:ttbar.lhe')
)

process.generator = cms.EDProducer("LHEProducer",
	eventsToPrint = cms.untracked.uint32(1),
	dumpConfig  = cms.untracked.string(""),
	dumpEvents  = cms.untracked.string(""),

	hadronisation = cms.PSet(
		process.herwigDefaultsBlock,

		generator = cms.string('ThePEG'),

		configFiles = cms.vstring(),

		parameterSets = cms.vstring(
			'cmsDefaults', 
			'lheDefaults', 
			'lheDefaultPDFs'
		)
	)
)

process.load("Configuration.StandardSequences.VtxSmearedBetafuncEarlyCollision_cff")
process.VtxSmeared.src = 'generator'

process.load("Configuration.StandardSequences.Generator_cff")
process.genParticles.abortOnUnknownPDGCode = False
process.genParticles.src = 'generator'
process.genParticleCandidates.src = 'generator'
process.genEventWeight.src = 'generator'
process.genEventScale.src = 'generator'
process.genEventPdfInfo.src = 'generator'

process.p0 = cms.Path(
	process.generator *
	process.pgen
)

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.printList = cms.EDFilter("ParticleListDrawer",
	src = cms.InputTag("genParticles"),
	maxEventsToPrint = cms.untracked.int32(-1)
)

process.printTree = cms.EDFilter("ParticleTreeDrawer",
	src = cms.InputTag("genParticles"),
	printP4 = cms.untracked.bool(False),
	printPtEtaPhi = cms.untracked.bool(True),
	printVertex = cms.untracked.bool(False),
	printStatus = cms.untracked.bool(True),
	printIndex = cms.untracked.bool(True),
	status = cms.untracked.vint32(1, 2, 3)
)

process.p = cms.Path(
	process.printTree *
	process.printList
)

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

process.load("Configuration.StandardSequences.Simulation_cff")
process.load("Configuration.StandardSequences.MixingNoPileUp_cff")

process.g4SimHits.Generator.HepMCProductLabel = 'generator'
process.mergedtruth.HepMCDataLabels.append('generator')

process.load("Configuration.StandardSequences.L1Emulator_cff")
process.load("Configuration.StandardSequences.DigiToRaw_cff")

process.p1 = cms.Path(
	process.generator *
	process.psim
)

process.p2 = cms.Path(
	process.generator *
	process.pdigi *
	process.L1Emulator
)

process.p3 = cms.Path(
	process.generator *
	process.DigiToRaw
)

process.load("Configuration.EventContent.EventContent_cff")

process.GENSIMDIGIL1RAW = cms.OutputModule("PoolOutputModule",
	process.FEVTSIMEventContent,
	dataset = cms.untracked.PSet(dataTier = cms.untracked.string('GENSIMDIGIL1RAW')),
	SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p0')),
	fileName = cms.untracked.string('raw.root')
)
process.GENSIMDIGIL1RAW.outputCommands.append('keep *_source_*_*')
process.GENSIMDIGIL1RAW.outputCommands.append('keep *_generator_*_*')

process.outpath = cms.EndPath(process.GENSIMDIGIL1RAW)

process.schedule = cms.Schedule(
	process.p0,
	process.p1,
	process.p2,
	process.p3,
	process.outpath
)
