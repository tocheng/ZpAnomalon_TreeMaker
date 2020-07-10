import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/0504C395-1529-6144-B631-EFDB3D149E59.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/06755C70-42CF-8445-AAF2-EFF9205059F5.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/07A86A1B-AEC6-884E-943B-819B94D6C6D4.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/07EF63F7-EB0F-6546-BC9F-4FE8D9263BC4.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/07F3E312-2BAA-014B-AD61-A8D86AE24435.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/0B609125-A55A-4F4A-AC24-D6766A28FC90.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/0C427592-D745-2542-8870-DF7FE8706403.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/0C6B38F4-B0EA-F04E-AD19-8DE4DF8E250E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/0E4543E0-F827-714E-A3BB-906973F78E34.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1040D4F0-33A6-844C-84F0-413400AE4437.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1223D2EA-E89B-E84B-A949-0040CB5FEF64.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1343C233-A78F-9340-A791-26B8C51F8A30.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/14CA1761-B39D-5B40-A123-39B1E1038B43.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/14E9C99D-32CC-9147-B093-FE132E1A682C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/159B5874-AD22-FF4C-B23F-B2E190613ACE.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/17528C7A-232B-D844-ACC7-527863024814.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1818A1F6-4159-AA4C-BAFE-675EB7AE71F9.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1836BBEC-60A4-364E-9031-53DD04342867.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1A8BCBD4-D841-724B-B92E-A0CBA1230342.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1B1814BD-E52B-B649-A0BC-4C5BABFCFA7F.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1B9D1802-BE15-1A47-91D1-4FFC7F7C20ED.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1BD5AC49-D2BE-1F46-9ADE-6C3BC7CF2A24.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1C944020-19E8-7F43-845C-016AE1D7AC82.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1CBF293A-624B-4A4A-9681-3091DB61719D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1D3A4D94-EB74-5D4B-9A42-9506C122A977.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1F491546-6741-EE46-A785-ACD1E2385345.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/1F85F775-AACC-F84E-8CC4-6428C5DE37CE.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/2050173B-D2F1-4541-9C2B-19F5B438F5AA.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/21471413-933E-254C-BA7C-4E614575EDDB.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/2214D873-136D-5746-B87A-A10F1F00F89C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/2276C4C4-2BED-CC44-888C-DC1D7331F945.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/25731111-8EA8-414D-9C50-E5166015BAD0.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/26345225-EDC7-EF4D-A967-F4B4D45C3988.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/26A8599E-B13B-7D49-BAAB-D3FDAAAF0597.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/27221A68-C15C-BB48-91A0-638494C40BC4.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/298A838F-1210-2F4B-81CF-95389201F067.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/2A47A5BA-B836-1049-BBB9-5020189E5B90.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/2B927DCF-37EC-C641-91BD-D7D54B196284.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/2C375F84-5A1E-D944-A712-0D85B6ADC776.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/2C3C668F-9B49-B848-B3A2-15150C3CAF01.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/2CBD450B-A5E9-F54C-BA34-3C71501A578C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/2F342A16-93DE-4D46-8428-47E00FA0892E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/2F73BA16-EA53-1541-BAB7-AFE4E95D4177.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/317A75BB-26AD-FF40-9851-7CE05DD0A5C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/341245AE-409A-6F43-A503-5D9FA063D8DA.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/3641D4F8-1CFC-4444-8D3F-C3877D755D45.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/37502ACA-2CA3-5441-9B67-5F8C2E7D1003.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/38B47907-A0B2-444D-ACD4-547BC3BA43A9.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/38D9F745-5CFC-8A47-8938-517DDB2E4199.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/38DDD1E3-79C0-D94A-A574-6410DC086AC5.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/38EC5C04-3714-E240-8DB0-EBC4A4E57A55.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/3AD03253-B4AB-CD42-B400-E73A20489F30.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/3CA7EC17-C44B-4043-A0B4-4A4B054E9B95.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/4282E527-925B-2146-BCFC-FFD56606D181.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/449C09B3-E004-2D4D-ABD6-48FBCBD60584.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/450AE0B5-45F3-974B-A4E3-B3A37AD040A4.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/46E44267-12A8-5540-AF6C-EE934A9219FD.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/488670AA-F7DA-424D-8479-A0DCF78AA801.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/48C35D8B-8B80-1D4D-A801-E7AA766EA5B1.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/496F8862-596C-144A-A22D-8A1192DBB83C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/49B0E757-EABF-7541-9230-7E51342228DD.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/4C7794B6-444B-1048-AABF-F170A1F61B31.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/4DF92138-9FF8-504E-B4C7-DE68D6091DA2.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/4E50B9EC-6D5D-AE45-9660-38FF1CD53D54.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/4E7603CF-38D8-CC4E-9225-08493A232333.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/4F78C609-29DF-5C4C-BC28-AC70CEBD4824.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/516001E7-D243-264E-88B0-F04B0FB8059D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/5439A558-C045-9B46-9D01-C3E1488D8348.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/5590C9EC-D858-8E4E-AA7E-8CD71EF22823.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/56DA6CAD-9708-0F4B-A94C-377653439A7F.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/5716181D-74C0-C144-95FB-4E1F16A1A62B.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/57C7CDA7-3871-B348-88D6-0185695F9575.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/5C3C5C7D-8161-1744-9031-525720E41520.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/5CC548C6-B167-F94A-8274-4CCB0BF9F5CF.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/5DF6458B-5965-2147-BACF-FC40BB0D5FD9.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/5F428BF6-B129-C544-818B-B5EB955D0376.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/5F6FF416-A537-FB46-84EE-6772CA3C7F79.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/62253375-092F-214D-A521-1392262364A3.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/671C589D-113C-524A-BA2A-65386B11386C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/69391060-88E5-6543-B079-53ACBAF17185.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/69CDFDB9-E092-BE49-9721-114885705458.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/6BC29746-4770-574C-AF6E-2C48DB504096.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/6D5260DF-01DE-354E-8FE4-632FD5BB3234.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/6E3AD922-5CC6-2541-90E9-A1446BE79768.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/6ECC7BCC-0817-7F46-9BF7-FAA59A6D25F2.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/6F6B455F-82F2-F34F-B3E4-E8F6E6681FD7.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/705C3164-4F47-734C-B994-D6B6EA975124.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/722BC1C6-92CE-3E4F-BC44-D64A50DBDF91.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/7335C15E-4C78-BB4D-BE64-418098B751E3.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/73F62D08-A414-524E-B42E-47F4D8D3BE72.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/74BC4BCB-E4F0-BB41-85BE-C09D3073AFCE.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/7530BEFE-5AD9-784E-94A5-93D9079F7750.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/75324FA6-6851-E34E-8E13-7A60EB5A108B.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/76105504-3A75-EC45-9814-2C285B02F71F.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/7643B026-DACF-C94C-A5B0-AD10C1BB9745.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/76F7D22C-35AD-7E4F-8250-6EB5F0D2DA17.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/774CA710-609A-1840-9278-549E71D43E12.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/7944F2B2-4877-BD4D-AAD5-404109838D6B.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/79BA9E2A-D922-8C45-85CC-B60F071C0080.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/7B09586B-AD3A-3243-A577-ACFE65915ED0.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/7BD6FDFA-6D84-BF4E-B747-A8BD1B26BC2E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/7BEB7B3A-6F3B-CE4C-A31D-261E9C12E747.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/7DEE3847-2E0A-7444-86B7-649100B28FE6.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/7F54E712-0053-7245-9404-D1309FDA68A2.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/802A7865-DF6B-B949-91AF-3F2CBA7BE272.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/86C25BC8-9855-F94A-9AFF-EF71F38826A8.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/893853FF-77FB-C741-BC46-FD5E3D8D4ADF.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/8A6BF09B-B341-C34F-B66A-82B38F55F8AD.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/8BFC6E0F-8B38-FB46-BA06-981C44DBA82A.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/8C013B71-4DCE-D74A-8BA3-10EAE87290D5.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/907DD58A-F477-3C4A-AC4E-E049E064030E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/90C9ED4F-6EAD-2645-BD66-67DA41EA06D5.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/913E3B7B-80F9-1E4D-B9D8-21518CEBEE06.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/92E49529-81C4-5D4D-B704-3C9BC7065B42.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/93116C9E-CEB6-8045-8CD8-16E23945E199.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/93F59768-FCCE-F74B-9A5F-B3C3EBB42395.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/940A1929-B0DC-0343-8753-74ECBC71CC21.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/9794570B-6EAA-5945-96F3-440174F17B8E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/9A0190DE-3310-C94C-934B-A2315631CBC7.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/9B3D7F00-415E-D542-A67D-D2A3674E34A3.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/9B6ED8AC-371A-2F45-BFB6-6DA08768E1B4.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/9C61D5ED-A958-7C4D-8F8D-2BBCCA96C8A8.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/9E08E393-D0D2-494D-A127-AF5703D363F3.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/9E615B2B-FCCA-1C4B-9917-9645B7EE2EBE.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/A0E52211-0E58-2547-A6EC-1CB92BC88541.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/A2BC8C96-E89E-894D-81E7-2AB660B998C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/A44FE952-E377-2F4F-B768-0B2B18F7548D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/A8D3000E-6EB5-F741-A57D-A4EB4A42C3EB.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/ACD54F87-B32E-EE43-A8DC-50D80B1649C5.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/B043F469-B707-934F-B3E1-32940F959B9D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/B0863AE4-6120-B14A-BB1D-81D0FC9219D7.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/B250D8FB-4B84-244C-85B2-99574EEAA6C8.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/B311CB95-0A8E-8847-9BCB-0BAB03538F75.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/B3A0D4C4-63AE-8540-B6C4-13838CCBD474.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/B653DE06-75CB-1540-AE1F-DABFBFE2E163.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/B7102BB1-B447-134C-8DBC-6FFF25F45CF1.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/B84ADB01-123E-9E44-A27E-5908A982F748.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/B92D39E9-5251-AE4D-A646-02204E5EC17A.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/B98516ED-5F82-E84F-A2C6-62162CA228CB.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/BD8644CF-DDB1-5847-A900-61736E75405F.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/BE2C5BA0-3C55-9341-A136-08935E357256.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/C04EC0FD-000D-D947-8A26-5DE273A81130.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/C09E290D-FDE8-4641-8903-E31AF544FD13.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/C13798DD-029B-5441-8949-C33156756637.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/C1AA8860-8348-CB41-AF3A-5379C9940A2D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/C1D114C2-88D8-AA41-8F0C-121A993BBBB9.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/C2638DA5-C8BE-9741-A3A3-375644DEEFC0.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/C4E5062D-C7A3-C043-87DD-76D61AF8B428.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/C568B614-716E-FD40-BE95-3679964A4EEA.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/C72406DB-1DA0-D749-A6DF-F5020335B50E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/C98C80AE-02B0-144E-B715-A727003E8D65.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/CA5A813C-E1EA-2E4F-9C5F-760E2B2DF262.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/CB497F9C-62B6-D746-A1D8-D8E02879D156.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/CE266586-6F35-9E4A-B134-DC4D1AC15F3D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/CEA32347-2A77-5944-BC53-57627A21A3B3.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/CF117DE8-7782-DB4E-BA19-C1A8016A07EC.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/CF8965BB-94B3-0846-964C-1E97049D0C5A.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/D15A9F82-5F6E-E242-BB81-615381E8298E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/D19C7F33-819B-4B48-B018-014C0E773954.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/D1A358DD-E5A9-9C4F-93BE-3FBA35131BC2.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/D1BC420B-2289-5F47-908E-6413F1061413.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/D331692E-7C15-5547-A023-6E09A62BBA17.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/D3E92092-4CBD-DE4D-A62B-E7A54BD836A2.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/D3F1A9DA-1C6F-4B49-A210-DA079DA04B28.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/D91A471F-FB73-9345-8DC0-41DC62B309E2.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/DAA57F48-65AF-174C-A048-E047819255AC.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/DB9F89D2-BB85-AA40-988A-C4B4FA9D9A7D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/E64CE085-21A3-AE46-B68F-3BF9EC25BEB7.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/E81BDC09-DA09-114E-A759-1E399FC944FB.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/E82F2F55-5D4E-EE45-910B-A8539D50B34E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/EABF845C-6004-824F-95C7-73514DC90BA5.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/EC8A3811-6ADA-1945-94C5-99FE5F0AD6B4.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/EEAD24DB-5572-CE41-B6BD-D6D18C3A4A4F.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/F09CB084-A384-814D-9A61-F5059B11C732.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/F19696BE-0A1F-454C-915A-20D13C43731D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/F77AE349-CDED-834B-895A-123543A65C8C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/F7B2B54A-F841-9445-920A-09357205D7D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/FA6263D8-6ED0-DA48-99F7-5F469C95ABD4.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/FBDF8736-2F72-BC43-B1C3-0882D06E405B.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/FE651E8F-3E50-8140-BA1C-C8CED73FD0B8.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiHH_HToBB_HToBB_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/FF5B2818-C843-9D43-ADCC-3319101AC286.root',
] )
