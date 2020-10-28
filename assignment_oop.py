
from pandas import DataFrame


class DataFrameProcessor():
    def __init__(self, df):
        self.df = df

    def add_state_names(self):
        """
        add a column of corresponding state names to dataframe
        params(my_df) is a dataframe with "abbrev" column
        return copy of df with state name column
        """
        names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
        self.df["name"] = self.df["abbrev"].map(names_map)


if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "DC", "TX"]})
    processor = DataFrameProcessor(df=df)
    print(processor.df.head())
    processor.add_state_names()
    print(processor.df.head())
