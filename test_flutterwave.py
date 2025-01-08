import requests
import os
from dotenv import load_dotenv
import django
import sys
from pathlib import Path

# Add your project's root directory to Python path
sys.path.append(str(Path(__file__).parent))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'holdingcore.settings')  # Changed from 'your_project' to 'holdingcore'
django.setup()

from django.conf import settings

def test_flutterwave_credentials():
    """Test Flutterwave API credentials and connection"""
    
    # Get credentials from Django settings
    secret_key = settings.FLUTTERWAVE_SECRET_KEY
    base_url = settings.FLUTTERWAVE_BASE_URL
    
    print("\n=== Flutterwave API Credential Test ===")
    print(f"Secret Key starts with: {secret_key[:8]}... ends with: {secret_key[-4:]}")
    print(f"Base URL: {base_url}")
    
    headers = {
        "Authorization": f"Bearer {secret_key}",
        "Content-Type": "application/json"
    }
    
    try:
        # Test banks endpoint
        print("\nTesting API connection...")
        response = requests.get(
            f"{base_url}/banks/NG",
            headers=headers
        )
        
        print(f"\nResponse Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("\n✅ API Connection Successful!")
            print("Your Flutterwave credentials are working correctly.")
            return True
        else:
            print("\n❌ API Connection Failed!")
            print(f"Error Response: {response.text}")
            return False
            
    except Exception as e:
        print("\n❌ Connection Error!")
        print(f"Error Details: {str(e)}")
        return False

if __name__ == "__main__":
    print("\nStarting Flutterwave API Test...")
    test_flutterwave_credentials()