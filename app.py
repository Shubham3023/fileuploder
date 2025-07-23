import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError
import os



# AWS credentials from environment or ~/.aws/credentials
s3 = boto3.client('s3')
bucket_name = "myawsuploadstreamlit"

st.title("📤 Upload to AWS S3")

uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_content = file.read()
        s3.upload_fileobj(file, bucket_name, file.name)
        st.success(f"Uploaded {file.name} to S3 bucket '{bucket_name}'")