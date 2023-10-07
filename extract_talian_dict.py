# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:06:21 2023

@author: gabrielmckee

dependencies: None

"""

import re
import pandas as pd





def get_pos_tags(dict_entry, tagging_dict):
    """
    Description
    -----------
    This function identifies an entry's POS tag'
    
    Parameters
    ----------
    dict_entry : str
        the raw entry found in the xlsx file

    Returns
    -------
    x : str
        returns the 2nd string, which is probably the entry's POS.

    """

    # Use regular expressions to find POS tags that start with "#" and end before "="
    tags_with_hash = re.findall(r'(#[\w.]+)(?=\s*=\s*|$)', dict_entry)
    
    # If no "#"-prefixed tags are found, consider the second word as the likely POS tag
    if not tags_with_hash:
        words = dict_entry.split()
        if len(words) >= 2:
            likely_pos_tag = words[1]
            # Check and map to standard POS tag spelling
            likely_pos_tag = tagging_dict.get(likely_pos_tag, likely_pos_tag)  
            tags_with_hash.append(likely_pos_tag)
            
    return "".join(tags_with_hash)
        

def map_POST_variants(dict_entry):
    pass

    
def get_entries(dict_entry):
    
    
    
    pivot = 0
    #identify the position of "="
    for pos, x in enumerate(dict_entry.split()):
        if x == "=":
            pivot = pos
    
    #retain everything that occurs before "="
    entry = dict_entry[:pos].split()
    
    #retain everything that occurs before "="
    pattern = r"^(.*)="
    entry = re.findall(pattern, dict_entry)
    
    #remove pos tag
    
    return dict_entry.split()[0]


def detect_assignmentSymbol(dict_entry):
    """
    Description
    -----------
    This function determines whether the assignment symbol "=" is present in the 
    dictionary entry; "=" is the symbol that divides the entries' form and POS tag(s)
    and. This symbol MUST be in the entry, because we use it to easily identify
    the entry and its POS tags (everything that comes before this symbol is either
    the entry or its POS tag(s))

    Parameters
    ----------
    dict_entry : str
        a dictionary entry in Talian, which typically contains an entry, its POS tag(s),
        an assignment symbol (i.e. "="), a Portuguese translation, a Portuguese definition,
        and sometimes alternative orthographic forms and subentries (e.g. a noun that can
        also be employed as an adjective)

    Returns
    -------
    bool
        if "=" present, returns "True"; if "=" is absent, returns False.
    
    Instructions
    ------------
    This function creates a new column in the xlsx; it has to be manually inspected
    (about 130 instances of missing assignment symbol which must be manually corrected)

    """
    
    if "=" not in dict_entry:
        return False
    return True


def standardize_assignmentSymbol(dict_entry):
    """
    Description
    -----------
    
    Parameters
    ----------
    dict_entry : TYPE
        DESCRIPTION.

    Returns
    -------
    dict_entry : TYPE
        DESCRIPTION.

    """
    
    if " = " in dict_entry:
        return dict_entry
    
    elif re.findall("\s=\S", dict_entry):
        dict_entry = dict_entry.replace(" =", " = ")
        print(dict_entry)
        return dict_entry
    
    elif re.findall("\S=\s", dict_entry):
        dict_entry = dict_entry.replace("= ", " = ")
        print(dict_entry)
        return dict_entry
    
    else:
        return dict_entry



def detect_orthographic_variants(dict_entry):
    """
    

    Parameters
    ----------
    dict_entry : TYPE
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    
    #search for key phrase
    if "o mesmo que" in dict_entry.lower():
        return True
    return False


    

def get_orthographic_variants(dict_entry):
    """
    Description
    -----------
    This function determines whether a dictionary entry contains orthographic variants; 
    if so,the orthographic variants are identified and returned along with their 
    pos tag; the orthographic variants can then later be added to the Talian 
    dictionary as independent entries, if they are not already
    
    Parameters
    ----------
    dict_entry : str
        a dictionary entry, which may contain orthographic variants, as indicated
        by the key phrase "o mismo que" (literally "the same as")

    Returns
    -------
    variants : a list of tuples
        a list containing orthographic variants, their pos tag, and their Portuguese 
        translation as tuples (e.g. abil, adj, Habil)
    
    Assumptions
    -----------
    The function assumes that...
    (1) ...the key phrase and the variants bookend the dictionary entry
           (i.e. no material other than orthographic variants follow the key phrase)
    (2) ...the orthographic variants (if any) have the same POS tag as the main entry

    """
    
    #check whether the entry contains the key phrase
    if "o mesmo que" in dict_entry.lower():
        #find the variants using the key phrase "o mesmo que" (the same as)
        variants = re.compile(r"o mesmo que.*")
        variants = re.find(variants, dict_entry)
        #delete key phrase (which should leave only the variants)
        variants = re.sub("o mesmo que", variants)
        #put the variants into a list
        variants = variants.split()
        
        #attribute original entry's pos tag to each orthographic variant
        
        return variants
    

