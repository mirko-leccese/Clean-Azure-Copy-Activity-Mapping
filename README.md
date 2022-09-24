# Clean-Azure-Copy-Activity-Mapping

Azure Data Factory and Azure Synapse Pipelines **Copy Activity** fails whenever you are trying to copy tables into Azure Data Lake Storage Gen2 in Parquet file format and your column headers contain characters such as whitespaces, brackets, etc. To avoid such error, you need to remove these undesired characters on the sink side when specifying the schema mapping. In case of tables with several columns, this operation may be tedious. 

This simple Python script reads a JSON file specifying the schema mapping and cleans column headers from undesired characters. The typical structure of such a JSON file is:

```json
{
    "translator": {
        "type": "TabularTranslator",
        "mappings": [
            {
                "source": "customer id",
                "sink": "customer id"
            },
            {
                "source": "orders",
                "sink": "orders"
            }
        ]
    }
}
```

The script produces a new JSON called *filename_Cleaned.json* where any ```sink```field from the ```mappings```array has been cleaned. 

# Installation
No installation required. To run the script, type:

```bash
./clean_azure_copy_mapping.py 
```

and answer the question asking for the JSON filename. 