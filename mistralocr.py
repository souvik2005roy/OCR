from mistralai import Mistral
from mistralai import DocumentURLChunk, ImageURLChunk, TextChunk
import json
from pathlib import Path

pdf_file = Path("C:/Users/souvi/OneDrive/Pictures/Screenshots/Screenshot 2025-05-17 182350.png")
client = Mistral(api_key="2rbvMHihgzLHRZmKujoTUUjMi4CvdmQj")
uploaded_file = client.files.upload(
      file={
          "file_name": pdf_file.stem,
          "content": pdf_file.read_bytes(),
      },
      purpose="ocr",
  )
 
signed_url = client.files.get_signed_url(file_id=uploaded_file.id, expiry=1)
 
pdf_response = client.ocr.process(document=DocumentURLChunk(document_url=signed_url.url), model="mistral-ocr-latest", include_image_base64=True)
 
response_dict = pdf_response.model_dump()
print(response_dict)
