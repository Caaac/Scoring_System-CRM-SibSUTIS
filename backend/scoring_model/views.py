from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import date, datetime
import pickle
import pandas as pd
from api.models import Company, LandingRate, CrmDeal, Users
from api.serializers import CompanySerializer, ContactSerializer, CrmDealSerializer, LandingRateSerializer, StatementSerializer, UsersSerializer

def update_scoring_rate(request, pk):
    if request.method == 'POST':
        try:
            deal = CrmDeal.objects.get(pk=pk)
            contact = deal.contact

            age = None
            if contact.birth_date:
                today = date.today()
                age = today.year - contact.birth_date.year - ((today.month, today.day) < (contact.birth_date.month, contact.birth_date.day))

            month = datetime.now().month

            count_deal_empty_date_closed = CrmDeal.objects.filter(contact=contact, date_closed__isnull=True).count()
            annual_income = deal.annual_income if deal.annual_income is not None else -1
            loan_type = deal.loan_type if deal.loan_type is not None else -1
            monthly_salary = deal.monthly_salary if deal.monthly_salary is not None else -1
            
            if annual_income < 0:
                return JsonResponse({'status': 'error', 'message': 'Annual income cannot be negative.'}, status=400)  
            if loan_type < 0:
                return JsonResponse({'status': 'error', 'message': 'Loan type cannot be negative.'}, status=400)  
            if monthly_salary < 0:
                return JsonResponse({'status': 'error', 'message': 'Loan type cannot be negative.'}, status=400)  


            count_deal = CrmDeal.objects.filter(contact=contact).count()

            new_data = pd.DataFrame({
                'Month': [month],
                'Age': [age],
                'Annual_Income': [annual_income],
                'Num_Credit_Inquiries': [count_deal],
                'Monthly_Inhand_Salary': [monthly_salary], 
                'Num_of_Loan': [count_deal_empty_date_closed],  
                'Type_of_Loan': [loan_type],
            })
            
            try:
                with open('../model/saved_model/model.pkl', 'rb') as model_file:
                    model = pickle.load(model_file)
                    predictions = model.predict(new_data)

                CrmDeal.objects.filter(pk=pk).update(scoring_result=predictions[0][0])

                return JsonResponse({
                    'status': 'success',
                    'data': predictions[0][0]
                })

            except FileNotFoundError:
                return JsonResponse({'status': 'error', 'message': 'Model file not found.'}, status=404) 

        except CrmDeal.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Deal not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'}, status=405)