from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import os
import uuid


class File_manager:
    def __init__(self, local_path: str, account_url: str, container_name: str) -> None:
        self.local_path = local_path
        self.account_url = account_url
        self.container_name = container_name
        self.credential = DefaultAzureCredential()

    def read_all_file(self):
        blob_service_client = BlobServiceClient(
            self.account_url,
            credential=self.credential
        )
        container_client = blob_service_client.get_container_client(
            container=self.container_name
        )

        blob_list = container_client.list_blobs()

        return blob_list

    def read_file(self):
        pass

    def upload_file(self):
        pass

    def update_file(self):
        pass

    def delete_file(self):
        pass


try:
    file_manager = File_manager(
        local_path="./uploads",
        account_url="https://image0330.blob.core.windows.net",
        container_name="image0330"
    )

    list = file_manager.read_all_file()

    for li in list:
        # print(li.name)
        # print(li.container)
        print(
            f"https://image0330.blob.core.windows.net/{li.container}/{li.name}"
        )

except Exception as e:
    print(f"Error:{e}")
