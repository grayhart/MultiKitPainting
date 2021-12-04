# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:05:29 2021

@author: graham
"""
#
# MultikitPainting
#
# Read in multiple DNA Segment files from different kits and merge them into a single DNAPainter import file
# Adjust match and group names accordingly
#
# Intial version - MyHeritage output files 
# Kit1, Kit2, Kit3 
# 
# Kit names are KITNAME + " DNA Matches shared segments " + Month dd yyyy-Random.csv
#
#
# Give a list of siblings and I will open and read their files.
#
#
# DNAPainter input needs to be:
# Chr Start End cM SNPs Match Confidence Group Side Notes Colour
    
import config
import os
import glob
import pandas as pd
import numpy as np


# Look for a single file for each sibling in the input folder and read it in
# Parse the unique id and store the details in a pandas dataframe tored in a hash
def read_files(sibling_list):
    df_array = {}
    for name in sibling_list:
        sibhash = {}
        print(f"Reading Name: {name}")
        filelist = glob.glob(config.INPUT_FOLDER + "\\" + name + "*")
        if len(filelist) == 0:
            print(f"No files found for {name}. Exiting")
            os.Exiting
        if len(filelist) > 1:
            print(f"Too many files found for {name}.")
            for file in filelist:
                print(file)
            print("Exiting")
            os.Exiting
        file = filelist[0]
        print(f"File: {file} found and will be processed")
        
        file_df = pd.read_csv(file)
        sibhash['name'] = name
        firstentry = file_df.iloc[0]['DNA Match ID']
        unique_id = firstentry.split("-D-")[0]
        sibhash['uniqueid'] = unique_id
        sibhash['data'] = file_df
        
        # Add columns for the unique ids of the kit and the match
        sibhash['data']['kit_id'] = unique_id
        
        def add_match_id(x):
            return  "D-" + x.split("-D-")[1]    
        
        sibhash['data']['match_id'] = sibhash['data']['DNA Match ID'].apply(add_match_id)
        sibhash['data']['orig_match_name'] = sibhash['data']['Match name']
        sibhash['data']['kit_match_name'] = name
        df_array[name] = sibhash
    return df_array


# Each siubling has the matches for each other sibling
# For each sibling after the first, remove the entries for the preceding siblings as they will already be present
def remove_duplicate_sibling_entries(df_array):
    is_first=True
    sib_ids = []
    temp_df = df_array
    for sibkey in temp_df:
        sibling = temp_df[sibkey]
        this_id = sibling['uniqueid']
        if is_first:
            sib_ids.append(this_id)
            is_first=False
            continue
        for sibid in sib_ids:
            key = this_id + "-" + sibid
            # Remove entries with this key
            df_array[sibkey]['data'] = sibling['data'][sibling['data']['DNA Match ID'] != key]
        sib_ids.append(this_id)
    return df_array
        
    
# For each sibling, change the Name field to a dummy name (the same one for each in case DNA Painter cares about it)
# Change the match_name to be prefixed by the relevant initial of the sibling
def prepare_converted_matches(df_array):
    temp_df = df_array
    for sibkey in temp_df:
        prefix = sibkey[0]
        sibling_df = temp_df[sibkey]['data']
        def set_to_dummy(x):
            return 'Dummy'
        
        sibling_df['Name'] = sibling_df['Name'].apply(set_to_dummy)
        
        def add_prefix(x):
            return prefix + '-' + x;
        
        sibling_df['Match name'] = sibling_df['Match name'].apply(add_prefix)
        
        df_array[sibkey]['data'] = sibling_df
    return df_array
    
def combine_output(df_array):
    comb_df = pd.DataFrame()
    for sibkey in df_array:
        comb_df = comb_df.append(df_array[sibkey]['data'])
    return comb_df

def format_and_add_group_and_side(df_array):
    # Sort and name the fields into the order that DNA Painter would like 
    # Chr Start End cM SNPs Match Confidence Group Side Notes Colour
    mapper = { 
        'Index' : 'Index',
        'DNA Match ID' : 'DNA Match ID',
        'Name' : 'Name',
        'Match name' : 'Match',
        'Chromosome' : 'Chr',
        'Start Location' : 'Start',
        'End Location' : 'End',
        'Start RSID' : 'Start RSID',
        'End RSID' : 'End RSID',
        'Centimorgans' : 'cM',
        'SNPs' : 'SNPs'
        }
    
    # Add the unique IDs and other information into the Notes
    def create_notes(x):
        return 'Created by MultikitPainter. Unique kit-match-id for MyHeritage = ' + x
        
    df_array['Notes'] = df_array['DNA Match ID']
    df_array['Notes'] = df_array['Notes'].apply(create_notes)
    
    df_array = df_array.rename(columns=mapper)
    df_array['Confidence'] = 0
    df_array['Group'] = ''
    df_array['Side'] = ''
    df_array['Colour'] = ''
    df_array['Ancestor'] = ''
    
    # Set the various sides and groups
    # df0['New Col1'] = np.where((df0['Col'] > 0), 'Increasing', 
    #                      np.where((df0['Col'] < 0), 'Decreasing', 'No Change'))
    
    if config.USE_NAMES:
        matchfield = 'orig_match_name'        
    else:
        matchfield = 'match_id'
        
    
    
    for match in config.SIBLING_LIST:
        df_array['Group'] = np.where((df_array['orig_match_name'] == match),df_array['kit_match_name'] + ' - ' + df_array['orig_match_name'], df_array['Group'])
        df_array['Side'] = np.where((df_array['orig_match_name'] == match),'Both', df_array['Side'])

    for match in config.BOTH_LIST:
        df_array['Group'] = np.where((df_array[matchfield] == match),df_array['kit_match_name'] + ' - ' + df_array['orig_match_name'], df_array['Group'])
        df_array['Side'] = np.where((df_array[matchfield] == match),'Both', df_array['Side'])
        
    for match in config.PATERNAL_LIST:
        df_array['Group'] = np.where((df_array[matchfield] == match),df_array['kit_match_name'] + ' - ' + df_array['orig_match_name'], df_array['Group'])
        df_array['Side'] = np.where((df_array[matchfield] == match),'Paternal', df_array['Side'])
        
    for match in config.MATERNAL_LIST:
        df_array['Group'] = np.where((df_array[matchfield] == match),df_array['kit_match_name'] + ' - ' + df_array['orig_match_name'], df_array['Group'])
        df_array['Side'] = np.where((df_array[matchfield] == match),'Maternal', df_array['Side'])
    
    for match in config.ANCESTOR_LIST:
        df_array['Ancestor'] = np.where((df_array[matchfield] == match), 1, df_array['Ancestor'])
        
        
    return df_array
    
def save_output(df_array):
    output_file = config.OUTPUT_FOLDER + "\\outputfile.csv"

    
    df_array.to_csv(output_file,index=False, columns=('Chr', 'Start', 'End', 'cM', 'SNPs', 'Match', 'Confidence', 'Group', 'Side', 'Notes', 'Colour', 'Ancestor'))
    

# Read in the files 
df_array = read_files(config.SIBLING_LIST)

# Remove duplicate sibling entries
df_array = remove_duplicate_sibling_entries(df_array)

# Prepare the final changes 
df_array = prepare_converted_matches(df_array)

# Combine and save the output 
df_array = combine_output(df_array)

# Add the group and side where known
df_array = format_and_add_group_and_side(df_array)

# Write the output
save_output(df_array)



