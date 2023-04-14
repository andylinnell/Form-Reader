import json
# import azure form recognizer libraries
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential


key = "7b386e5b451d48e78dd7faea127db015"
endpoint = "https://formrecognizerandylinnell.cognitiveservices.azure.com/"

# create the client and authenticates with the endpoint and key
form_recognizer_client = FormRecognizerClient(endpoint, AzureKeyCredential(key))

myReceiptUrl = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/receipt/contoso-receipt.png"

# user form recognizer client to recognize image from myReceiptUrl
poller = form_recognizer_client.begin_recognize_receipts_from_url(myReceiptUrl)
result = poller.result()

# loop through results and extract data from receipt
for receipt in result:
    for name, field in receipt.fields.items():
        # each field is of type FormField
        # label_data is populated if you are using a model trained without labels,
        # since the service needs to make predictions for labels if not explicitly given to it.
        if field.label_data:
            print("...found label '{}' with value '{}' within '{}'".format(field.label_data.text, field.value, name))
        else:
            print("...found '{}' with value '{}'".format(name, field.value))
