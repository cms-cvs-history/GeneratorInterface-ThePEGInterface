#!/bin/env cmsRun
import FWCore.ParameterSet.Config as cms

process = cms.Process("Gen")

process.source = cms.Source("LHESource",
	fileNames = cms.untracked.vstring('file:ttbar.lhe')
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('alpha'),
	name = cms.untracked.string('LHEF input'),
	annotation = cms.untracked.string('ttbar')
)

process.load("Configuration.StandardSequences.Services_cff")

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
			'lheDefaults', 
			'lheDefaultPDFs'
		)
	)
)

process.load("Configuration.StandardSequences.VtxSmearedGauss_cff")

process.VtxSmeared.src = 'generator'
process.genEventWeight.src = 'generator'
process.genEventScale.src = 'generator'
process.genEventPdfInfo.src = 'generator'
process.genParticles.src = 'generator'
process.genParticleCandidates.src = 'generator'

process.genParticles.abortOnUnknownPDGCode = False

process.load("Configuration.StandardSequences.Generator_cff")

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

process.load("Configuration.EventContent.EventContent_cff")

process.GEN = cms.OutputModule("PoolOutputModule",
	process.FEVTSIMEventContent,
	dataset = cms.untracked.PSet(dataTier = cms.untracked.string('GEN')),
	fileName = cms.untracked.string('test.root')
)
process.GEN.outputCommands.append('keep *_source_*_*')
process.GEN.outputCommands.append('keep *_generator_*_*')

process.outpath = cms.EndPath(process.GEN)

process.schedule = cms.Schedule(process.p0, process.outpath)
