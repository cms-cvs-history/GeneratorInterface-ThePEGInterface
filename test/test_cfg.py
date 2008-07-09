#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms

process = cms.Process("Gen")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))

process.configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('alpha'),
	name = cms.untracked.string('ThePEG'),
	annotation = cms.untracked.string('Herwig++ QCD')
)

process.load("Configuration.StandardSequences.Generator_cff")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'

process.load("GeneratorInterface.ThePEGInterface.herwigDefaults_cff")

process.source = cms.Source("ThePEGSource",
	process.herwigDefaultsBlock,

	eventsToPrint = cms.untracked.uint32(1),
	configDump  = cms.untracked.string("LHC.in"),

	configFiles = cms.vstring(
#		'MSSM.model'
	),

	parameterSets = cms.vstring(
		'cmsDefaults',
#		'mssm',
		'validation'
	),

	mssm = cms.vstring(
		'cd /Herwig/NewPhysics',
		'set HPConstructor:IncludeEW No',
		'set TwoBodyDC:CreateDecayModes No',
		'setup MSSM/Model ${HERWIGPATH}/SPhenoSPS1a.spc',
		'insert NewModel:DecayParticles 0 /Herwig/Particles/~d_L',
		'insert NewModel:DecayParticles 1 /Herwig/Particles/~u_L',
		'insert NewModel:DecayParticles 2 /Herwig/Particles/~e_R-',
		'insert NewModel:DecayParticles 3 /Herwig/Particles/~mu_R-',
		'insert NewModel:DecayParticles 4 /Herwig/Particles/~chi_10',
		'insert NewModel:DecayParticles 5 /Herwig/Particles/~chi_20',
		'insert NewModel:DecayParticles 6 /Herwig/Particles/~chi_2+'
	),

	validation = cms.vstring(
		'cd /Herwig/MatrixElements/',
		'insert SimpleQCD:MatrixElements[0] MEQCD2to2',
		'set /Herwig/Cuts/QCDCuts:MHatMin 20.*GeV'
	)
)

process.load("Configuration.StandardSequences.VtxSmearedGauss_cff")

process.genParticles.abortOnUnknownPDGCode = False

process.p0 = cms.Path(process.pgen)

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

process.outpath = cms.EndPath(process.GEN)

process.schedule = cms.Schedule(process.p0, process.outpath)
