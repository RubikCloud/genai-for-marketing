import json
DATASET_ID = "gai_marketing"

events_columns = [
    ("customer_id", "Unique ID for the customer."),
    ("event_id", "Unique ID for the event."),
    ("event_date", "Date for the event"),
    ("event_type", "Type of the event. Some examples are:"
     """gridMarcasHomeButton
app: usuario inicio app
mpo - salida del navegador
registro: usuario valido OTP
agregarCashbackListaDeCompras
app: usuario inicio sesion app
registro: usuario solicito OTP
trivia: usuario completo trivia
""")
]

customers_table = [
    ("id_campaign", "The ID of the campaign that targeted the user"),
    ("brancht_id", "The ID of the point of sale. Note the typo in 'brancht'"),
    ("customer_id", "ID of the customer"),
    ("email", "Email of the customer"),
    ("city", "The city of the customer"),
    ("state", "The state where the customer lives in"),
    ("channel", "The channel the customer uses. Either 'Email' or 'SMS'"),
    ("total_purchases", "Total amount bought"),
    ("total_value", "the value of the customer"),
    ("total_emails", "the amount of emails sent to the customer"),
    ("loyalty_score", "the loyalty score computed by the CRM"),
    ("is_media_follower", "Is the customer a media follower?"),
    ("last_sign_up_date", "self explanatory"),
    ("last_purchase_up_date", "self explanatory"),
    ("last_activity_up_date", "self explanatory"),

]


transactions_table = [
    ("transaction_id", "self explanatory"),
    ("customer_id", "self explanatory"),
    ("transaction_quantity", "self explanatory"),
    ("transaction_value", "self explanatory"),
    ("transaction_type", "One of: carga,anulacion,vencimiento,banderazo,promocion,redencion,regalo_comercio,regalo"),
    ("app_purchase_quantity", "self explanatory"),
    ("is_online", "was the sale online?"),
    ("transaction_date", "self explanatory"),
    ("product_name", "self explanatory"),
    ("product_id", "self explanatory"),
]

with open("metadata-out.json", "w") as j:
    trs = [{"dataset_id": DATASET_ID, "table_id": "transactions", "column_id": e[0],
            "description": e[1], "is_primary_key": False, "is_foreign_key": False} for e in transactions_table]
    cst = [{"dataset_id": DATASET_ID, "table_id": "customers", "column_id": e[0],
            "description": e[1], "is_primary_key": False, "is_foreign_key": False} for e in customers_table]
    jj = json.dump(trs+cst, j)


# {
#     "dataset_id": DATASET_ID,
#     "table_id": "events",
#     "column_id": "event_id",
#     "description": "A unique identifier for the event.",
#     "is_primary_key": "true",
#     "is_foreign_key": "false"
# }
