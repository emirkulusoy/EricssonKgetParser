# File Parser Library

The `kgetParserLib` parses Ericsson kget files to a text or csv file. 
The "#" symbol is used as a separator at the output file because ";" and "," are already used on kget files.
There is an example text at the end of the README file. 
To use this library, kindly clone the repository.
To get the Ericsson kget file, run the commands below after connecting AMOS:
	lt all
	l+
	kget all
	l-


# Usage
# Directory Structure

project/
│
├── kgetParserLib/
│   ├── __init__.py
│   ├── parser.py
│   └── utils.py
│
└── example_usage.py

# Example Ericsson kget input file

XXX99999X> kget all


Proxy Id                             0
MO                                   SubNetwork=ONRM_ROOT_MO,SubNetwork=WestSacramento,MeContext=XXX99999X,ManagedElement=XXX99999X

dnPrefix                             SubNetwork=ONRM_ROOT_MO,SubNetwork=WestSacramento,MeContext=XXX99999X
locationName                         
logicalName                          
managedElementId                     XXX99999X
managedElementType                   RadioNode
managedElementTypeList[9]            Bts ENodeB EquipmentSupport Fgw GNBCUCP GNBCUUP GNBDU Mce NodeB 
networkManagedElementId              XXX99999X
release                              22.Q2
siteLocation                         
swVersion                            22.Q2
userDefinedState                     
userLabel                            XXX99999X
vendorName                           Ericsson AB

Proxy Id                             1
MO                                   SubNetwork=ONRM_ROOT_MO,SubNetwork=WestSacramento,MeContext=XXX99999X,ManagedElement=XXX99999X,ENodeBFunction=1

alignTtiBundWUlTrigSinr              0 (OFF)
allowMocnCellLevelCommonTac          true
altNasBackTo                         0 (DEFAULT_DCN)
biasThpWifiMobility                  10
caAwareMfbiIntraCellHo               true
caUnknownImeisvEnabled               false
checkEmergencySoftLock               false
combCellSectorSelectThreshRx         300
combCellSectorSelectThreshTx         300
csfbMeasFromIdleMode                 true
csfbUseRegisteredLai                 false
csmMinHighHitThreshold               70
dlBbCapacityMaxLimit                 3000
dlBbCapacityNet                      3000
dlBbCapacityTarget                   -1
dlMaxWaitingTimeGlobal               0
dnsLookupOnTai                       0 (OFF)
dnsLookupTimer                       0
dnsSelectionS1X2Ref                  
Struct drxCycleNb has 3 members:
 >>> 1.drxCycleNb0 = 256
 >>> 2.drxCycleNb1 = 2048
 >>> 3.drxCycleNb2 = 8192
Struct drxInactivityTimerNb has 3 members:
 >>> 1.drxInactivityTimerNb0 = 4
 >>> 2.drxInactivityTimerNb1 = 4
 >>> 3.drxInactivityTimerNb2 = 2
dscpLabel                            24
ductIntCharInfoScheme                0 (GENERIC)
ductIntFlexibleDetectionEnabled      false
eNBId                                81300
eNodeBFunctionId                     1
Struct eNodeBPlmnId has 3 members:
 >>> 1.mcc = 999
 >>> 2.mnc = 999
 >>> 3.mncLength = 3