def add_hashtags_to_embedded_POS_tags(dict_entry, tagging_dict):
    # Extract everything before "="
    entry_parts = dict_entry.split('=')
    if len(entry_parts) != 2:
        return False
    
    before_equal = entry_parts[0].strip()
    after_equal = entry_parts[1]
    
    # Find and add "#" in front of matching POS tags (excluding "num") without parentheses
    for key, value in tagging_dict.items():
        if key != "num":
            pattern = re.compile(rf"(?<![a-zA-Z])#?{key}(?![a-zA-Z])")
            after_equal = re.sub(pattern, f"#{key}", after_equal)
    
    # Reconstruct the modified entry
    modified_entry = f"{before_equal} = {after_equal}"
    
    return "".join(modified_entry)

    
def correct_punctuation(dict_entry):
    
    #replace "," with "."
    
    capturegroup1 = re.match
        

        
def add_entry_to_dict(potential_entry, dict_):
    
    #check whether entry is already in the dictionary
    
    if potential_entry not in dict_:
        #add new entry to dict
        pass
    

def create_tagging_dict():
    """
    

    Returns
    -------
    tagging_dict : TYPE
        DESCRIPTION.

    """
    
    df = pd.DataFrame()
    df = pd.read_excel("tag_standardization.xlsx")
    tagging_dict = pd.Series(df.standard_tag.values,index=df.original_tag).to_dict()
    #order the dict's elements based on len so that smaller items dont interfere with longer ones
    tagging_dict_list = sorted(list(tagging_dict.items()), key = lambda key : len(key[0]), reverse=True)
    tagging_dict = {ele[0] : ele[1]  for ele in tagging_dict_list}
    
    return tagging_dict


def detect_other_POS_tags(dict_entry, tagging_dict):
    """
    

    Parameters
    ----------
    dict_entry : TYPE
        DESCRIPTION.
    tagging_dict : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """

    #get everything after "="
    entry = re.findall("= (.*$)", dict_entry)
    #remove all punctuation
    entry = re.sub(r'[^\w\s]', '', "".join(entry))
    
    # Store matching tags in a list
    matching_tags = []

    #check if a pos tag is in the data
    for key, value in tagging_dict.items():
        pattern = re.compile(r"\s+{}\s+".format(key))
        if re.findall(pattern, entry):
            matching_tags.append(key)
    
    # Return the list of matching tags
    return ", ".join(matching_tags) if matching_tags else False



def clean_sentence(sentence):
    """
    Delete instances of words that contain hashtag in them (analysis error)

    Parameters
    ----------
    sentence : TYPE
        DESCRIPTION.

    Returns
    -------
    cleaned_sentence : TYPE
        DESCRIPTION.

    """
    # Remove "#" between two letters in words
    cleaned_sentence = re.sub(r'(?<=[a-zA-Z])#(?=[a-zA-Z])', '', sentence)
    
    # Keep periods followed by a space
    cleaned_sentence = re.sub(r'\. ', ' ', cleaned_sentence)

    return cleaned_sentence



def standardize_POS_tags(dict_entry, tagging_dict):
    """
    

    Parameters
    ----------
    dict_entry : (str) 
        a complete dictionary entry from the Talian dictionary
    tagging_dict : (dict)
        a tagset that contains all known variants of the tags and their standard variant

    Returns
    -------
   dict
        the dictionary entry, with its initial part of speech standardized

    """
    
    #identify the position of the assignment symbol (i.e. "=")
    pivot = 0
    for pos, x in enumerate(dict_entry.split()):
        if "=" in x:
            pivot = pos
            break
            
    
    dict_entry = dict_entry.split()
    #cut first word, which is usually the entry
    entry = "".join(dict_entry[0])
    pos_tags = " ".join(dict_entry[1:pos])
    rest_of_entry = " ".join(dict_entry[pos:])  
    
    #remove punctuation
    pos_tags = re.sub(r'[^\w\s]', '', pos_tags)
    pos_tags2 = pos_tags
    #search for pos tags
    for key, value in tagging_dict.items():
        #print(key)
        pattern = re.compile(r"{}$".format(key))
        if re.findall(key, pos_tags.rstrip()):
            pos_tags = re.sub(key, value, pos_tags)            
            pos_tags2 = re.sub(value, "", pos_tags)
            if len(pos_tags2) == 0:
                return entry +" "+ pos_tags + " " + rest_of_entry
            break

            
    #check for other pos tags (e.g. adj e sf)
    if len(pos_tags2) != 0 and pos_tags2 != " ":
        for key, value in tagging_dict.items():
            if re.findall(key, pos_tags2.rstrip()):
                pattern = re.compile(r"{}$".format(key))
                pos_tags2 = re.sub(key, value, pos_tags2)
                return entry +" "+ pos_tags + " " + pos_tags2 + " " + rest_of_entry

        return entry +" "+ pos_tags + " " + rest_of_entry
    
    return " ".join(dict_entry)


