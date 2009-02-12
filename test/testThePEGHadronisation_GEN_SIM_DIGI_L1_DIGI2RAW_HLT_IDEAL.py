# Auto generated configuration file
# using: 
# Revision: 1.108 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
## with command line options: GeneratorInterface/ThePEGInterface/testThePEGHadronisation -s GEN:ProducerSourceSequence,SIM,DIGI,L1,DIGI2RAW,HLT --datatier GEN -n 100 --eventcontent RAWSIM --conditions FrontierConditions_GlobalTag,IDEAL_30X::All --no_exec --customise=GeneratorInterface/ThePEGInterface/customProducer
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/MixingNoPileUp_cff')
process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load('Configuration/StandardSequences/Generator_cff')
process.load('Configuration/StandardSequences/VtxSmearedEarly10TeVCollision_cff')
process.load('Configuration/StandardSequences/Sim_cff')
process.load('Configuration/StandardSequences/Digi_cff')
process.load('Configuration/StandardSequences/SimL1Emulator_cff')
process.load('Configuration/StandardSequences/L1TriggerDefaultMenu_cff')
process.load('Configuration/StandardSequences/DigiToRaw_cff')
process.load('Configuration/StandardSequences/HLTtable_cff')
process.load('Configuration/StandardSequences/EndOfProcess_cff')
#process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration/EventContent/EventContent_cff')

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('LHE example - ttbar events, MRST2001 used, MinKT=1400 GeV'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/GeneratorInterface/ThePEGInterface/test/testThePEGHadronisation.py,v $')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)
process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)
# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('file:ttbar.lhe')
)

# Output definition
process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('testThePEGHadronisation_GEN_SIM_DIGI_L1_DIGI2RAW_HLT.root'),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN'),
        filterName = cms.untracked.string('')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
#process.GlobalTag.globaltag = 'IDEAL_30X::All'
process.generator = cms.EDProducer("LHEProducer",
    eventsToPrint = cms.untracked.uint32(1),
    hadronisation = cms.PSet(
        cm10TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 10000.0', 
            'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.1*GeV'),
        run = cms.string('LHC'),
        repository = cms.string('HerwigDefaults.rpo'),
        cm14TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 14000.0', 
            'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.2*GeV'),
        dataLocation = cms.string('${HERWIGPATH}'),
        pdfCTEQ5L = cms.vstring('mkdir /LHAPDF', 
            'cd /LHAPDF', 
            'create ThePEG::LHAPDF CTEQ5L', 
            'set CTEQ5L:PDFName cteq5l.LHgrid', 
            'set CTEQ5L:RemnantHandler /Herwig/Partons/HadronRemnants', 
            'cp CTEQ5L cmsPDFSet', 
            'set /Herwig/Particles/p+:PDF cmsPDFSet', 
            'set /Herwig/Particles/pbar-:PDF cmsPDFSet', 
            'cd /'),
        lheDefaults = cms.vstring('cd /Herwig/Cuts', 
            'create ThePEG::Cuts NoCuts', 
            'cd /Herwig/EventHandlers', 
            'create ThePEG::LesHouchesInterface LHEReader', 
            'set LHEReader:Cuts /Herwig/Cuts/NoCuts', 
            'set LHEReader:PDFA /LHAPDF/cmsPDFSet', 
            'set LHEReader:PDFB /LHAPDF/cmsPDFSet', 
            'create ThePEG::LesHouchesEventHandler LHEHandler', 
            'set LHEHandler:WeightOption VarWeight', 
            'set LHEHandler:PartonExtractor /Herwig/Partons/QCDExtractor', 
            'set LHEHandler:CascadeHandler /Herwig/Shower/ShowerHandler', 
            'set LHEHandler:HadronizationHandler /Herwig/Hadronization/ClusterHadHandler', 
            'set LHEHandler:DecayHandler /Herwig/Decays/DecayHandler', 
            'insert LHEHandler:LesHouchesReaders 0 LHEReader', 
            'cd /Herwig/Generators', 
            'set LHCGenerator:EventHandler /Herwig/EventHandlers/LHEHandler', 
            'cd /'),
        cmsDefaults = cms.vstring('+basicSetup', 
            '+cm14TeV', 
            '+pdfMRST2001', 
            '+setParticlesStableForDetector'),
        lheDefaultPDFs = cms.vstring('cd /Herwig/EventHandlers', 
            'set LHEReader:PDFA /LHAPDF/cmsPDFSet', 
            'set LHEReader:PDFB /LHAPDF/cmsPDFSet', 
            'cd /'),
        pdfMRST2001 = cms.vstring(''),
        generatorModule = cms.string('/Herwig/Generators/LHCGenerator'),
        eventHandlers = cms.string('/Herwig/EventHandlers'),
        basicSetup = cms.vstring('cd /Herwig/Generators', 
            'create ThePEG::RandomEngineGlue /Herwig/RandomGlue', 
            'set LHCGenerator:NumberOfEvents 10000000', 
            'set LHCGenerator:DebugLevel 1', 
            'set LHCGenerator:PrintEvent 0', 
            'set LHCGenerator:MaxErrors 10000', 
            'set LHCGenerator:RandomNumberGenerator /Herwig/RandomGlue', 
            'cd /'),
        setParticlesStableForDetector = cms.vstring('cd /Herwig/Particles', 
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
            'cd /'),
        pdfCTEQ6L1 = cms.vstring('mkdir /LHAPDF', 
            'cd /LHAPDF', 
            'create ThePEG::LHAPDF CTEQ6L1', 
            'set CTEQ6L1:PDFName cteq6ll.LHpdf', 
            'set CTEQ6L1:RemnantHandler /Herwig/Partons/HadronRemnants', 
            'cp CTEQ6L1 cmsPDFSet', 
            'set /Herwig/Particles/p+:PDF cmsPDFSet', 
            'set /Herwig/Particles/pbar-:PDF cmsPDFSet', 
            'cd /'),
        configFiles = cms.vstring(),
        parameterSets = cms.vstring('cmsDefaults', 
            'lheDefaults', 
            'lheDefaultPDFs'),
        generator = cms.string('ThePEG')
    ),
    dumpEvents = cms.untracked.string(''),
    dumpConfig = cms.untracked.string('')
)
process.ProducerSourceSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.Path(process.endOfProcess)
process.out_step = cms.EndPath(process.output)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.out_step])
# special treatment in case of production filter sequence  
for path in process.paths: 
    getattr(process,path)._seq = process.ProducerSourceSequence*getattr(process,path)._seq


# Automatic addition of the customisation function
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


# End of customisation function definition

process = customise(process)
