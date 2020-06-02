
from pandas import DataFrame




# Helper Functions for Assignment
#State abbreviation -> Full Name and visa versa. FL -> Florida, etc. 
#(Handle Washington DC and territories like Puerto Rico etc.)

def add_state_names_column(my_df):
    """
    Add a column of correspondingstate names to a dataframe.

    Params (my_df) a DataFrame with a column called "abbrev" that has abbreviations

    Return a copy of original dataframe, with an extra column.
    """
    new_df = my_df.copy()

    names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}

    new_df["name"] = new_df["abbrev"].map(names_map)

    #new_new_df

    return new_df

if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())
    
    mapped_df = add_state_names_column(df)
    print(mapped_df.head())

    df2 = DataFrame({"other_col": [1,2,3]})
    df2.head()
    
    breakpoint()