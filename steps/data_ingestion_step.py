import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from src.ingest_data import DataIngestorFactory
from zenml import step


@step
def data_ingestion_step(file_path: str) -> pd.DataFrame:
    """Ingest data from a ZIP file using the appropriate DataIngestor."""
    # Determine the file extension
    file_extension = ".zip"  # Since we're dealing with ZIP files, this is hardcoded

    # Get the appropriate DataIngestor
    data_ingestor = DataIngestorFactory.get_file_extension(file_extension)

    # Ingest the data and load it into a DataFrame
    df = data_ingestor.DataIngest(file_path)
    return df
