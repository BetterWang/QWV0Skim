# QWV0Skim

## Produced RERECO V0 Skim

0) ``
1) `/HIMinimumBias1/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER`, Done
2) `/HIMinimumBias2/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER`, Done
3) `/HIMinimumBias3/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER`, Done
4) `/HIMinimumBias4/qwang-V0Skim_v3-9d53152409b8a9b6fb15042030d9bf69/USER`, DONE
5) ``
6) ``
7) ``
8) ``
9) ``
10) ``
11) ``
12) `/HIMinimumBias12/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER`
13) `/HIMinimumBias13/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER`, Done
14) `/HIMinimumBias14/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER`, Done
15) `/HIMinimumBias15/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER`
16) `/HIMinimumBias16/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER`, Done
17) `/HIMinimumBias17/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER`, Done
18) `/HIMinimumBias18/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER`, Done
19) `/HIMinimumBias19/qwang-V0Skim_v3-5f932986cf38f9e8dbd6c3aea7f6c2b4/USER`, Done

## Produced Hydjet V0 Skim
`/MinBias_Hydjet_Drum5F_2018_5p02TeV/qwang-crab_HydjetDrum5F_RECODEBUG_V0Skim_v2-4fb2a1ba2f6b043399c08fb9db565e25/USER`

## Setting up


```bash
ssh lxplus.cern.ch # OR
ssh lxplus6.cern.ch
cd workdir
export SCRAM_ARCH=slc6_amd64_gcc700 # for lxplus6 slc6
export SCRAM_ARCH=slc7_amd64_gcc700 # for lxplus  slc7
cmsrel CMSSW_10_3_1_patch3
cd CMSSW_10_3_1_patch3/src
cmsenv
git cms-init
git remote add CmsHI git@github.com:CmsHI/cmssw.git
git fetch CmsHI
git checkout CmsHI/forest_CMSSW_10_3_1 -b forest_CMSSW_10_3_1
git clone git@github.com:BetterWang/RecoVertex2018.git RecoVertex
git cms-addpkg RecoVertex/PrimaryVertexProducer
scram b -j 4
mkdir QWAna
cd QWAna
git clone git@github.com:BetterWang/QWV0Skim.git
cd QWV0Skim
cmsRun qw_PbPb18_withV0_Skim_v3.py
# if can't find the input file, change it to /eos/cms/store/group/phys_heavyions/qwang/data/FEE2C037-D0FB-B94A-BC4D-00E99FE4647D.root
# crab_HIMB2018_RERECO_V0Skim_v1.py is the config to submit skim jobs.
```
