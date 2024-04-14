import requests
import os
import zipfile

def download_file(url, filename):
  """Downloads a file from the given URL and saves it as filename."""
  response = requests.get(url)
  if response.status_code == 200:
    with open(filename, 'wb') as f:
        #print(f"response content is {response.content}")
        f.write(response.content)
    return True
  else:
    print(f"Download failed with status code: {response.status_code}")
    return False

def extract_archive(filename, output_dir):
  """Extracts the downloaded archive and saves any .exe file."""
  try:
    with zipfile.ZipFile(filename, 'r') as zip_ref:
      for member in zip_ref.namelist():
        if member.endswith('.exe'):
          # Extract the .exe file to the specified output directory
          zip_ref.extract(member, output_dir)
          print(f".exe file extracted and saved to: {output_dir}/{member}")
          break  # Stop after saving the first .exe (if multiple exist)
  except zipfile.BadZipFile:
    print(f"Error: Downloaded file is not a valid zip archive.")
  except FileNotFoundError:
    print(f"Error: Downloaded file not found.")
  except OSError as e:
    print(f"Error during extraction: {e}")


# Replace placeholders with actual values
download_url = "https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.105/win32/chromedriver-win32.zip"
download_filename = "chromedriver.zip"
output_dir = "extracted_files"  # Change this to your desired output directory

if download_file(download_url, download_filename):
  print(f"Download complete! File saved as: {download_filename}")
  extract_archive(download_filename, output_dir)
else:
  print("Download failed!")
