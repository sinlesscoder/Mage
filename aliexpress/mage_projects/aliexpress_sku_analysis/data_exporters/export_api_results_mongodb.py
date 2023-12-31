from datetime import datetime
from pymongo import MongoClient
from json_read import json_reader

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


# Helper Function: Connecting to Mongo
def retrieve_mongo_connection(search_term: str):
    """
    Inputs:
        - search_term (string): Search term for the query of API
        - uri (string): Uniform Resource Identifier to represent MongoDB server
    
    Output:
        - collection_name (Mongo.Collection): Collection to store your results.
    """
    uri = json_reader("URI")

    # Set up a Mongo Client
    client = MongoClient(uri)

    # Select a database
    database = client['aliexpress_items']

    # Select a collection
    collection_name = database[search_term]

    return collection_name

# Prepare Data
def prepare_data_mongo(search_term: str, api_result: dict):
    """
    Inputs:
        - search_term (string): Search query for item information
    Output:
        - result_dict (dictionary): Dictionary containing key, 
            values of page number mapped to actual JSON result
    """
    # Get results
    results = api_result[search_term]

    return results

def db_load(search_term: str,api_result:dict):
    """
    Inputs:
        - search_term (string)
    Output:
        - result_dict (dictionary): Dictionary containing results
            with pages as keys
    """
    # Get the Mongo collection
    collection_name = retrieve_mongo_connection(search_term)

    # Get the result dictionary
    results = api_result[search_term]
    # Convert above into a dictionary
    result_dict = {f"{i+1}" : result for i, result in enumerate(results)}
    # Getting current date time as a string
    result_dict['updated_at'] = str(datetime.now())

    # Insert the Dictionary as an Object in the MongoDB Collection
    collection_name.insert_one(result_dict)

    return result_dict


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source

    Args:
        args: The input variables from upstream blocks

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    for term in data:
        db_load(term,data)

