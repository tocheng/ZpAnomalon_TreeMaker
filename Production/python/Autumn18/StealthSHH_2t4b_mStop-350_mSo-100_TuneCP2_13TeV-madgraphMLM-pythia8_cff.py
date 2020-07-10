import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0934CEEF-4B99-5143-8938-F57B4B915A02.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0E7AABFD-10F3-C545-8239-3300DEF6494F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0EEC9F3D-5AF8-2141-A85F-DC938CF07C7B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/13A7B9E7-0B02-B340-8BAA-34B6FDF4123B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1ACA2E4B-C245-B140-8A72-53B756359BBE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/20C41F89-4DBE-E54C-B5C5-7E16DC8A7B30.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/22176BD7-E683-7344-9052-3DA6A8F3DFAD.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/23203C71-7948-0A49-82D6-E6D0E209C983.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/260450B7-99F0-3C49-BB62-3AAA6615D36C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/29CE3D05-1D9B-8C4A-B3A0-5AB3142B1A09.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/3660E7D6-9470-BB4D-8043-A7E5C608F3D0.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/3911FCC0-2DF1-3144-898F-A733F6A16F2F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/3BF2773D-3626-8D40-ACB3-2E9868474C57.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/41012144-C796-994C-AA81-9EEFD0BF237C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/4196EEEE-B343-974B-B1BF-1344A3BA518E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/42D33D9B-0AD7-1D42-9188-AB78F460AC0B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/485417AD-E575-E046-8EBE-FD955A4B008D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/4F20D007-6F3B-EB4A-AC79-1104866D97C1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/57BEBF3E-8D7F-994E-85C3-031ADDD4A42D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/590BFBCC-D907-364D-9568-0E230E018E22.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/5ED08998-0B4B-8D49-AE87-BBF87E81F4C9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/6771D77B-3289-794F-91C6-A83208D29E36.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/6B3443E7-B05C-7B46-A174-18B6687726F2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/6C1A7F98-3C82-0B4C-9218-0E94D77E6E3C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/6FF662CF-5D78-504D-AE35-60253EAA0664.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/76A42BBB-25D3-D240-BD1B-4CE0A08D2D20.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/80666C1F-442E-2F45-9152-F21F585371CA.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8959B363-FE98-0945-A6FF-2D200E8C416F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/89CCE40E-BE9E-0D49-990F-83FCCA01335D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/89E67D92-E2F9-3041-AC53-EF1F91CEDD38.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8BC0E8AD-C87F-5740-ADBC-3D53641145C9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8D0EB6E7-928D-CE42-9F38-7A5895AC8774.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8D474410-ADAB-124F-9FED-D7F291F6560E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/93C25692-EBFD-5448-A1EB-1A33569469AB.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/952A637A-3B7F-9440-B862-4395E5734F8B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/95AF6D1E-E639-0447-977B-6BBAA4A9A58D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/962FAFA4-BE06-9B43-B165-B44CB5AD7434.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/99323C89-954E-D645-B9BA-D5AEB9512C18.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9D69234E-9B51-CF4C-BF96-80635060AC45.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9E06F083-4913-4944-BC94-AB16565C13D9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9E5E79BC-45FF-7249-86E3-2FEDF8A816D9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A11A6002-F49F-DF4C-A4F4-80BE3A40DD24.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A30AB5F3-D74A-AD40-898E-01E820C7E99B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A482CA4D-B975-E64C-A8EB-E09C5F8EE43A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/ACE7FA6C-D165-6D48-9D93-2F6CC19955BA.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B1EF4561-3258-C848-A414-FE3FA0CE2241.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B53FAFBD-12E4-044A-9075-BD235116CCF7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C2AB10CD-369C-7A4C-836F-42C4FA885F97.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C408B397-A226-D442-B041-AA2FD2D79438.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C6916EEB-A776-924D-93B3-DDAA02DE5AFA.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C6FBE49A-884A-5F40-8018-E142F07D107B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CC3595A4-69B9-7D49-ACA3-18A460479B54.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CD6C5938-8AEA-B64F-849B-452781191929.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CD730608-0DEC-5A42-8486-72DE9FD22863.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D4DDB3CC-524C-244F-BFAE-3DC7306AA92E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D9E74643-751B-344B-B75F-B85D03454A3C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/DAF92DB9-50F2-3D4C-B419-ABF5F5C3C0E3.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/DC3AF955-90B8-914B-8F9C-B543D865FA74.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/DDAFCA80-AA6C-FA43-A759-4C9672F211AE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/DDB37ADF-222F-824B-816F-245E8A27826F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E9F0B3AE-FB1B-8445-A4E4-72A7F5297669.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F458F74B-CCDE-DC40-8C30-B8C48E5D2D0A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F5659E1B-D3AD-5D46-8D99-04C2E0D7B34A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/FDBA0BFB-41B0-5847-9870-9894C9706918.root',
] )
