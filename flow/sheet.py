import gspread

## Connecting through the GCP json creds
sa = gspread.service_account(filename="service_account.json")

## Sheet name
sh = sa.open("pythontwitter")

## Worksheet name
wks = sh.worksheet("Sheet1")

