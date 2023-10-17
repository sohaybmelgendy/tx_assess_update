import json
import pandas as pd
import os

def get_values(d):
    for v in d.values():
        if isinstance(v, dict):
            yield from get_values(v)
        else:
            yield v

                

for i in os.listdir(os.getcwd()):
    filename=i
    print(filename)
    f=open("{}".format(filename),"r")
    data=json.load(f)

    columns_names=["id",
"address",
"GIS_PIN",
"Corporate_Owned",
"Absentee",
"Calculated_Taxes" ,
"Calculated_Taxes_Year" ,
"Census_State",
"Census_County",
"Census_Tract",
"Census_Block",
"Census_Code",
"Electric_Provider",
"Gas_Provider",
"Sewer_Service_Area",
"Water_Provider",
"Number_Of_Owners",
"No_Of_Dwellings",
"Exemption_Code_1",
"Exemption_Code_2",
"Exemption_Code_3",
"Exemption_Code_4",
"Updated",
"PRIOR_GIS_PIN",
"COUNTY_NAME",
"DISTRICT_NAME",
"Municipality",
"Block",
"Lot",
"Qual",
"Owners_Name",
"Owners_Mailing_Address",
"Property_Location",
"City_State_Zip",
"Deed_Book",
"Deed_Page",
"Sale_Date",
"Sale_Price",
"NU_Code",
"Acreage",
"Map_Page",
"Sq_Ft",
"Property_Class",
"Building_Class",
"Land_Desc",
"Building_Desc",
"Class_4_Code",
"Yr_Built",
"Zone",
"Year_1",
"Land_Assmnt_1",
"Building_Assmnt_1",
"Total_Assmnt_1",
"Taxes_1",
"Veterans_CNT",
"Senior_Citizens_CNT",
"Widows_CNT",
"Surv_Spouse_CNT",
"Disabled_CNT",
"Deduction_Amount",
"O_City",
"O_State",
"O_Zip",
"P_City",
"P_State",
"P_Zip",
"Additional_Lots_Parsed",
"Prop_Mail_ErrorCode",
"Owner_Mail_ErrorCode",
"Prop_Mail_HouseNum",
"Prop_Mail_StreetName",
"Prop_Mail_Suffix",
"Prop_Mail_City",
"Prop_Mail_State",
"Prop_Mail_Zip",
"Prop_Mail_Zip4",
"Prop_Mail_UnitNum",
"Prop_Mail_PreDir",
"Prop_Mail_PostDir",
"Prop_Mail_Street",
"Prop_Mail_CRRT",
"Prop_Mail_VacantStatus",
"Owner_Mail_HouseNum",
"Owner_Mail_StreetName",
"Owner_Mail_Suffix",
"Owner_Mail_City",
"Owner_Mail_State",
"Owner_Mail_Zip",
"Owner_Mail_Zip4",
"Owner_Mail_UnitNum",
"Owner_Mail_PreDir",
"Owner_Mail_PostDir",
"Owner_Mail_Street",
"Owner_Mail_CRRT",
"Direct_Parties",
"Reverse_Parties",
"APN",
"TotalUnits",
"Eff_Age",
"Exterior_Finish",
"Foundation",
"Height",
"Interior_Finish",
"Roof_Material",
"Roof_Type",
"Style",
"isRedacted",
"location_lat",
"location_lng",
"parcelCentroid_lat",
"parcelCentroid_lng",
"rooftop_lat",
"rooftop_lng"]

    df=pd.DataFrame(columns=columns_names)

    


    for i in data['result']:
        
        if i['recordData']==None:
            i['recordData']={
				"Eff_Age": '',
				"Exterior_Finish": "",
				"Foundation": "",
				"Height": "",
				"Interior_Finish": "",
				"Roof_Material": "",
				"Roof_Type": "",
				"Style": ""
			}

    
        if i['location']==None:
            i['location']={'lat': '', 'lng': ''}
        
        if i['parcelCentroid']==None:
            i['parcelCentroid']={'lat': '', 'lng': ''}
        
        if i['rooftop']==None:
            i['rooftop']={'lat': '', 'lng': ''}

        data_row=list(get_values(i))
        print(len(data_row))
        newlist=['' if v is None else v for v in data_row]
    
        df.loc[len(df)]=newlist
        

    df.to_csv("{}.csv".format(filename), index=False)   
    print("____________________Done_________________________________")
    

print("____________________Done_________________________________")

