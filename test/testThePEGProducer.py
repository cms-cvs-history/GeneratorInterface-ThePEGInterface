import FWCore.ParameterSet.Config as cms
from GeneratorInterface.ThePEGInterface.herwigDefaults_cff import *
from GeneratorInterface.ThePEGInterface.herwigValidation_cff import *

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('$Revision: 1.1 $'),
	name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/GeneratorInterface/ThePEGInterface/test/testThePEGProducer.py,v $'),
	annotation = cms.untracked.string('Herwig++ example - QCD events, MRST2001 used, MinKT=1400 GeV')
)

source = cms.Source("EmptySource")

generator = cms.EDProducer("ThePEGProducer",
	herwigDefaultsBlock,
	herwigValidationBlock,

	configFiles = cms.vstring(
#		'MSSM.model'
	),

	parameterSets = cms.vstring(
		'cmsDefaults', 
#		'validationMSSM',
		'validationQCD'
	),
)

ProductionFilterSequence = cms.Sequence(generator)
