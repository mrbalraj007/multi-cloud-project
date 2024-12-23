from azure.storage.blob import BlobClient

# Replace with your SAS URL
sas_url = "https://automatingstuffsairaj.blob.core.windows.net/tfstate/terraform.tfstate?sp=r&st=2024-12-15T09:15:36Z&se=2025-01-11T17:15:36Z&spr=https&sv=2022-11-02&sr=b&sig=tlVwpW%2By97Lj6mOd%2F9xeqnfpTj1PakV1CLUTSrZexZk%3D"
local_file_path = "state_file.tfstate"  # Path to save the downloaded file

try:
    # Create a BlobClient using the SAS URL
    blob_client = BlobClient.from_blob_url(sas_url)

    # Download the blob content to a local file
    with open(local_file_path, "wb") as download_file:
        download_stream = blob_client.download_blob()
        download_file.write(download_stream.readall())

    print(f"State file downloaded successfully to {local_file_path}")

except Exception as e:
    print(f"Failed to download state file: {e}")