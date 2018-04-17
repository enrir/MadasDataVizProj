# Householder by race
# source: sf1 files decennial census 2000/2010
sf1_hhr_race_2010 = {'H0060001' : 'tot_c10',
'H0070002' : 'notHISP_tot_c10',
'H0070003' : 'notHISP_white_c10',
'H0070004' : 'notHISP_black_c10',
'H0070006' : 'notHISP_asian_c10',
'H0070010' : 'HISP_tot_c10'}

sf1_hhr_race_2000 = {'H006001' : 'tot_c00',
'H007002' : 'notHISP_tot_c00',
'H007003' : 'notHISP_white_c00',
'H007004' : 'notHISP_black_c00',
'H007006' : 'notHISP_asian_c00',
'H007010' : 'HISP_tot_c00'}

#  Housing tenure/rent/values
# sources: 2010 acs5 2015, 2000 sf3 file decennial census

acs5_HU_2015 = {'B25001_001E':'HU_tot_e',
'B25002_001E':'HUstat_tot_e',
'B25002_002E':'HU_occ',
'B25002_003E':'HU_vac',
'B25031_001E':'HU_med_rent',
'B25032_002E':'HU_occ_owner',
'B25108_001E':'HU_agg_value',
'B25107_001E':'HU_med_value'}

sf1_HU_2000 = {'H006001':'HU_tot',
'H006002':'HU_occ',
'H006003':'HU_vac',
'H063001':'HU_med_rent',
'H084001':'HU_occ_owner',
'H086001':'HU_agg_value',
'H085001':'HU_med_value'}

# Educational attainment all popilation aged 25 and over
# sources: 2010 acs5 2015, 2000 sf3 file decennial census

acs5_edu_2015 = {'B15003_001E':'edu_tot25over',
'B15003_017E':'edu_totHS',
'B15003_018E':'edu_SC1',
'B15003_019E':'edu_SC2',
'B15003_020E':'edu_SC3',
'B15003_021E':'edu_grad1',
'B15003_022E':'edu_grad2',
'B15003_023E':'edu_grad3',
'B15003_024E':'edu_grad4',
'B15003_025E':'edu_grad5'}


sf3_edu_sex_2000 = {'P037001':'edu_tot25over_m',
'P037011':'edu_totHS_m',
'P037012':'edu_SC1_m',
'P037013':'edu_SC2_m',
'P037014':'edu_grad1_m',
'P037015':'edu_grad2_m',
'P037016':'edu_grad3_m',
'P037017':'edu_grad4_m',
'P037018':'edu_grad5_m',
'P037019':'edu_tot25over_f',
'P037028':'edu_totHS_f',
'P037029':'edu_SC1_f',
'P037030':'edu_SC2_f',
'P037031':'edu_grad1_f',
'P037032':'edu_grad2_f',
'P037033':'edu_grad3_f',
'P037034':'edu_grad4_f',
'P037035':'edu_grad5_f'}

# Housing  built last 20 years
# Sources: acs5 2015 and sf3 decennial census 2000

acs5_H0_2015 = {'B25034_001E':'HO_tot',
'B25034_002E':'HO_2014',
'B25034_003E':'HO_2013_2010',
'B25034_004E':'HO_2009_2000',
'B25034_005E':'HO_1999_1990'}

sf3_HO_2000 ={'H034001':'HO_tot',
'H034002':'HO_m2000_1999',
'H034003':'HO_1998_1995',
'H034004':'HO_1995_1990',
'H034005':'HO_1989_1980'}

# Median Income 
# Sources: acs5 2015 and sf3 decennial census 2000 (1999 dollars)

acs5_medI_2015 = {'B19013_001E':'med_inc'}
sf3_medI_2000 = {'HCT012001':'med_inc'}