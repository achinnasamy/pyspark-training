
METROLINX_TABLES = {

   'OR0'       : 'RVN_PROD.RAMS_PRESTO_USAGE_TEMP',
   'OR1'       : 'RVN_PROD.RAMS_PRESTO_SALESTRAN',
   'OR2'       : 'RVN_PROD.RAMS_PRESTO_USAGE',

   'HI1'       : "RAMS_PRESTO_USAGE_TEMP",
   'HI2'       : "PROD.RAMS_PRESTO_SALESTRAN",
   'HI3'       : "PROD.RAMS_PRESTO_USAGE",

   'HI4'       : "bi_opd_stop_ext",
   'HI5'       : "bi_opd_trip_ext",
   'HI6'       : "nom_vehicle_ext",
   'HI7'       : "nom_vehicle_type_ext",
   'HI8'       : "veh_stop_detail_ext",
   'HI9'       : "veh_stop_ext",
   'HI10'      : "veh_trip_ext",

   'C1'        : "BI_OPD_STOP_Modified",
   'C2'        : "NOM_VEHICLE_Modified",
   'C3'        : "NOM_VEHICLE_TYPE_Modified",
   'C4'        : "VEH_STOP_Modified",
   'C5'        : "VEH_STOP_DETAIL_Modified",
   'C6'        : "VEH_TRIP_Modified"
}


#########################################################################################################
# Creating dictionary from sequence
# Use the zip transformation and dict to create the

key_table = ['C1', 'C2', 'C3']

value_table = ["BI_OPD_STOP_Modified", "NOM_VEHICLE_Modified", "NOM_VEHICLE_TYPE_Modified"]

metro_dict = dict(zip(key_table, value_table))

#########################################################################################################

# Delete a key in hash map
#del metro_dict['C1']


# Returns the keys and values as List
# print(metro_dict.keys())
# print(metro_dict.values())


# Iterating a dictionary
for key, value in metro_dict.iteritems():
    print(key + '  ' + value)


# Get the value for the dictionary
print(metro_dict.get('C1'))


# Get the value for the dictionary
print(metro_dict['C1'])


# Update the element of the dictionary
metro_dict['C1'] = 'BI_START'

# Insert the element to the dictionary
metro_dict['C5'] = 'NOM_START'

print(metro_dict['C1'])
print(metro_dict['C5'])

# Get the value using DEFAULT
print(metro_dict.get('C9', "DEFAULT"))

# Check if a key exists.
print ('C10' in metro_dict)

if 'C3' in metro_dict:
    print("Element is in Dictionary")
else:
    print('Element is not in Dictionary')

new_dict = {'B1': 'NOM', 'B2':'NOM2'}

# metro_dict is added with the elements of new_dict
metro_dict.update(new_dict)

print(metro_dict)