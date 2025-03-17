import FWCore.ParameterSet.Config as cms


from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9
process = cms.Process('mtdValidation',Phase2C17I13M9)

process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = "DEBUG"
# or enable LogDebug messages for all modules
process.MessageLogger.debugModules = ["*"]
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')

process.load("Configuration.Geometry.GeometryExtendedRun4D110Reco_cff")
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


process.load('Configuration.StandardSequences.Services_cff')


# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(200.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-3)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/08e4d934-e5d1-43c6-ae01-08dfcbfd6076.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/10347225-5f6a-4513-8ff2-fdb4460b179b.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/127daabc-ff27-4264-8d29-a68b337e4f68.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/14a3bb29-6fce-4cf6-bd70-cda5d4090947.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/1abf35f8-a8cf-4b3a-843e-16a6a82d7695.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/26baf842-dcaa-4b78-aaea-435fcd810efc.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/49808792-e153-46af-90d7-c52d54c192cd.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/4a9ef0c0-d126-4174-b1af-396b260a07d3.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/5e9bb55d-e732-44cf-afaa-5a5ee1a6f490.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/68bd95e6-f820-4837-a9bd-f52ec6cd8686.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/77bab8ea-84b3-43e3-b78d-d7e4bed42b61.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/976f71e1-3258-4352-90cf-4b3ba4e625f8.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/a0cafcc2-f8e5-4f74-9eee-302da27b5488.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/a92e511b-bb7f-4d1d-857f-1d755ce11269.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/ab13b252-6d7c-454a-a5aa-be317ac5638e.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/c5ca9597-8ab3-4529-9680-c85b466f17d8.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/d6ade537-6e32-4d5a-bf02-e098a49b2e52.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/e3b75a09-6fff-47ac-b3e5-5d37a7d4ef17.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/e961d2ae-96b9-4afa-a660-0a2728017307.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/130000/ee0aa054-6b83-47a6-8097-9edd38bc7824.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/0535a978-66b7-4405-b992-03a524916060.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/1601b226-4905-4d53-ad1a-6bf7cada59bc.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/2e4f88ca-3400-4b3f-a2da-eefc6bb218a3.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/57efd50b-de66-4a48-8f0e-16af5caecb19.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/614fde87-f57c-4370-a16d-dfb83c72ae9f.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/638e337c-eb67-43f9-9b17-eb4315b2f882.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/6599295e-8620-458d-88f1-f0d033dd53ef.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/6f9bd929-5d58-41f8-ba0b-89bd3a3b43f3.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/7f05e011-d53e-496d-8621-1d16245d4020.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/89198263-90a2-49f2-a22f-fb78b3377e01.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/92c8bb8b-c4ef-4089-a9cc-f3f727fc70d2.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/95e27b7b-9be5-45dc-aa29-a7fb6c16c52e.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/a255df1f-375b-4578-a70e-bff79d2c4116.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/a69f3268-e518-49a2-b524-fe282990b30d.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/acd20cf8-a49a-46e9-ae8f-f0b3ee87fe06.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/ae14389b-6602-4f8a-9d7b-1b69d724d9fa.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/b7fa42ce-babe-47aa-b0c2-13a3e1ed58f3.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/b8bdf3b0-f866-4d74-95f5-6aae3187d3fe.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/caadae3e-0cf1-445f-b83c-aef0b41c5d1f.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/140000/f512526f-f2da-4a66-aa36-b9c9c12a3426.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2810000/05d251ee-3569-4c2f-911c-b1df07c6f506.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2810000/0a3b4d5a-3e3e-4f84-af0c-e02d6f3e13fd.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2810000/2d416270-79f5-442a-bbf4-a54263bb6851.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2810000/33cab941-7bf1-42a7-8dfd-765a6d8dd8b6.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2810000/645a754c-8837-4421-9870-4bfa3d635269.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2810000/6c6c0263-da29-4882-96d9-33a6cfff1f5a.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2810000/8b378661-e302-44e8-94d3-0ec01de05296.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2810000/928da30b-ee3f-49f3-8c20-8d1b2f6edf37.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2810000/9fbee30c-9190-4502-b549-20c4cad88c38.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2810000/c5f41a3d-6b58-497e-b661-f6892f006718.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/01c16877-11d6-432d-ad29-7406934acaae.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/0d0f6aa7-b13f-4a2d-bf61-fded70b6663f.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/1a82d25b-2f32-4584-9012-ed4e64a366a6.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/1f3f96b8-d4d6-4f1f-98e2-95d055e83964.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/22e1d555-7a6b-4407-aaf8-3254ff66a119.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/27b53419-0863-4afe-a350-1b54edfdc83a.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/2b3e6964-8744-4f55-85d0-8635e6f88b4a.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/2c342479-0bbd-42c3-9e27-f69382c06618.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/2f245688-92b6-4e79-97a0-f7898256ef6f.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/367765ec-26d4-4ec8-95c6-f03789f0ce02.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/3a67681e-5f2e-4be8-a239-87294535b7c0.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/43563064-d2da-426d-97e0-47c8c312a40a.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/518ce2ac-a566-449f-9341-2a0d4efe6008.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/5644f1ea-8d52-4b20-a542-f424a12dc9c0.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/6a8bd8f9-fb8d-4984-b3e0-44de27baa5bc.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/71e7ae78-2257-4c86-b245-596711982912.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/72114ebf-a2d3-4e10-b078-faa5d340cc9f.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/98984e0f-631b-492d-ba43-b1f2bb2e4aaa.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/996fa7fc-c512-4b1e-8910-7d9e8be779e6.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/9b72240b-d928-41be-b499-41d712af714b.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/9bb3014a-d9a5-4644-95ef-b74566882995.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/ac75e971-c6d1-4620-b0df-3fb66e314c31.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/b5a6636d-02dd-4815-a9aa-5a7c57427071.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/b7c3b4bd-c7ac-4b85-b24d-76f9f6e38d6d.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/b7f0d854-4de8-4be3-ba73-997481a08f7e.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/c35c937d-1230-400a-aed1-d0764f0fe9f2.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/c6ed004c-2dd4-40d5-a5a8-901af796ff3a.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/c980dbce-d01f-4902-a40d-1b909288ce00.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/cdf7a2a3-15d7-4d56-bbaf-eed0b21041e1.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/d27a94e4-2d68-41f8-ad97-9ff38fffb7fc.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/d67b1611-b05e-4b69-8794-dddc025104ce.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/d6ed9f4f-ecae-4b97-81de-c109a03614cb.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/d76c970a-1c8e-46d8-8846-45aff04aba57.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/d9d7c97f-6632-4ee5-86e8-d3f9d4376614.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/dbbe6bb8-30f9-4322-980d-85370d900897.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/e8a4b4e0-e7fe-43ef-aa10-deec3e0abbeb.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/f00c6774-8316-4f7b-8ceb-88df8db5c46b.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/f0c5fb82-f0d4-478b-bbb2-957359a19d29.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/f93b70d7-a0d7-429e-9bb7-829c816dbc3f.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/fd5ba9fb-840f-47c8-9ab3-2d1bf17bf939.root', '/store/mc/CMSSW_15_0_0_pre3/RelValMinBias_14TeV/GEN-SIM/141X_mcRun4_realistic_v3_STD_MinBias_Run4D110_GenSim-v1/2820000/ff9c6e4d-fa1d-4a08-9b33-ad89f6fee75e.root'])

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T33', '')
process.load('RecoLocalFastTime.FTLClusterizer.MTDCPEESProducer_cfi')
process.load("Configuration.StandardSequences.Reconstruction_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

#Setup FWK for multithreaded
process.options.numberOfThreads = 1
process.options.numberOfStreams = 0
process.options.numberOfConcurrentLuminosityBlocks = 0
process.options.eventSetup.numberOfConcurrentIOVs = 1

process.MessageLogger.cerr.FwkReport  = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(1),
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
"/store/relval/CMSSW_15_0_0_pre3/RelValTTbar_14TeV/GEN-SIM-RECO/PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v2/2580000/008977ec-54ed-42c7-a69f-7df26681d0c6.root"
    )
)

