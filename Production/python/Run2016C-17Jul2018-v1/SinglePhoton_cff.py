import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/010000/C4E502C1-CD8E-E811-9D88-002590D9D9BC.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/0228F38F-5E8C-E811-839B-002590D9D894.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/042F0B9F-D38C-E811-B32A-00259029E720.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/0A3FC0E4-CC8C-E811-99A1-0025901FB438.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/0A6E3D15-058C-E811-A433-002590FD5A48.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/143860D7-938A-E811-A62A-002590D9D8AC.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/1ABFD076-5E8C-E811-8C78-0CC47A57D168.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/1ADC57CC-938A-E811-8F61-0025907859B8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/302F7B55-868C-E811-AD94-00259029E714.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/320EA2D2-068C-E811-8484-002590D9D8D4.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/3822E0D1-CC8C-E811-94D1-0CC47AA53D76.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/38E75A5A-788C-E811-8589-00259048AE00.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/3C108EF8-988B-E811-B424-0CC47A57CCE8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/3C1B4984-AF8C-E811-9350-0CC47AA53D6A.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/3C5293DE-798C-E811-BAE1-002590FD5A48.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/421B5A7D-5E8C-E811-A54D-0CC47A0AD4A4.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/42CACA0F-7A8C-E811-9E36-002590D9D8BA.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/4A124161-8A8C-E811-A193-0CC47AA53D6A.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/54FBF5AC-C88C-E811-B027-002590D9D96E.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/5A459734-AC8A-E811-A58C-002590D9D968.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/6258FFEA-168C-E811-A1CF-0CC47A57D1F8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/708FB160-868C-E811-8644-0025902BD8CE.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/72A1C740-5E8C-E811-9EA1-002590791D3C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/7A9E4946-9F8C-E811-9A68-002590791D36.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/7C799FCF-068C-E811-801C-002590791D36.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/824F4275-C88C-E811-9F07-00259075D72C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/88FE9423-B88C-E811-8F97-002590785950.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/8C5E53D7-938A-E811-A11B-00259048AE00.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/90545241-E88C-E811-949F-0CC47AA53D92.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/925DB65C-868C-E811-99E9-00259048AC08.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/9414A435-C08C-E811-8163-00259019A418.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/94F88174-798C-E811-8C94-F45214101150.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/967C379F-DB8C-E811-BEF1-0CC47A0AD6F8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/9A0A9082-5E8C-E811-8B29-0CC47A57CC42.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/9C46FF52-9F8C-E811-A4F0-0CC47A0AD742.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/A0E11A43-9F8C-E811-B123-0CC47AA478BE.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/A2E9529C-B38C-E811-B643-0CC47AA53D86.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/B02A4DA8-DB8C-E811-9AC7-00259029E720.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/B4011786-5E8C-E811-8D08-0025907D24F0.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/B49C5A7A-5E8C-E811-932C-0CC47AA53D6E.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/B4D81A9F-D38C-E811-BC09-00259029E720.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/B6B779D9-9A8C-E811-9960-0CC47AD24CF8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/B8A9FBE7-078C-E811-A810-0CC47A0AD498.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/BEA890F1-9A8C-E811-8750-002590D9D896.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/C6B5A2D4-9A8C-E811-937A-0CC47A0AD456.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/CC1BFFD0-178C-E811-B28C-002590791D60.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/D68B9236-868C-E811-BDC8-0025901ABD18.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/D8FDA516-928C-E811-9F5D-0CC47A0AD6FC.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/DA6271D5-938A-E811-9AE8-0CC47A57D13E.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/E2B689D6-B78C-E811-8FAE-00259029E84C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/EC215D8C-AF8C-E811-B188-0CC47AA53D86.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/EEBD7378-AF8C-E811-AE66-0CC47A57D168.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/20000/FA82E69E-DB8C-E811-B4CB-0025907D1D6C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/02C23424-BE8A-E811-AE5B-002590785950.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/0618F2FD-448B-E811-A4DA-0025907DE278.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/085D4EC4-5D8B-E811-B54E-0CC47AA53D5A.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/086B0F75-9C8B-E811-8DF0-0CC47AA477B6.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/0A180A16-848B-E811-A083-0CC47A57CF08.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/0A20B671-9C8B-E811-9724-0CC47AA53D66.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/0C62C6C0-768B-E811-8F82-0CC47A57CC26.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/0E22A27F-9C8B-E811-88D1-00259075D708.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/127A48C1-768B-E811-9C8C-0CC47A57CC26.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/148931CC-5D8B-E811-99AD-0CC47A0AD780.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/16234479-848B-E811-90B1-0CC47A57CEB4.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/1CA05558-848B-E811-989E-002590FD5A48.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/1E2E439E-438B-E811-B7B8-0025907DE22C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/1E6FE773-9C8B-E811-8A5E-0CC47A57D1F8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/20460D22-BE8A-E811-85CB-002590785950.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/2202A44B-768B-E811-9C06-0CC47A57CF08.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/26B43484-9C8B-E811-AF33-002590D9D8C4.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/2CB6FEE1-5D8B-E811-A7E6-00259019A43E.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/2E3ACB06-5F8B-E811-9EE3-003048CB8572.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/2EE2520E-738B-E811-890C-0CC47A57CBF8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/30C46B66-738B-E811-9B1D-00259075D706.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/325F6C94-438B-E811-BC2A-0CC47A57CCE8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/32B73CBD-4C8B-E811-B61D-0CC47AA53D6E.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/342904A0-658B-E811-9030-00259075D714.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/36AC7003-7F8B-E811-A5A9-0CC47A0AD668.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/36BD7B14-7F8B-E811-A1E0-0025907D2430.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/383A6796-658B-E811-A274-0CC47AA53D76.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/3A7B84C5-768B-E811-BC40-0CC47A57CF08.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/3E2222CD-5D8B-E811-ADB9-0CC47A0AD6AA.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/462B84A1-438B-E811-B085-0CC47A57D036.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/488DF121-888B-E811-ADD0-0CC47A57CD88.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/4C9E55D3-5D8B-E811-8F3B-00259048AC12.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/52107F22-BE8A-E811-A224-0CC47AD24D32.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/5254C130-888B-E811-ABE7-002590D9D966.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/58586462-5E8B-E811-AF36-002590D9D8C0.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/5A190EAF-FF8A-E811-B913-0CC47AA53DBE.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/5ABD8F96-658B-E811-B941-0CC47A0AD6F8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/606559D1-5D8B-E811-BE70-002590AB3A88.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/60F2D3CB-4C8B-E811-B885-002590D9D8C4.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/62E836DD-5D8B-E811-80D3-002590D9D8B4.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/645A51C7-5D8B-E811-94D9-0CC47AA53D60.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/64E203EC-5D8B-E811-BEF6-003048CBA444.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/64E74C70-5E8B-E811-BD94-002590FD5122.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/68791BFF-838B-E811-AF1E-0CC47AA47824.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/68B614EC-7E8B-E811-8A93-0CC47AA4861C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/68C5E54B-768B-E811-A57F-0CC47A0AD668.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/6C0E07BF-768B-E811-BDE7-0CC47A57CDD2.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/6E6D61A1-E38A-E811-BA6F-002590D9D8A4.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/6EB54661-738B-E811-B4B1-00259048AE00.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/7083170F-848B-E811-BD14-002590D9D956.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/742439AF-FF8A-E811-BFBB-0CC47AA53DBE.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/768A40CC-5E8B-E811-AC40-0025907DE278.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/76C86110-7F8B-E811-922E-0CC47A0AD742.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/7A466345-768B-E811-B072-0CC47A57CD56.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/82D550D1-658B-E811-B82F-0025907D244A.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/82FDCEE9-838B-E811-99B2-0025907D2430.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/8414AF77-848B-E811-9661-0CC47A0AD6E4.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/88108675-738B-E811-B8A0-002590FD5A72.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/8C3BA28E-738B-E811-A42A-0CC47A57CCE8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/8C60E0D2-5D8B-E811-863E-0CC47AA53D82.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/90DE2325-738B-E811-AF83-0CC47A0AD6F8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/9237839A-438B-E811-A0AE-003048C8F3A2.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/96278ECC-5D8B-E811-8E0F-0CC47A57CF08.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/9A97D194-658B-E811-96DF-00259048AC12.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/9E0862AF-FF8A-E811-8FD6-002590D9D9DA.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/A0596183-9C8B-E811-A77A-00259029ECEA.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/A0B0C6D5-838B-E811-8135-0CC47AA4861C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/A0ECCA10-BE8A-E811-83D5-0CC47AD24D32.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/A29700E4-C58B-E811-9BD4-002590D9D956.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/A2B36509-848B-E811-B9EB-002590FD5A4C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/A65A4ABE-768B-E811-B26C-0CC47A57CDD2.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/A693F66D-738B-E811-85A1-00259029E87C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/A811A77D-9C8B-E811-B209-002590FD5A78.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/AC359E08-848B-E811-9317-0025907D250C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/AEF9CD9A-658B-E811-A9FB-0CC47A57CB8E.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/B0E8D074-9C8B-E811-9C46-0CC47AA53D92.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/B239243E-738B-E811-97C3-0CC47A0AD6E0.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/B2800998-658B-E811-9229-0025907D1D6C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/B41139DF-7E8B-E811-8C7C-0CC47AA53D6E.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/B692FD19-848B-E811-B474-002590D9D8BA.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/B8779504-848B-E811-A484-002590D9D956.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/B8F1250A-888B-E811-8E47-0CC47AA47824.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/BC1A71A0-658B-E811-981C-002590D9D8B2.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/BE5B68EB-D98C-E811-8C3B-002590D9D8C2.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/BE736B9F-438B-E811-B52A-00259048AD6A.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/C20E55C2-658B-E811-BDBB-002590D9D8B4.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/C2CE4BAA-808B-E811-A2DA-0CC47AB0BDDE.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/C4BC34F0-758B-E811-BA2B-0CC47A0AD3BC.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/C6731B44-738B-E811-81C1-0CC47AA47914.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/CAC4CDB0-FF8A-E811-AB03-0CC47A57CE00.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/CE38DECB-4C8B-E811-93D6-0CC47AB0BDDE.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/D675799A-438B-E811-8019-0CC47A57CCE8.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/DC2DF8C0-768B-E811-A6C0-0CC47A57CC26.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/DC8855A6-E38A-E811-8B72-0CC47AB0B704.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/E02EF8C0-768B-E811-9189-0CC47A57CC26.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/E8007292-658B-E811-9FFC-0CC47AA53DBE.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/EA035CA3-E38A-E811-9FA9-00259029E91C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/EAE4A15F-738B-E811-8CE1-0CC47A57CE00.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/EC6D2E28-668B-E811-A2F1-00259029E84C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/F04D0398-658B-E811-91CB-0025907D1D6C.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/F06396FF-728B-E811-8B74-0CC47AA47824.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/F4B554D3-5D8B-E811-AE68-00259048AC12.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/F6569492-438B-E811-8B42-0CC47AA53D5A.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/F6D7D616-888B-E811-BA8D-0CC47A57D086.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/F888A50C-848B-E811-8E7F-002590D9D8B4.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/FA7914DD-7E8B-E811-8BE6-0CC47A57CF08.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/FA79D1A2-658B-E811-AF5A-0025904CBF10.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/FA81A9FE-7E8B-E811-A478-002590FD5A48.root',
       '/store/data/Run2016C/SinglePhoton/MINIAOD/17Jul2018-v1/40000/FE0D9497-438B-E811-B326-00259075D708.root',
] )