enabledUlTrigMeas                    false
endcAllowed                          true
endcAwareMfbiIntraCellHo             false
endcDataUsageReportEnabled           false
endcIntraBandBlocked                 true
endcPowerOffsetLte                   3
endcS1OverlapMode                    true
endcSplitAllowedMoVoice              false
endcSplitAllowedNonDynPwrShUe        true
endcX2IpAddrViaS1Active              false
eranUlCompReSelectLinkTime           7
eranUlCompVlanPortRef                
eranVlanPortRef                      ManagedElement=XXX99999X,Transport=1,VlanPort=ERAN
extendedBandN77Supported             false
extendedWaitTimeNb                   0
externalLinkFailureFilterTime        490
externalLinkToGNodeBFailureFilterTime  490
forcedSiTunnelingActive              false
gtpuErrorIndicationDscp              40
inhibitEndcFr2Volte                  false
initPreschedulingEnable              true
interEnbCaTunnelDscp                 14
interEnbUlCompTunnelDscp             14
Struct interNodalProtVersions has 8 members:
 >>> 1.commonProtVerRel = 10
 >>> 2.commonProtVerRelMinus1 = 9
 >>> 3.commonProtVerRelMinus2 = 8
 >>> 4.commonProtVerRelMinus3 = 7
 >>> 5.eRanCaProtVerExact = 407
 >>> 6.eRanUlCompProtVerExact = -1
 >>> 7.interEnbCaProtVerExact = 253
 >>> 8.interEnbUlCompProtVerExact = -1
intraEnbHoNasNonDelIndCause          false
intraRanIpAddressRef                 ManagedElement=XXX99999X,Transport=1,Router=LTE,InterfaceIPv4=LTE,AddressIPv4=1
ipsecEndcEpAddressRef                
ipsecEpAddress2Ref                   
ipsecEpAddressRef                    
iuaBbmResourceLimit                  20
licCapDistrMethod                    0 (SYSTEM)
licConnectedUsersPercentileConf      90
licDlBbPercentileConf                90
licDlPrbPercentileConf               90
licUlBbPercentileConf                90
licUlPrbPercentileConf               90
locationReportForPSCell              false
maxNoCellsNaccCsfb                   4
maxNoCellsNaccSessionCont            4
maxNrOfEnbPartnersEranUlComp         6
maxNrOfInterEnbUlCompLbm             6
maxRandc                             255
measuringEcgiWithAgActive            false
mfbiFbipOnX2Enabled                  true
mfbiSupport                          true
mfbiSupportPolicy                    true
minRandc                             1
mmeSupervisionTimerNb                5
mtRreWithoutNeighborActive           true
nbRrcConnReestActive                 false
nnsfMode                             2 (RPLMN_IF_MME_SERVES_SPLMN)
obsMode                              5 (AUTO)
obsProtectionAutoTargetMode          1 (COUNTER_AND_PM_EVENT)
obsStatus                            0 (NORMAL)
Struct onDurationTimerNb has 3 members:
 >>> 1.onDurationTimerNb0 = 4
 >>> 2.onDurationTimerNb1 = 4
 >>> 3.onDurationTimerNb2 = 2
