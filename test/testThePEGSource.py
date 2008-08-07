import FWCore.ParameterSet.Config as cms
from GeneratorInterface.ThePEGInterface.herwigDefaults_cff import *

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('$Revision: 1.6 $'),
	name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/Herwigpp_base_cff.py,v $'),
	annotation = cms.untracked.string('Herwig++ example - QCD events, MRST2001 used, MinKT=1400 GeV')
)

source = cms.Source("ThePEGSource",
	herwigDefaultsBlock,
	configFiles = cms.vstring(),

	eventsToPrint = cms.untracked.uint32(1),
	dumpConfig  = cms.untracked.string(""),
	dumpEvents  = cms.untracked.string(""),

	crossSection = cms.untracked.double(1.845050e-07),
	filterEfficiency = cms.untracked.double(1.0),


		QCDParameters = cms.vstring(
			'cd /Herwig/MatrixElements/',
			'insert SimpleQCD:MatrixElements[0] MEQCD2to2',
			'cd /',
			'set /Herwig/Cuts/JetKtCut:MinKT 1400*GeV',
			'set /Herwig/UnderlyingEvent/MPIHandler:Algorithm 1',
		),

		parameterSets = cms.vstring(
			'+cm10TeV',
			'+QCDParameters',
			'+basicSetup',
			'+setParticlesStableForDetector',
		),
)