def split_dictionary_entry_into_subentries(entry):
    # Split the entry into parts based on "#" as the separator
    entry_parts = entry.split('#')
    
    # Extract the word from the original entry (before the first "#")
    word = entry_parts[0].strip()
    
    # Create a list to store the separated entries
    separated_entries = []
    
    # Iterate over the parts starting from the second part
    for i, part in enumerate(entry_parts[1:], start=1):
        # Find the next "#" symbol
        next_hashtag_index = part.find('#')

        # Check if there's a third "#" symbol
        if next_hashtag_index != -1:
            # Extract the part until the next "#" symbol
            separated_part = part[:next_hashtag_index]
        else:
            # If there's no third "#" symbol, use the entire part
            separated_part = part
        
        # Append "=" sign after the words starting with a "#" (POS tags) in entries after the 1st
        if i > 1:
            separated_part = "#" + separated_part
            separated_part = re.sub(r'#(\w+(\.\w+)?)\s*', r'#\1 = ', separated_part)
        
        # Construct the separated entry with the word
        separated_entry = f"{word} {separated_part}"
        
        separated_entries.append(separated_entry)
    
    return separated_entries




def get_Portuguese_translation(string):
    

    pattern = "=\s+(.*);"
    entry = re.findall(pattern, string)
    
    if len(entry) != 0:
        return "".join(entry)
    else:
        return "False"
    
    
columns = ["original_entry"]

def count_assignmentSymbols(dict_entry):
    
    return len(re.findall("=", dict_entry))

df = pd.DataFrame()
df = pd.read_excel("Talian_dictionary.xlsx")


###
### PROCEDURE
###

#1
#detect whether assignment symbol is present; manually correct, as required
#df['assignment_symbol'] = df['original_entry'].apply(lambda entry : detect_assignmentSymbol(str(entry)))

#2
#standardize assignment symbol (whitespace to both left and right)
#df['original_entry'] = df['original_entry'].apply(lambda entry : standardize_assignmentSymbol(str(entry)))


#standardize POS tags (except for multitagged entries)
tagging_dict = create_tagging_dict()
#df['original_entry'] = df['original_entry'].apply(lambda entry : standardize_POS_tags(str(entry), tagging_dict))

# #3
# #extract entry
#df['entry'] = df['original_entry'].apply(lambda entry : get_entries(str(entry)))

# #extract pos tag
#df['pos_tag'] = df['original_entry'].apply(lambda entry : get_pos_tags(str(entry), tagging_dict))


#fix the error that introduced # and "." into certain words.
df['original_entry'] = df['original_entry'].apply(lambda entry : clean_sentence(str(entry)))


#determine whether there are variants (orthographic or other)
#df['orthographic_variants'] = df['original_entry'].apply(lambda entry : detect_orthographic_variants(str(entry)))

#df['other_pos_tags_with_same_form'] = df['original_entry'].apply(lambda entry : detect_other_POS_tags(str(entry), tagging_dict))
#determine whether there are probably pos tags to the right of the "="

#get Portuguese translation
#df['portuguese_translation'] = df['original_entry'].apply(lambda entry : get_Portuguese_translation(str(entry)))

#determine whether there are embedded entries (i.e. one form, but two or more parts of speech, and thus 2 or more entries)
#df['num_assignmentSymbols'] = df['original_entry'].apply(lambda entry : count_assignmentSymbols(str(entry))) 

#df['original_entry'] = df['original_entry'].apply(lambda entry : add_hashtags_to_embedded_POS_tags(entry, tagging_dict))



# Apply the function to each row and explode the DataFrame
df['original_entry'] = df['original_entry'].apply(split_dictionary_entry_into_subentries)
df = df.explode('entry', ignore_index=True)
print(df.head(20))
df.to_excel("Talian_dictionary.xlsx", index=False)

universal_tagset = {
                    "#adj.": "ADJ",
                    "#adv." : "ADV",
                    "#s.m.": "NOUN",
                    "#s.f.": "NOUN",
                    "#v.trans." : "VERB",
                    "#v.intrans.": "VERB", 
                    "num" : "NUM",
                    "pron" : "PRON",
                    "interj." : "INTJ",
                    "Exc." : "INTJ",
                    "excL." : "INTJ",
                    "art." : "DET",
                    "prep." : "ADP"
                    }




