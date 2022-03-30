import os
import io
import json
import glob
from google.cloud import storage

META_BUCKET = "how-to-nfts-metadata"
client = storage.Client()
bucket = client.get_bucket(META_BUCKET)

os.chdir("metadata")
fn = "foo11.txt"
os.system("touch " + fn)
blob = bucket.blob(fn)
blob.upload_from_filename(fn)
os.chdir("..")

for blob in client.list_blobs(META_BUCKET):
  if "foo11_" in blob.name:
    blob.delete()
# end for blobs