process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")

# --- BTL Validation
process.load("Validation.MtdValidation.btlSimHitsValid_cfi")
process.load("Validation.MtdValidation.btlDigiHitsValid_cfi")
process.load("Validation.MtdValidation.btlLocalRecoValid_cfi")
btlValidation = cms.Sequence(process.btlSimHitsValid + process.btlDigiHitsValid + process.btlLocalRecoValid)

# --- ETL Validation
process.load("Validation.MtdValidation.etlSimHitsValid_cfi")
process.load("Validation.MtdValidation.etlDigiHitsValid_cfi")
process.load("Validation.MtdValidation.etlLocalRecoValid_cfi")
etlValidation = cms.Sequence(process.etlSimHitsValid + process.etlDigiHitsValid + process.etlLocalRecoValid)

# --- Global Validation
process.load("Validation.MtdValidation.mtdTracksValid_cfi")
process.load("Validation.MtdValidation.mtdEleIsoValid_cfi")
process.load("Validation.MtdValidation.vertices4DValid_cfi")

# process.btlDigiHitsValid.optionalPlots = True
# process.etlDigiHitsValid.optionalPlots = True
# process.btlLocalRecoValid.optionalPlots = True
# process.etlLocalRecoValid.optionalPlots = True
# process.mtdTracksValid.optionalPlots = True
# process.vertices4DValid.optionalPlots = True

process.validation = cms.Sequence(btlValidation + etlValidation + process.mtdTracksValid + process.mtdEleIsoValid + process.vertices4DValid)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.p = cms.Path( process.mix + process.mtdTrackingRecHits + process.validation )
process.endjob_step = cms.EndPath(process.endOfProcess)
process.DQMoutput_step = cms.EndPath( process.DQMoutput )

process.schedule = cms.Schedule( process.p , process.endjob_step , process.DQMoutput_step )

# customisation of the process.

