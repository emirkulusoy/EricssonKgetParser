# File Parser Library

The `kgetParserLib` parses Ericsson kget files to a text or csv file. 
The "#" symbol is used as a separator at the output file because ";" and "," are already used on kget files.
There is an example text at the end of the README file. 
To use this library, kindly clone the repository.
To get the Ericsson kget file, run the commands below after connecting AMOS: lt all, l+, kget all, l-
Please check example_usage.py for example usage.

# Usage
# Directory Structure

project/kgetParserLib
project/example_usage.py

# Example Ericsson kget input file

Proxy Id                             1
MO                                   SubNetwork=ONRM_ROOT_MO,SubNetwork=WestSacramento,MeContext=XXX99999X,ManagedElement=XXX99999X,ENodeBFunction=1

alignTtiBundWUlTrigSinr              0 (OFF)
allowMocnCellLevelCommonTac          true
altNasBackTo                         0 (DEFAULT_DCN)
biasThpWifiMobility                  10
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
iTunnelingActive              false
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
obsProtectionAutoTargetMode          1 (COUNTER_AND_PM_EVENT)
obsStatus                            0 (NORMAL)
Struct onDurationTimerNb has 3 members:
 >>> 1.onDurationTimerNb0 = 4
 >>> 2.onDurationTimerNb1 = 4
 >>> 3.onDurationTimerNb2 = 2
pdbMeasurementDelta                  0
pimAutoDetectionEnabled              false

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
zzzTemporary6                        -2000000000
zzzTemporary7                        -2000000000
zzzTemporary9                        -2000000000

