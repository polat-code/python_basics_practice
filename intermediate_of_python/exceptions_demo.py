class MyCustomException(Exception):
    def __init(self,message: str):
        self.message = message
        super().__init__(self.message)


x : int = 10
if x > 5:
    raise MyCustomException("X should be less than 5")



from minio import Minio
from minio.error import S3Error

def generate_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

def file_exists(bucket_name, data, client):
    """
    Check if a file with the same content exists in the MinIO bucket.

    Parameters:
    - bucket_name: The name of the bucket.
    - data: Data bytes of the file to check.
    - client: Minio client instance.

    Returns:
    - True if a file with the same content exists, False otherwise.
    """
    hash_name = generate_hash(data)
    try:
        # Try to retrieve the object by hash name
        response = client.get_object(bucket_name, hash_name)
        file_data = response.read()

        # Compare data directly
        if file_data == data:
            return True
        else:
            return False
    except S3Error as e:
        if e.code == 'NoSuchKey':
            # The object does not exist
            return False
        else:
            # Handle other exceptions
            raise

# MinIO client setup
client = Minio(
    "your-minio-server.com",
    access_key="your-access-key",
    secret_key="your-secret-key",
    secure=True
)

# Usage example
bucket_name = "your-bucket-name"
data = b'Hello, world!'  # Example data

exists = file_exists(bucket_name, data, client)
print(f"File exists: {exists}")
