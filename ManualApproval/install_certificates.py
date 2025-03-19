import os
import ssl
import subprocess
import sys

def install_certificates():
    # Get the default SSL certificate file path
    cert_file = ssl.get_default_verify_paths().openssl_cafile

    # Install or upgrade the 'certifi' package
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "certifi"])

    # Get the path to the 'certifi' certificate bundle
    import certifi
    certifi_cafile = certifi.where()

    # Remove any existing certificate file
    if os.path.exists(cert_file):
        os.remove(cert_file)

    # Create a symlink to the 'certifi' certificate bundle
    os.symlink(certifi_cafile, cert_file)
    print(f"SSL certificates have been installed successfully at {cert_file}")

if __name__ == "__main__":
    install_certificates()
