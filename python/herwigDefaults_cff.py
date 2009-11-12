import FWCore.ParameterSet.Config as cms

herwigDefaultsBlock = cms.PSet(
	dataLocation = cms.string('${HERWIGPATH}'),

	repository = cms.string('HerwigDefaults.rpo'),
	eventHandlers = cms.string('/Herwig/EventHandlers'),
	generatorModule = cms.string('/Herwig/Generators/LHCGenerator'),

	run = cms.string('LHC'),

	cmsDefaults = cms.vstring(
		'+pdfMRST2001',
		'+basicSetup',
		'+cm14TeV',
		'+setParticlesStableForDetector',
	),

	basicSetup = cms.vstring(
		'cd /Herwig/Generators',
		'create ThePEG::RandomEngineGlue /Herwig/RandomGlue',
		'set LHCGenerator:RandomNumberGenerator /Herwig/RandomGlue',
		'set LHCGenerator:NumberOfEvents 10000000',
		'set LHCGenerator:DebugLevel 1',
		'set LHCGenerator:PrintEvent 0',
		'set LHCGenerator:MaxErrors 10000',
		'cd /Herwig/Particles',
		'set p+:PDF /cmsPDFSet',
		'set pbar-:PDF /cmsPDFSet',
		'cd /',
	),

	# Default pdf for Herwig++ 2.3
	pdfMRST2001 = cms.vstring(
		'cd /Herwig/Partons',
		'create Herwig::MRST MRST2001 HwMRST.so',
		'setup MRST2001 ${HERWIGPATH}/PDF/mrst/2001/lo2002.dat',
		'set MRST2001:RemnantHandler HadronRemnants',
		'cd /',
		'cp /Herwig/Partons/MRST2001 /cmsPDFSet',
		'+ueLO',
	),
	# Default pdf for Herwig++ 2.4
	pdfMRST2008LOs = cms.vstring(
		'cp /Herwig/Partons/MRST /cmsPDFSet',
		'+ueLOs',
	),	
	pdfCTEQ5L = cms.vstring(
		'mkdir /LHAPDF',
		'cd /LHAPDF',
		'create ThePEG::LHAPDF CTEQ5L',
		'set CTEQ5L:PDFName cteq5l.LHgrid',
		'set CTEQ5L:RemnantHandler /Herwig/Partons/HadronRemnants',
		'cp CTEQ5L /cmsPDFSet',
		'cd /',
	),
	pdfCTEQ6L1 = cms.vstring(
		'mkdir /LHAPDF',
		'cd /LHAPDF',
		'create ThePEG::LHAPDF CTEQ6L1',
		'set CTEQ6L1:PDFName cteq6ll.LHpdf',
		'set CTEQ6L1:RemnantHandler /Herwig/Partons/HadronRemnants',
		'cp CTEQ6L1 /cmsPDFSet',
		'cd /',
	),

	cm7TeV = cms.vstring(
		'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 7000.0',
		'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV',
	),
	cm10TeV = cms.vstring(
		'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 10000.0',
		'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.1*GeV',
	),
	cm14TeV = cms.vstring(
		'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 14000.0',
		'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.2*GeV',
	),

	# UE Tune from Herwig++ 2.3
	ueLO = cms.vstring(
		'cd /Herwig/UnderlyingEvent',
		'set KtCut:MinKT 4.0',
		'set UECuts:MHatMin 8.0',
		'set MPIHandler:InvRadius 1.5',
		'cd /'
	),
	# UE Tune from Herwig++ 2.4 - with LO** pdf
	ueLOs = cms.vstring(
		'cd /Herwig/UnderlyingEvent',
		'set KtCut:MinKT 4.3',
		'set UECuts:MHatMin 8.6',
		'set MPIHandler:InvRadius 1.2',
		'cd /'
	),

	reweightConstant = cms.vstring(
		'mkdir /Herwig/Weights',
		'cd /Herwig/Weights',
		'create ThePEG::ReweightConstant reweightConstant ReweightConstant.so',
		'cd /',
		'set /Herwig/Weights/reweightConstant:C 1',
		'insert SimpleQCD:Reweights[0] /Herwig/Weights/reweightConstant',
	),
	reweightPthat = cms.vstring(
		'mkdir /Herwig/Weights',
		'cd /Herwig/Weights',
		'create ThePEG::ReweightMinPT reweightMinPT ReweightMinPT.so',
		'cd /',
		'set /Herwig/Weights/reweightMinPT:Power 4.5',
		'set /Herwig/Weights/reweightMinPT:Scale 15*GeV',
		'insert SimpleQCD:Reweights[0] /Herwig/Weights/reweightMinPT',
	),

	setParticlesStableForDetector = cms.vstring(
		'cd /Herwig/Particles',
		'set mu-:Stable Stable',
		'set mu+:Stable Stable',
		'set Sigma-:Stable Stable',
		'set Sigmabar+:Stable Stable',
		'set Lambda0:Stable Stable',
		'set Lambdabar0:Stable Stable',
		'set Sigma+:Stable Stable',
		'set Sigmabar-:Stable Stable',
		'set Xi-:Stable Stable',
		'set Xibar+:Stable Stable',
		'set Xi0:Stable Stable',
		'set Xibar0:Stable Stable',
		'set Omega-:Stable Stable',
		'set Omegabar+:Stable Stable',
		'set pi+:Stable Stable',
		'set pi-:Stable Stable',
		'set K+:Stable Stable',
		'set K-:Stable Stable',
		'set K_S0:Stable Stable',
		'set K_L0:Stable Stable',
		'cd /',
	),

	lheDefaults = cms.vstring(
		'cd /Herwig/Cuts',
		'create ThePEG::Cuts NoCuts',
		'cd /Herwig/EventHandlers',
		'create ThePEG::LesHouchesInterface LHEReader',
		'set LHEReader:Cuts /Herwig/Cuts/NoCuts',
		'create ThePEG::LesHouchesEventHandler LHEHandler',
		'set LHEHandler:WeightOption VarWeight',
		'set LHEHandler:PartonExtractor /Herwig/Partons/QCDExtractor',
		'set LHEHandler:CascadeHandler /Herwig/Shower/ShowerHandler',
		'set LHEHandler:HadronizationHandler /Herwig/Hadronization/ClusterHadHandler',
		'set LHEHandler:DecayHandler /Herwig/Decays/DecayHandler',
		'insert LHEHandler:LesHouchesReaders 0 LHEReader',
		'cd /Herwig/Generators',
		'set LHCGenerator:EventHandler /Herwig/EventHandlers/LHEHandler',
		'cd /Herwig/Shower',
		'set Evolver:HardVetoScaleSource Read',
		'set Evolver:MECorrMode No',
		'cd /',
	),

	lheDefaultPDFs = cms.vstring(
		'cd /Herwig/EventHandlers',
		'set LHEReader:PDFA /cmsPDFSet',
		'set LHEReader:PDFB /cmsPDFSet',
		'cd /',
	)
)