pdbMeasurementDelta                  0
pimAutoDetectionEnabled              false
pimCancAutoConfigEnabled             false
plmnServiceAlarmFilterTime           0
plmnServiceAlarmLevel                0 (ENODEB)
prachConfigEnabled                   false
prioritizeAdditionalBands            false
pwsPersistentStorage                 1 (ON)
randUpdateInterval                   200
release                              not applicable
releaseInactiveUesInactTime          5
releaseInactiveUesMpLoadLevel        2 (VERY_HIGH_LOAD)
rpUpIpAddressRef                     
rrcConnReestActive                   true
s1GtpuEchoDscp                       14
s1GtpuEchoEnable                     0 (DISABLED)
s1GtpuEchoFailureAction              0 (NONE)
s1GtpuEchoInterval                   1000
s1HODirDataPathAvail                 true
s1RetryTimer                         30
sctpEndcX2Ref                        
sctpRef                              ManagedElement=XXX99999X,Transport=1,SctpEndpoint=LTE
sctpX2Ref                            
sleepCellDataCollect                 1 (COLLECTION_ENABLED)
softLockRwRWaitTimerInternal         60
softLockRwRWaitTimerOperator         60
srsAllocationV2TddAasEnabled         false
srsPeriodicityTdd                    20
tMoVoiceBearerEstSupervision         2000
tOutgoingHoExecCdma1xRtt             5
tRelocOverall                        7
tS1HoCancelTimer                     3
tWaitForConnEstInd                   3
tddVoipDrxProfileId                  -1
timeAndPhaseSynchAlignment           true
timeAndPhaseSynchCritical            false
timePhaseMaxDevIeNBUlComp            30
timePhaseMaxDeviation                100
timePhaseMaxDeviationCdma2000        100
timePhaseMaxDeviationEdrx            10
timePhaseMaxDeviationIeNbCa          30
timePhaseMaxDeviationMbms            50
timePhaseMaxDeviationOtdoa           100
timePhaseMaxDeviationSib16           100
timePhaseMaxDeviationTdd             15
timePhaseMaxDeviationTdd1            15
timePhaseMaxDeviationTdd2            15
timePhaseMaxDeviationTdd3            15
timePhaseMaxDeviationTdd4            15
timePhaseMaxDeviationTdd5            15
timePhaseMaxDeviationTdd6            15
timePhaseMaxDeviationTdd7            15
timePhaseSyncStateEdrx               true
timePhaseSyncStateIeNBUlComp         true
timePhaseSynchStateCdma2000          true
timePhaseSynchStateMbms              true
timePhaseSynchStateNR                true
timePhaseSynchStateOtdoa             true
timePhaseSynchStateSib16             true
ueCapabilityEnquirySteps             0 (ONE_STEP)
ulBbCapacityMaxLimit                 1500
ulBbCapacityNet                      1500
ulHeavyUeBsrHyst                     100
ulHeavyUeBsrThUlCaFactor             6
ulHeavyUeBsrThresh                   400
ulHeavyUeDetectTime                  500
ulHeavyUeDetectTimeOffset            250
ulMaxWaitingTimeGlobal               0
ulPhyProcResTradingEnabled           0
ulSchedulerDynamicBWAllocationEnabled  true
upEndcX2IpAddressRef                 
upIpAddress2Mode                     0 (LOAD_SHARING)
upIpAddress2Ref                      
upIpAddressRef                       ManagedElement=XXX99999X,Transport=1,Router=LTE,InterfaceIPv4=LTE,AddressIPv4=1
upX2IpAddress2Ref                    
upX2IpAddressRef                     
useBandPrioritiesInSCellEval         true
useFullResumeId                      false
userLabel                            
x2BlackList[0]                       
x2GtpuEchoDscp                       14
x2GtpuEchoEnable                     0 (DISABLED)
x2IpAddrViaS1Active                  true
x2SetupTwoWayRelations               false
x2WhiteList[0]                       
x2retryTimerMaxAuto                  1440
x2retryTimerStart                    30
zzzTemporary1                        
zzzTemporary10                       -2000000000
zzzTemporary11                       -2000000000
zzzTemporary12                       -2000000000
zzzTemporary13                       -2000000000
zzzTemporary16                       -2000000000
zzzTemporary18                       -2000000000
zzzTemporary2                        
zzzTemporary21                       -2000000000
zzzTemporary22                       -2000000000
zzzTemporary23                       -2000000000
zzzTemporary24                       -2000000000
zzzTemporary25                       -2000000000
zzzTemporary26                       -2000000000
zzzTemporary28                       -2000000000
zzzTemporary3                        
zzzTemporary32                       -2000000000
zzzTemporary34                       -2000000000
zzzTemporary35                       -2000000000
zzzTemporary36                       -2000000000
zzzTemporary37                       -2000000000
zzzTemporary39                       -2000000000
zzzTemporary40                       -2000000000
zzzTemporary41                       -2000000000
zzzTemporary42                       -2000000000
zzzTemporary43                       
zzzTemporary47                       -2000000000
zzzTemporary48                       -2000000000
zzzTemporary49                       -2000000000
zzzTemporary5                        
zzzTemporary50                       -2000000000
zzzTemporary51                       -2000000000
zzzTemporary52                       1
zzzTemporary57                       -2000000000
zzzTemporary58                       -2000000000
zzzTemporary6                        
zzzTemporary61                       -2000000000
zzzTemporary64                       false
zzzTemporary65                       -2000000000
zzzTemporary66                       -2000000000
zzzTemporary67                       -2000000000
zzzTemporary68                       -2000000000
zzzTemporary69                       -2000000000
zzzTemporary7                        
zzzTemporary70                       -2000000000
zzzTemporary71                       -2000000000
zzzTemporary72                       
zzzTemporary73                       
zzzTemporary74                       -2000000000
zzzTemporary75                       -2000000000
zzzTemporary76                       -2000000000
zzzTemporary77                       -2000000000
zzzTemporary78                       
zzzTemporary79                       -2000000000
zzzTemporary8                        
zzzTemporary80                       -2000000000
zzzTemporary81                       -2000000000
zzzTemporary82                       -2000000000
zzzTemporary83                       -2000000000
zzzTemporary84                       -2000000000
zzzTemporary9                        -2000000000

