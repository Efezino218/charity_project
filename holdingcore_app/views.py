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







# Secret API key for Flutterwave (Test mode)
# def process_donation(request):
#     if request.method == "POST":
#         # Get form data
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         amount = request.POST.get("amount")
#         currency = request.POST.get("currency")

#         # Flutterwave API endpoint
#         url = "https://api.flutterwave.com/v3/payments"

#         # Request payload
#         payload = {
#             "tx_ref": f"donation_{name}_{amount}",
#             "amount": amount,
#             "currency": currency,
#             "redirect_url": request.build_absolute_uri('/donation-success/'),  # Redirect after payment
#             "customer": {
#                 "email": email,
#                 "name": name,
#             },
#             "customizations": {
#                 "title": "Charity Donation",
#                 "description": "Donation for helping needy people."
#             },
#         }

#         # Headers with the secret key
#         headers = {
#             "Authorization": f"Bearer {settings.FLW_SECRET_KEY}",
#             "Content-Type": "application/json",
#         }

#         # Send POST request to Flutterwave
#         response = requests.post(url, json=payload, headers=headers)
#         response_data = response.json()

#         # Redirect to payment link if successful
#         if response_data["status"] == "success":
#             payment_link = response_data["data"]["link"]
#             return redirect(payment_link)

#         return JsonResponse({"error": "Payment initialization failed."}, status=400)

#     return JsonResponse({"error": "Invalid request method."}, status=405)

# def donation_success(request):
#     return render(request, "donation_success.html")





# Set up your Flutterwave API credentials
# FLW_PUBLIC_KEY = "FLWPUBK_TEST-993473418a25acd957bfeae3e5db3ffc-X"
# FLW_SECRET_KEY = "FLWSECK_TEST-643ba6ecea228bb2615a06892d6a50ea-X"
# FLW_ENCRYPTION_KEY = "FLWSECK_TESTa818b743b7c1"

# @csrf_exempt
# def process_donation(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         amount = request.POST.get('amount')
#         currency = request.POST.get('currency')

#         # Step 1: Set up the payment request data
#         data = {
#             "tx_ref": "txn" + str(int(time.time())),  # Unique transaction reference
#             "amount": amount,
#             "currency": currency,
#             "payment_type": "card",  # You can change to other types (e.g., bank, wallet)
#             "email": email,
#             "phone_number": "",  # Optional: collect phone number if needed
#             "order_id": "order12345",  # Optional: Track orders
#         }

#         # Step 2: Make the API request to Flutterwave
#         headers = {
#             "Authorization": f"Bearer {FLW_SECRET_KEY}",
#         }

#         response = requests.post(
#             "https://api.flutterwave.com/v3/charges?order_id=order12345",  # Flutterwave API endpoint
#             headers=headers,
#             data=data
#         )
        
#         # Step 3: Handle the response
#         response_data = response.json()

#         if response_data['status'] == 'success':
#             # Redirect to Flutterwave checkout page for the user to complete payment
#             payment_link = response_data["data"]["payment_url"]
#             return redirect(payment_link)
#         else:
#             return JsonResponse({"message": "Error processing donation, please try again."})

#     return render(request, 'holdingcore_app/donate.html')  # Update with your actual template name



# def payment_response(request):
#     # Check the payment status from the GET parameters (Flutterwave sends this)
#     payment_status = request.GET.get("status")

#     if payment_status == "successful":
#         return render(request, 'holdingcore_app/donation_success.html')  # Success page
#     else:
#         return render(request, 'holdingcore_app/donation_failed.html')  # Failure page




import requests
import json
import uuid
import time
from django.shortcuts import render, redirect
from django.conf import settings
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
