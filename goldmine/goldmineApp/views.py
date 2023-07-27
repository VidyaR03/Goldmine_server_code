from django.shortcuts import render

# Create your views here.

from . modules . Admin . admin import *
from . modules . Dashboard . dashboard import *

## View path of python file included in Masters folder

from . modules . Masters . masters import *
from . modules . Masters . group import *
from . modules . Masters . accounts import *
from . modules . Masters . branch import *
from . modules . Masters . vehicle import *
from . modules . Masters . location import *
from . modules . Masters . pay_type import *
from . modules . Masters . driver import *
from . modules . Masters . city import *
from . modules . Masters . delivery_type import *
from . modules . Masters . consignee import *
from . modules . Masters . consignor import *
from . modules . Masters . expence import *



## View path of python file included in Operational folder


from . modules . Operations . operations import *
from . modules . Operations . pickup_requests import *
from . modules . Operations . consignment_no import *
from . modules . Operations . pickup_runsheet_views import *
from . modules . Operations . manifestload import *
from . modules . Operations . tripsheet import *
from . modules . Operations . manifestunload import *
from . modules . Operations . delivery_runsheet import *
from . modules . Operations . invoice_views import *
from . modules . Operations . delivery_runsheet import *


## View path of python file included in Finance folder


from . modules . Finance . add_voucher import *
from . modules . Finance . listing_voucher import *
from . modules . Finance . ledger import *
from . modules . Finance . trial_balance import *
from . modules . Finance . profit_loss import *
from . modules . Finance . balance_sheet import *