Proxy Id                             2
MO                                   SubNetwork=ONRM_ROOT_MO,SubNetwork=WestSacramento,MeContext=XXX99999X,ManagedElement=XXX99999X,ENodeBFunction=1,AdmissionControl=1

admNrRbDifferentiationThr            750
admNrRrcDifferentiationThr           1000
admResourceMinQciPrio                5
admissionControlId                   1
arpBasedPreEmptionState              1 (ACTIVATED)
diffAdmCtrlFilteringEnabled          false
dlAdmDifferentiationThr              800
dlAdmOverloadThr                     850
dlMbmsGbrRatio                       200
dlNonPaGbrTn                         750
dlTransNwBandwidth                   1000
enhPttAdmCtrlRejPaReqOvlGbr          true
lbAtoThresholdLevel1                 30
lbAtoThresholdLevel2                 60
limitSrNonPa                         0
nrOfPaConnHpaReservPerCell           0
nrOfPaConnReservationsPerCell        20
nrOfPrevPreempPaRbReservation        0
nrOfRbReservationsPerPaConn          4
paArpOverride                        6
paArpOverrideHpa                     0
preemptInactTimerMin                 15
resourceReservationForDifferentiation  5
resourceReservationForPAState        1 (ACTIVATED)
srBbmPaUsersPreallocation            true
ulAdmDifferentiationThr              800
ulAdmOverloadThr                     850
ulNonPaGbrTn                         750
ulTransNwBandwidth                   1000
zzzTemp1                             -1
zzzTemp10                            1000
zzzTemp11                            1000
zzzTemp12                            1000
zzzTemp13                            1000
zzzTemp14                            1000
zzzTemp15                            1000
zzzTemp16                            1000
zzzTemp17                            1000
zzzTemp18                            1000
zzzTemp19                            1000
zzzTemp2                             -1
zzzTemp3                             -1
zzzTemp4                             -1
zzzTemp5                             -1
zzzTemp6                             1000
zzzTemp7                             1000
zzzTemp8                             1000
zzzTemp9                             1000
zzzTemporary1                        
zzzTemporary2                        
zzzTemporary22                       -2000000000
zzzTemporary23                       -2000000000
zzzTemporary24                       -2000000000
zzzTemporary25                       -2000000000
zzzTemporary26                       -2000000000
zzzTemporary27                       -2000000000
zzzTemporary28                       -2000000000
zzzTemporary3                        
zzzTemporary4                        
zzzTemporary5                        -2000000000
zzzTemporary6                        -2000000000
zzzTemporary7                        -2000000000

Proxy Id                             3
MO                                   SubNetwork=ONRM_ROOT_MO,SubNetwork=WestSacramento,MeContext=XXX99999X,ManagedElement=XXX99999X,ENodeBFunction=1,AmoFunction=1

