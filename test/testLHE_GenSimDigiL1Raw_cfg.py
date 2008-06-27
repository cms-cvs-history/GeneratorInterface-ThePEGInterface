#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms

process = cms.Process("GenSimDigiL1Raw")

process.source = cms.Source("LHESource",
	fileNames = cms.untracked.vstring('file:ttbar.lhe')
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string("alpha"),
	name = cms.untracked.string("LHEF input"),
	annotation = cms.untracked.string("ttbar")
)

process.load("Configuration.StandardSequences.Generator_cff")

process.RandomNumberGeneratorService.generator = cms.PSet(
	initialSeed = cms.untracked.uint32(123456789),
	engineName = cms.untracked.string('HepJamesRandom')
)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'

process.load("GeneratorInterface.ThePEGInterface.herwigDefaults_cff")

process.generator = cms.EDProducer("LHEProducer",
	eventsToPrint = cms.untracked.uint32(1),

	hadronisation = cms.PSet(
		process.herwigDefaultsBlock,

		generator = cms.string('ThePEG'),

		configFiles = cms.vstring(),

		parameterSets = cms.vstring(
			'cmsDefaults', 
			'disableCtau10mmDecays',
			'lheDefaults', 
			'lheDefaultPDFs'
		)
	)
)

process.p0 = cms.Path(
	process.generator *
	process.pgen
)

process.load("Configuration.StandardSequences.VtxSmearedBetafuncEarlyCollision_cff")

process.VtxSmeared.src = 'generator'
process.genEventWeight.src = 'generator'
process.genEventScale.src = 'generator'
process.genEventPdfInfo.src = 'generator'
process.genParticles.src = 'generator'
process.genParticleCandidates.src = 'generator'

process.genParticles.abortOnUnknownPDGCode = False

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

process.load("Configuration.StandardSequences.Simulation_cff")
process.load("Configuration.StandardSequences.MixingNoPileUp_cff")

process.g4SimHits.Generator.HepMCProductLabel = 'generator'
#process.trackingtruthprod.HepMCDataLabels.append('generator')

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
