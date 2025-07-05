#!/usr/bin/env python3
"""
Script de debug pour tester l'accès au site et les cookies CSRF
"""

import requests
import sys
from urllib.parse import urljoin

def test_csrf_access(base_url):
    print(f"Testing CSRF access to {base_url}")
    
    # Create a session to maintain cookies
    session = requests.Session()
    
    try:
        # First, get the login page to obtain CSRF token
        print("\n1. Getting login page...")
        response = session.get(urljoin(base_url, '/login/'))
        print(f"Status: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        
        # Check for CSRF cookie
        csrf_cookie = None
        for cookie in session.cookies:
            if cookie.name == 'csrftoken':
                csrf_cookie = cookie.value
                break
                
        if csrf_cookie:
            print(f"CSRF Cookie found: {csrf_cookie[:10]}...")
        else:
            print("WARNING: No CSRF cookie found!")
            
        # Look for CSRF token in HTML
        if 'csrfmiddlewaretoken' in response.text:
            print("CSRF token found in HTML form")
        else:
            print("WARNING: No CSRF token found in HTML!")
            
        # Try to get CSRF token from response content
        import re
        csrf_pattern = r'name=["\']csrfmiddlewaretoken["\'] value=["\']([^"\']+)["\']'
        match = re.search(csrf_pattern, response.text)
        
        if match:
            csrf_token = match.group(1)
            print(f"CSRF Token extracted: {csrf_token[:10]}...")
            
            # Now try a simple form submission
            print("\n2. Testing form submission...")
            
            login_data = {
                'csrfmiddlewaretoken': csrf_token,
                'login': 'test_user',
                'password': 'test_password'
            }
            
            headers = {
                'Referer': urljoin(base_url, '/login/'),
                'X-CSRFToken': csrf_token
            }
            
            response = session.post(
                urljoin(base_url, '/login/'),
                data=login_data,
                headers=headers,
                allow_redirects=False
            )
            
            print(f"Form submission status: {response.status_code}")
            if response.status_code == 403:
                print("CSRF verification failed!")
                print(f"Response content: {response.text[:500]}...")
            elif response.status_code in [200, 302]:
                print("Form submission successful (CSRF OK)")
            else:
                print(f"Unexpected status code: {response.status_code}")
                
        else:
            print("Could not extract CSRF token from HTML")
            
    except Exception as e:
        print(f"Error during test: {e}")

if __name__ == "__main__":
    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://172.16.10.30:3000"
    test_csrf_access(base_url)