allowInterVendorX2Signal             true
amoAllowedInterVendor                true
amoFunctionId                        1

Proxy Id                             4
MO                                   SubNetwork=ONRM_ROOT_MO,SubNetwork=WestSacramento,MeContext=XXX99999X,ManagedElement=XXX99999X,ENodeBFunction=1,AnrFunction=1

anrFunctionId                        1
cellRelHoAttRateThreshold            10
detectObsoleteExtCellsEnabled        false
maxNoPciReportsEvent                 15
maxTimeEventBasedPciConf             30
pciConflictDetectionEcgiMeas         false
pciConflictMobilityEcgiMeas          false
perCgiMeasPlmnWhiteListGeran         true
perCgiMeasPlmnWhiteListUtran         true
perEcgiMeasPlmnWhiteList             true
plmnWhiteListEnabled                 true
plmnWhiteListGeranEnabled            true
plmnWhiteListUtranEnabled            true
prioHoRate                           100
prioHoSuccRate                       100
prioTime                             100
probCellDetectLowHoSuccThres         35
probCellDetectLowHoSuccTime          1
probCellDetectMedHoSuccThres         60
probCellDetectMedHoSuccTime          1
problematicCellPolicy                2 (AUTO_DETECT_AND_BAR)
removeNcellTime                      1
removeNenbTime                       1
removeNgnbTime                       7
removeNrelTime                       2
s1HoPrepConsFailThres                50
zzzTemporary1                        
zzzTemporary10                       -2000000000
zzzTemporary11                       -2000000000
zzzTemporary12                       -2000000000
zzzTemporary13                       -2000000000
zzzTemporary2                        
zzzTemporary3                        
zzzTemporary4                        
zzzTemporary5                        -2000000000
zzzTemporary6                        -2000000000
zzzTemporary7                        -2000000000
zzzTemporary9                        -2000000000

Proxy Id                             5
MO                                   SubNetwork=ONRM_ROOT_MO,SubNetwork=WestSacramento,MeContext=XXX99999X,ManagedElement=XXX99999X,ENodeBFunction=1,AnrFunction=1,AnrFunctionEUtran=1

acquirePlmnIdListEnabled             false
anrEutranInterFMeasReportDecr        1
anrEutranInterFMeasReportIncr        10
anrEutranInterFMeasReportMax         100
anrEutranInterFMeasReportMin         5
anrFunctionEUtranId                  1
anrInterFreqState                    1 (ACTIVATED)
anrIntraFreqState                    1 (ACTIVATED)
anrUesEUtraIntraFDecr                10
anrUesEUtraIntraFIncrAnr             20
anrUesEUtraIntraFIncrHo              100
anrUesEUtraIntraFMax                 20
anrUesEUtraIntraFMin                 1
anrUesThreshInterFDecr               10
anrUesThreshInterFIncrAnr            20
anrUesThreshInterFIncrHo             100
anrUesThreshInterFMax                0
anrUesThreshInterFMin                0
cellAddRsrpThresholdEutran           -1040
cellAddRsrqThresholdEutran           -1920
hoAllowedEutranPolicy                true
lbCellOffloadCapacityPolicy          1000
x2SetupPolicy                        true

Proxy Id                             6
MO                                   SubNetwork=ONRM_ROOT_MO,SubNetwork=WestSacramento,MeContext=XXX99999X,ManagedElement=XXX99999X,ENodeBFunction=1,AnrFunction=1,AnrFunctionGeran=1

anrFunctionGeranId                   1
anrGeranMeasReportDecr               1
anrGeranMeasReportIncr               10
anrGeranMeasReportMax                100
anrGeranMeasReportMin                5
anrGeranMeasReportRacIncr            20
anrGeranRacMeasOn                    true
anrStateGsm                          1 (ACTIVATED)
problematicCellPolicy                0 (OFF)
rimIntegrationEnabled                true

