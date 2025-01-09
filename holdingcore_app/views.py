from django.http import HttpResponse
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import time
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Program, Blog
from django.core.paginator import Paginator

import requests
import json
import uuid
import time
from django.shortcuts import render, redirect
from django.conf import settings
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.


def home(request):
    return render(request, 'holdingcore_app/index.html')

def about(request):
    return render(request, 'holdingcore_app/about.html')

def causes(request):
    return render(request, 'holdingcore_app/causes.html')


def programs(request):
    programs_list = Program.objects.all()
    paginator = Paginator(programs_list, 5)  # Display 4 programs per page

    page_number = request.GET.get('page')  # Get the current page number from query parameters
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj  # Pass the page object to the template
    }
    return render(request, 'holdingcore_app/programs.html', context)


def volunteer(request):
    return render(request, 'holdingcore_app/volunteer.html')


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog(request):
    blogs_list = Blog.objects.all()  # Fetch all blog posts
    paginator = Paginator(blogs_list, 9)  # Display 9 blogs per page

    page_number = request.GET.get('page')  # Get the page number from query params
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)  # Default to the first page if page is not an integer
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)  # Default to the last page if page exceeds bounds

    context = {
        'page_obj': page_obj  # Pass the page object to the template
    }
    return render(request, 'holdingcore_app/blog.html', context)


def event_gallery(request):
    return render(request, 'holdingcore_app/event_gallery.html')


def guidelines(request):
    return render(request, 'holdingcore_app/guidelines.html')

def donate(request):
    return render(request, 'holdingcore_app/donate.html')


def contact(request):
    return render(request, 'holdingcore_app/contact.html')






#---------------------------------------------
    ## FlutterWave Payment Intergrations ## 
#------------------------------------------------

logger = logging.getLogger(__name__)

def initialize_payment(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            amount = request.POST.get('amount', '').strip()
            currency = request.POST.get('currency', '').strip()

            # Debug print
            print(f"\n=== Payment Initialization Debug ===")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Amount: {amount}")
            print(f"Currency: {currency}")

            # Generate reference
            tx_ref = f"TX{int(time.time())}"

            # Construct payment data
            payment_data = {
                "tx_ref": tx_ref,
                "amount": amount,
                "currency": currency,
                "redirect_url": "https://3bef-197-211-59-130.ngrok-free.app/verify-payment/",  # Make sure this matches your URL
                "meta": {
                    "consumer_id": 23,
                    "consumer_mac": "92a3-912ba-1192a"
                },
                "customer": {
                    "email": email,
                    "phonenumber": "080****4528",
                    "name": name
                },
                "customizations": {
                    "title": "Holdingcore Donation",
                    "description": "Donation Payment",
                    "logo": "https://assets.piedpiper.com/logo.png"
                }
            }

            # Debug print the request data
            print("\n=== Request Data ===")
            print(f"Endpoint: {settings.FLUTTERWAVE_BASE_URL}/payments")
            print(f"Headers: Authorization: Bearer ...{settings.FLUTTERWAVE_SECRET_KEY[-4:]}")
            print(f"Payload: {json.dumps(payment_data, indent=2)}")

            headers = {
                "Authorization": f"Bearer {settings.FLUTTERWAVE_SECRET_KEY.strip()}",
                "Content-Type": "application/json",
            }

            # Make request with debug output
            print("\n=== Making Request ===")
            response = requests.post(
                f"{settings.FLUTTERWAVE_BASE_URL.strip()}/payments",
                json=payment_data,
                headers=headers,
                timeout=30
            )

            # Debug print the response
            print("\n=== Response Debug ===")
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {dict(response.headers)}")
            print(f"Response Body: {response.text}")

            if response.status_code == 200:
                response_data = response.json()
                if response_data.get('status') == 'success':
                    payment_link = response_data['data']['link']
                    return redirect(payment_link)
                else:
                    error_message = response_data.get('message', 'Payment initialization failed')
            else:
                try:
                    error_data = response.json()
                    error_message = f"Error: {error_data.get('message', 'Unknown error')}"
                except:
                    error_message = f"Status {response.status_code}: {response.text}"

            # If we got here, something went wrong
            print(f"\nError Message: {error_message}")
            return render(request, 'holdingcore_app/payment_error.html', {
                'error_message': error_message,
                'technical_details': f"Status: {response.status_code}, Response: {response.text[:200]}"
            })

        except Exception as e:
            print(f"\nException occurred: {str(e)}")
            return render(request, 'holdingcore_app/payment_error.html', {
                'error_message': f"An error occurred: {str(e)}"
            })

    return render(request, 'holdingcore_app/donate.html')


def verify_payment(request):
    transaction_id = request.GET.get('transaction_id')
    headers = {
        "Authorization": f"Bearer {settings.FLUTTERWAVE_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.get(
        f"{settings.FLUTTERWAVE_BASE_URL}/transactions/{transaction_id}/verify",
        headers=headers
    )

    response_data = response.json()

    if response_data.get('status') == 'success' and response_data['data']['status'] == 'successful':
        # Render success template with transaction details
        return render(request, 'holdingcore_app/payment_success.html', {
            'transaction': response_data['data']
        })
    else:
        # Render failure template with transaction details
        return render(request, 'holdingcore_app/payment_failed.html', {
            'transaction': response_data.get('data', {}),
            'error_message': response_data.get('message', 'Payment verification failed.')
        })
        
#---------------------------------------------
    ## FlutterWave Payment Intergrations END ## 
#------------------------------------------------



