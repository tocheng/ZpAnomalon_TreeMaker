import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/BE99E154-3534-2241-843D-81B104E6D3F4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/0F63E366-1575-1248-9167-FC55024ADE64.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/95952196-447A-6C44-B501-7AA9E6A1153B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/A564D704-B86A-CE47-9996-519BE572F313.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/ACD5E906-CC00-0049-95E2-FF9D15CF1661.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/019C6A1D-0453-A645-9156-09B067B08CE0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/050863CA-BC1B-0B47-88B8-E7CC457DA220.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/0828F1FC-48C2-7A44-A48C-9962A539CFB9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/0B0EF725-8904-A840-8F0D-CD494BA2F973.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/0F95955B-B9BE-4744-A665-A334704A6A38.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/1AB1EC5B-95A8-B24D-80A4-4CE80EA1DFD2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/1E5D3B6C-6F19-2247-AC51-5DAC3660119E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/244468C5-56BB-6248-97C0-B1540B8F1839.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/24D4AC3B-0335-884F-BFAE-D26B9FFC9C7D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/2863E20C-C257-0B4E-88F0-A85B0D8B410E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/2AF4973B-C0C4-5D49-8492-DE20C598815E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/2C50DD97-9B52-164C-83DE-5EE9FDE1AE95.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/335D3EE9-0986-484B-992A-98EC077FB51A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/3B091D9C-3245-C248-8D13-AF6BC097B2A9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/3D642288-D8DF-164B-BB0C-164D5340D1E0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/40344316-D162-A04C-A440-EBF66EACACA4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/407A65AD-6431-1E41-A553-401DAB1A1427.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/424EAC9C-97D6-834E-9341-EDE36E7E2B4A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/4517138A-D0DA-A84C-A166-169B5ECDC74B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/472F5488-FD69-DB4F-94B7-3A1F980FD5CF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/4E836180-7432-6747-A2AF-ABCCD3E115A8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/508D4EC8-475B-9642-911F-943A618B444F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/52F687F0-2B7E-F947-BE82-6760FA1ECF68.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/54DE4C41-B8F2-6546-981E-4FC310CB6655.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/58B39179-327B-A148-A58F-34CFCE7B1120.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/58C93AF4-588A-E442-9025-AD5A31AAD558.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/5C7512FF-B717-C342-8719-DB1ECA979C79.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/5E806EF5-937E-A849-8058-8677BD416E67.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/625C981C-B6DE-ED44-AE0B-18DC2CB34813.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/6D9D65B3-27AF-0546-AA26-511BAE8DCDB0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/6DB88487-F1EC-BD40-ACFD-8F1FF469D634.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/6FDE51CD-F40C-E040-972C-15160E01118D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/75CF2C96-9EE7-8448-BF5A-85ECBB9C5309.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/76D9C3D8-DDE4-934D-896B-3BBB0B19F895.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/7A51CA7C-E834-9E4F-B527-51E1CC4DF4B8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/7F3E2B16-B664-894B-8FE1-8542C7424F4C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/83D9139B-2846-D54B-B9C3-E955E40026E1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/859F0793-0C6B-044F-B03C-99C7051E42C3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/8A726808-0664-E04E-9CF0-397BE19E1BD0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/8B2472F6-96C4-584C-B08E-9CD3FDF118AF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/8F23C30E-EC7D-9148-9088-91BA9171B20D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/920960E1-7616-3046-B329-97C49ED0DEEE.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/940F3E94-B520-F745-AB63-5A8ADF8DFEBB.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/982350E7-C966-EA48-BD52-E1349CBBAC7F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/9A416FFC-0CE1-EB46-8C52-6530680A40BC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/A0A78F43-B59E-9B46-AF41-74240225D58E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/A1B65D7A-7304-9E41-B344-B90D8E65B4B9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/A291CE84-6198-1447-BF2A-FA09621A48D6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/A698B3A0-9A09-A847-B8C9-224643ED84AE.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/A75820CE-25CF-0645-A6D6-D8BF441B3EDD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/A7E7DF96-9986-9148-96E7-50CD4A8CD182.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/AC4F314F-FEEC-F44F-AF56-2941353AA27B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/B0F4C793-2316-3B44-88AA-479837271661.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/B28E5E97-6DA2-DE4A-8AB6-564192B0DFC0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/B2DD7B02-323F-3E44-8EFF-844BE802FA48.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/B43F7D4F-7BDA-7B42-8EC0-156E40A8AE16.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/B49791D8-080C-3547-9947-1905555B71B0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/B5BF4B89-A84D-714C-8173-5B28627996FB.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/B9C664DB-9AE4-B04B-B2F4-949D7B4BCABD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/BC34F082-B974-8F42-918B-B726E1122E81.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/BD03CCAC-11C5-0F40-926B-62BF32784507.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/C3AF19F1-71AD-5149-AF31-0115AFE76974.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/C581E729-A59E-794C-875F-1EE7E0B76A1A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/C9CD41AC-2A38-1F46-9E3E-6FCCC50D5C54.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/CD40FB0A-FAE3-2E4E-A930-3551895E1EDD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/CF3F6B00-3915-4B42-BA28-2CA198D4F7D8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/D116BB9B-FC66-F941-B8E3-D9C6FDE56A74.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/D1A4F98E-2F91-F44A-BA06-368698CCAD96.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/D2C91124-5AAF-644C-BE2A-2BBAE6E44125.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/D3ACD034-DCD3-634E-922E-7E43FF7F009F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/DD22EA0C-819D-AA46-98A3-7F2A0267EB14.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/DE88620D-5380-B744-AA79-436D4964E02B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/DFD49682-130E-A248-A97B-E6B460067284.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/DFE978A2-BAA6-BC48-A6EC-3D38F041017F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/E391EEB4-18C3-D340-8BFB-C0EE67096F08.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/E986928B-92E6-D44C-9299-6D2F368B9237.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/F29F987F-5EEF-A847-ACE0-8E756773F352.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/FB402C23-5FDC-FD45-8D83-82C4E9CF2DD4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/FDF0620F-FDD8-BB42-A8CD-FAA5D627BAE2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/FF42A30E-8AA7-4948-A7BE-579664413BB8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/FF7B9752-E477-AE43-9DFD-85B4EF4DCA9B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/410000/02866DAE-4782-4446-A29B-F4C123B33E64.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/410000/D406B9EE-56DB-E646-BB3F-3BE674C02787.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/0D18538B-A7BF-1247-B08B-01A73A7E788A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/280FA90E-2416-634A-BB3C-A5414A25090E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/7BE4FC6C-9C86-9745-8E0D-4348398D5C41.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/DBC20071-8580-BF49-BF27-62EE8ABBC12E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/F34A2060-5C69-194B-8B0F-6B91FAEAFF31.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/0B696A17-522E-594C-87BA-367BB59A9375.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/0BEC532B-2E52-D44A-9423-C885700F1753.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/1055582F-73DB-0C48-92A6-547FB8392FBD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/1CC3B386-5447-4F47-97E0-C7CC361336FE.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/26265AF4-DA1E-0C40-A239-D5D359D2415D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/29610A8C-134D-7045-BEF8-0421850CF7DD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/3306D868-B37C-1B43-8CFD-EB4037E55AEC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/4AC2695B-BA51-3946-9D64-74687B3A8384.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/50EEA65E-5F54-D441-B72F-46681355C234.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/66E79519-8FAE-FA4B-AD7C-6109F67583B2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/67868CC7-BFB9-4F4F-BE72-2EE4BEF8E476.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/6B73E38C-E279-A844-8FC5-A63CB7875268.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/6C8ED3AB-5E61-7648-A663-E4DC481F1FF4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/75F20B1A-B9F5-9F4A-8EED-50E295FDAA73.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/866CCDD0-2732-1D4F-85BE-10F60B8894A6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/886D6BD9-ABDB-D14F-8650-20B007BA8B96.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/925AD9AA-5B90-DC40-8A14-FD182CE1BA0F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/99E90277-6F2A-EF43-9BF8-F912618AD0DB.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/9D15A275-A635-F946-94CB-3562A617AD34.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/A6180812-2E9C-9945-9547-C1F616A2BE20.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/BB52FAD9-C8DE-EF40-9791-E4A11303E9D9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/C23E1BED-7E63-BA47-B409-23F19F452640.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/CBBE9BC4-581A-DD41-BB69-FAEC8833BF29.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/CCF4F7F5-8755-AA47-B6D4-47A7C677AC7E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/CE249E61-D9DD-1D40-A298-D43483088128.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/D5013580-5CEF-8D4D-975C-23FE8ACD1705.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/D5D32B8B-D282-C648-9107-4B41DBEA201F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/F6562A01-4F8A-BB49-ADD6-207BC0B838FC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/FD196C7F-04D2-FD43-87F2-234E6B3E7393.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/FEFE40A3-6E27-A849-8E12-73B9FA8D4DF6.root',
] )