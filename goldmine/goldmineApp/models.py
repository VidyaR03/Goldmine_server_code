from django.db import models


class Branch(models.Model):
    '''
    Branch class for to store the data of branch.
    '''
    s_Branch_Address = models.CharField(max_length=250)
    s_Branch_City = models.CharField(max_length=50)
    s_Branch_State = models.CharField(max_length=50)
    s_Status = models.BooleanField(default=0)


    def __str__(self):
        return f"{self.s_Branch_City}"
    
    class Meta:
        db_table = 'Branch'
        ordering = ['-id'] 





class Roles(models.Model):
    """This is Model for role_permission"""
    s_Role_Name=models.CharField(max_length = 200, unique=True)

    def __str__(self):
        return f"{self.s_Role_Name}"
    
    class Meta:
        db_table = 'Roles'
        ordering = ['-id'] 


class Group(models.Model):
    '''
    Group class for to store data of groups.
    '''
    s_Group_Name = models.CharField(max_length=100)
    s_Date = models.DateField()
    s_Status = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.s_Group_Name}"
    
    class Meta:
        db_table = 'Group'
        ordering = ['-id'] 




class Accounts(models.Model):
    '''
    Accounts class for to store the data of accounts.
    '''
    s_Group = models.ForeignKey(Group,on_delete=models.CASCADE)
    s_Company_Name = models.CharField(max_length=100)
    s_First_Name = models.CharField(max_length=50)
    s_Last_Name = models.CharField(max_length=50)
    i_Mobile_Number = models.CharField(max_length=50)
    i_Phone_Number = models.CharField(max_length=50)
    s_Email_Id = models.EmailField()
    s_Address = models.CharField(max_length=100)
    s_City = models.CharField(max_length=50)
    s_State = models.CharField(max_length=50)
    i_PinCode = models.PositiveBigIntegerField()
    i_Fax_Number = models.PositiveBigIntegerField()
    s_GST_Number = models.CharField(max_length=50)
    s_PAN_Number = models.CharField(max_length=50)
    s_Status = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.s_Company_Name}"
    
    class Meta:
        db_table = 'Accounts'
        ordering = ['-id'] 




class Driver(models.Model):
    '''
    Driver class for add the new driver.
    '''
    s_driver_name = models.CharField(max_length=50)
    s_date_of_birth = models.DateField()
    s_address = models.CharField(max_length=250)
    s_city = models.CharField(max_length=20)
    s_state = models.CharField(max_length=20)
    i_mobile_number = models.CharField(max_length=50)
    s_licence_number = models.CharField(max_length=50)
    s_Status = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.s_driver_name}"
    
    

  
    
    class Meta:
        db_table = 'Driver'
        ordering = ['-id'] 



class Vehicle(models.Model):
    '''
    Vehicle class for add the new vehicle.
    '''
    s_vehicle_number = models.CharField(max_length=50,primary_key=True)
    s_vehicle_type = models.CharField(max_length=50)
    s_Driver_name =  models.ForeignKey( Driver, on_delete=models.CASCADE, null=True, blank=True)
    i_driver_mobile = models.CharField(max_length=50)
    s_owner_name = models.CharField(max_length=100)
    i_owner_mobile = models.CharField(max_length=50)
    s_owner_pan_number = models.CharField(max_length=50)
    s_Status = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.s_vehicle_number}"
    
    
    class Meta:
        db_table = 'Vehicle'
        



class Location(models.Model):
    '''
    Location class for add the new location
    '''
    s_Address = models.CharField(max_length=100)
    s_City = models.CharField(max_length=50)
    i_PinCode = models.PositiveBigIntegerField()


    
    class Meta:
        db_table = 'Location'
        ordering = ['-id'] 




class Expence(models.Model):
    '''
    Expence class for add the new expence.
    '''
    s_Expence = models.CharField(max_length=100,null=True)
    s_Date = models.DateField()
    s_Status = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.s_Expence}"
    
    class Meta:
        db_table = 'Expence'
        ordering = ['-id'] 





class Delivery_Type(models.Model):
    '''
    Delivery type class for add the type of delivery.
    '''
    s_Delivery_Type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.s_Delivery_Type}"
    
    class Meta:
        db_table = 'Delivery_Type'
        ordering = ['-id'] 





class Pay_Type(models.Model):
    '''
    Pay type class for add the type of payment
    '''
    s_Pay_Type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.s_Pay_Type}"
    

    class Meta:
        db_table = 'Pay_Type'
        ordering = ['-id'] 





class Lorry_Book(models.Model):
    '''
    Lorry_Book class for to store the data of lorry_books.
    '''
    s_Start = models.IntegerField(null=False)
    s_End = models.IntegerField(null=False)

    class Meta:
        db_table = 'Lorry_Book'



class City(models.Model):
    '''
    City class for to store the data of city.
    '''
    s_City_Name = models.CharField(max_length=50)
    s_State= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.s_City_Name}"
    
    class Meta:
        db_table = 'City'
        ordering = ['-id'] 







class Consignee(models.Model):
    '''
    Pay type class for add the type of payment
    '''
    id = models.AutoField(primary_key=True, editable=False)
    s_Consignee_Name = models.CharField(max_length=50)
    s_Consignee_Address = models.CharField(max_length=50)
    s_Consignee_GST = models.CharField(max_length=50)
    i_Mobile_No = models.BigIntegerField()
    s_State = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.s_Consignee_Name}"
    


    class Meta:
        db_table = 'Consignee'
        ordering = ['-id'] 




class Consignor(models.Model):
    '''
    Pay type class for add the type of payment
    '''
    id = models.AutoField(primary_key=True, editable=False)
    s_Consignor_Name = models.CharField(max_length=50)
    s_Consignor_Address = models.CharField(max_length=50)
    s_Consignor_GST = models.CharField(max_length=50)
    i_Mobile_No = models.BigIntegerField()
    s_State = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.s_Consignor_Name}"
    


    class Meta:
        db_table = 'Consignor'
        ordering = ['-id'] 


class Pickup_Runsheet(models.Model): 
    s_vehicle_number= models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True)
    i_Pickup_Runsheet_No= models.BigIntegerField()
    s_Branch = models.CharField(max_length=100,null=True) 
    s_Date =models.DateField()
    i_PR_NO = models.CharField(max_length=100)
    s_Status = models.BooleanField(default=0)

    # pickup_requests = models.ManyToManyField(Pickup_Request, related_name='pickup_runsheets')
    
    def __str__(self):
        return f"{self.i_Pickup_Runsheet_No}"
    class Meta:
        db_table = 'Pickup_Runsheet'
        ordering = ['-id'] 





#########################################################################################################################################

class Pickup_Request(models.Model):
    '''
    For store the Pickup Request data.
    '''
    i_Pickup_Runsheet = models.ForeignKey(Pickup_Runsheet, on_delete=models.CASCADE, null=True, blank=True)

    s_Branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    s_Pay_Type = models.ForeignKey(Pay_Type,on_delete=models.CASCADE)
    s_Consignor_Name = models.ForeignKey(Consignor,on_delete=models.CASCADE, null=True,blank=True)
    s_Consignee_Name = models.ForeignKey(Consignee,on_delete=models.CASCADE, null=True,blank=True)  
    s_Date = models.DateField()
    i_PR_NO = models.CharField(max_length=100, null=False)  
    i_Pid_No =models.IntegerField(unique=True,null=False)
    i_No_of_Articles= models.IntegerField()
    s_Consignor_Address = models.CharField(max_length=100, null=True, blank=True)
    s_Consignor_GST =models.CharField(max_length=100, null=True, blank=True)
    s_Consignee_Address= models.CharField(max_length=100, null=True, blank=True)
    s_Consignee_GST =models.CharField(max_length=100, null=True, blank=True)
    s_From = models.CharField(max_length=100,null=True, blank=True)
    s_To = models.CharField(max_length=100)
    s_Description =models.CharField(max_length=200)
    i_Actual_Weight = models.IntegerField()
    i_Charged_Weight = models.IntegerField()
    i_Freight = models.IntegerField()
    i_FOV = models.IntegerField()
    i_Docket_Charge = models.IntegerField()
    i_Grant_Total = models.IntegerField()
    s_Remark = models.CharField(max_length=100)
    s_Vehicle = models.CharField(max_length=100, null=True, blank=True)
    s_Status = models.BooleanField(default=0)
    class Meta:
        db_table = 'Pickup_Request'
        ordering = ['-id'] 

   





class Manifest_UnLoad(models.Model):
    i_Manifest_Unload_No = models.BigIntegerField(null=True)
    # s_vehicle_number= models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True)
    consignmnet = models.ManyToManyField('Consignment_No')
    s_Manifest_No = models.CharField(max_length=100, null=False, blank=False)
    s_Branch = models.CharField(max_length=100,null=True)
    i_MR_NO = models.CharField(max_length=100,null=True)
    s_Date = models.DateField(null=True)
    s_Status = models.BooleanField(default=0)
 

    def __str__(self):
        return f"{self.i_Manifest_Unload_No}"
    
    class Meta:
        db_table = 'Manifest_UnLoad'
        ordering = ['-id'] 



class Delivery_Run(models.Model):
    i_Delivery_Runsheet_No=models.BigIntegerField()
    s_Branch = models.CharField(max_length=100,null=True) 
    s_vehicle_number = models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True)
    s_Date =models.DateField(null=True)
    s_From = models.CharField(max_length=100,null=True)
    s_To = models.CharField(max_length=100,null=True)
    s_driver_name = models.ForeignKey(Driver,on_delete=models.CASCADE)
    s_No_Delivery_Boy= models.IntegerField(null=True)
    s_Delivery_Boy_Name = models.CharField(max_length=100,null=True)
    i_Delivery_Boy_Phone_No = models.BigIntegerField(null=True)
    i_DR_No = models.CharField(max_length=100,null=True)
    i_Total_Amount = models.IntegerField(null=True)
    consignment_no = models.CharField(max_length=100,null=True)
    s_Status = models.BooleanField(default=0)


   
    class Meta:
        db_table = 'Delivery_Run'    
        ordering = ['-id']
        
        
class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Image'   



 
class Trip_Sheet(models.Model):
    '''
    This class create the trip sheet table
    '''
    i_Trip_Sheet_No = models.IntegerField(unique=True, null=False)
    i_TR_NO = models.CharField(max_length=100, null=False)

    s_Branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    s_To = models.CharField(max_length=50)
    s_Via = models.CharField(max_length=50)
    s_Vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True)
    s_Driver1 = models.ForeignKey(Driver,on_delete=models.CASCADE)
    s_Driver2 = models.CharField(max_length=100,null=True)
    i_Manifest_No = models.CharField(max_length=100,null=True)
    i_Total_Packages = models.IntegerField()
    i_Total_Weight = models.CharField(max_length=100)
    s_Start_Date = models.DateField(null=True, blank=True)
    s_End_Date = models.DateField(null=True,  blank=True)
    i_Loaded_Weight = models.CharField(max_length=100,null=True, blank=True)
    s_Party_Name = models.CharField(max_length=100,null=True, blank=True)
    i_Opening_KM = models.CharField(max_length=100,null=True, blank=True)
    s_Reach_Date = models.DateField(null=True, blank=True)
    s_Reach_Time = models.TimeField(null=True, blank=True)
    i_Closing_KM = models.CharField(max_length=100, blank=True)
    
    i_Total_Hours = models.CharField(max_length=100, blank=True)
    i_Disel_Issued = models.CharField(max_length=100, blank=True)
    i_Disel_Rate = models.CharField(max_length=100, blank=True)
    i_Average = models.CharField(max_length=100, blank=True)
    i_Advance_to_Driver = models.CharField(max_length=100,null=True, blank=True)
    s_Sign_of_Authority = models.CharField(max_length=100,null=True)
    
    i_Total_Disel_Qty = models.CharField(max_length=100, blank=True)
    i_Total_Running_KM = models.CharField(max_length=100, blank=True)
    i_Rate_Per_KM = models.CharField(max_length=100, blank=True)
    i_Total_Amt = models.CharField(max_length=100, blank=True)

    i_Disel = models.CharField(max_length=100,null=True, blank=True)
    i_Cash_Toll = models.CharField(max_length=100,null=True, blank=True)
    i_Entry_Tax = models.CharField(max_length=100,null=True, blank=True)
    i_Border_Tax = models.CharField(max_length=100,null=True, blank=True)
    i_Vehicle_Repair = models.CharField(max_length=100,null=True, blank=True)
    i_Loading_Unloading = models.CharField(max_length=100,null=True, blank=True)
    i_Others = models.CharField(max_length=100,null=True, blank=True)
    i_Total_Expence = models.CharField(max_length=100,null=True, blank=True)
    i_Advance = models.CharField(max_length=100,null=True, blank=True)
    i_Total_Amount = models.CharField(max_length=100,null=True, blank=True)

    i_Disel_LTRS = models.CharField(max_length=100,null=True, blank=True)
    i_Disel_Rate_Last = models.CharField(max_length=100,null=True, blank=True)
    i_Total_Disel_Cost = models.CharField(max_length=100,null=True, blank=True)

    s_Remark = models.CharField(max_length=500, blank=True)
    
 
    
    class Meta:
        db_table = 'Trip_Sheet'
        ordering = ['-id']
        

class Manifest_Load(models.Model):
    s_vehicle_number = models.CharField(max_length=100)
    i_Manifest_Int = models.BigIntegerField()
    s_Manifest_No = models.CharField(max_length=100, null=False, blank=False)
    s_Branch = models.CharField(max_length=100,null=True)
    s_Date = models.DateField(null=True)
    i_Package = models.BigIntegerField(null=True,blank=True)
    i_Weight = models.BigIntegerField(null=True,blank=True)
    s_Status = models.BooleanField(default=0)
    tripsheet = models.ForeignKey(Trip_Sheet,on_delete=models.CASCADE ,null=True, blank=True)
    def __str__(self):
        return f"{self.s_Manifest_No}"
    
    class Meta:
        db_table = 'Manifest_Load'
        ordering = ['-id']

class Invoice(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    s_Branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    i_Bill_No= models.CharField(max_length=100,null=True)
    i_Invoice_Bill=models.IntegerField(unique=True)
    s_Bill_Date=models.DateField()
    i_Total_Amount = models.IntegerField(null=True)
    s_GST_No=models.IntegerField(null=True)
    s_Company_GST_No = models.CharField(max_length=100,null=True)
    s_Company_Pan_No = models.CharField(max_length=100,null=True)
    s_Company_SAC_No = models.CharField(max_length=100,null=True)
    s_Consignor_Name = models.ForeignKey(Consignor,on_delete=models.CASCADE,null=True)
    s_Consignor_Address = models.CharField(max_length=100,null=True)
    s_Consignor_GST =models.CharField(max_length=100,null=True)
    #s_State = models.CharField(max_length=100)
    i_Sub_Total = models.FloatField()
    s_GST= models.CharField(max_length=100,null=True)
    i_GST_Amount = models.FloatField(null=True)
    i_Total_Final_Amount = models.FloatField()
    s_Remark = models.CharField(max_length=100,null=True)
    s_Kind_Attention = models.CharField(max_length=100,null=True)
    i_Inv = models.CharField(max_length=100,null=True)
    s_Status = models.BooleanField(default=0)
    class Meta:
        db_table = 'Invoice'
        ordering = ['-id']

class Consignment_No(models.Model):
    '''
    For store the Consignment Data.
    '''
    i_Invoice_Bill = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    i_delivery_runsheet = models.ForeignKey(Delivery_Run, on_delete=models.CASCADE, null=True, blank=True, related_name='consignments')
    i_Pickup_Runsheet = models.ForeignKey(Pickup_Runsheet, on_delete=models.CASCADE, null=True, blank=True)
    i_Manifest_Unload_Int = models.ForeignKey(Manifest_UnLoad, on_delete=models.CASCADE, null=True, blank=True)
    i_Manifest = models.ForeignKey(Manifest_Load, on_delete=models.CASCADE, null=True, blank=True)
    s_Branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    s_Pay_Type = models.ForeignKey(Pay_Type,on_delete=models.CASCADE)
    s_Consignor_Name = models.ForeignKey(Consignor,on_delete=models.CASCADE, null=True,blank=True)
    s_Consignee_Name = models.ForeignKey(Consignee,on_delete=models.CASCADE, null=True,blank=True)
    s_Date = models.DateField()
    i_LR_NO = models.CharField(max_length=100, null=False)  
    i_Lid_No =models.IntegerField(unique=True,null=False)
    i_No_of_Articles= models.IntegerField()
    s_Consignor_Address = models.CharField(max_length=100)
    s_Consignor_GST =models.CharField(max_length=100)
    s_Consignee_Address= models.CharField(max_length=100)
    s_Consignee_GST =models.CharField(max_length=100)
    s_From = models.CharField(max_length=100,null=True)
    s_To = models.CharField(max_length=100)
    s_Description =models.CharField(max_length=200)
    i_Actual_Weight = models.IntegerField(null=True)
    i_Charged_Weight = models.IntegerField(null=True)
    i_Freight = models.IntegerField(null=True)
    i_FOV = models.IntegerField(null=True)
    i_Docket_Charge = models.IntegerField(null=True)
    i_Grant_Total = models.IntegerField(null=True)
    s_Remark = models.CharField(max_length=100)
    s_Vehicle = models.CharField(max_length=100, null=True, blank=True)
    s_Status = models.BooleanField(default=0)
    i_Mani_NO = models.CharField(max_length=100, null=True,blank=True)  
    i_Mani_Un_NO = models.CharField(max_length=100, null=True,blank=True)
    m_status = models.BooleanField(default=0)
  
    
    class Meta:
        db_table = 'Consignment_No'
        ordering = ['-id']     


      
        
class delivery_add_run(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    # deliver_run_name = models.ForeignKey(Delivery_Run,on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='consignments')
    i_consignment_no = models.ForeignKey(Consignment_No, on_delete=models.CASCADE,blank=True,null=True)
    s_perticular = models.CharField(max_length=100)
    s_consinee = models.CharField(max_length=100)
    i_weight = models.IntegerField()
    i_pkg = models.IntegerField()
    s_pay_type = models.CharField(max_length=100)
    i_amount = models.IntegerField()
    
    class Meta:
        db_table = 'delivery_add_run'
        ordering = ['-id'] 


       
# class Delivery_Runsheet(models.Model):
#     id = models.AutoField(primary_key=True, editable=False)
#     Delivery_Run_id = models.ForeignKey(Delivery_Run, on_delete=models.CASCADE, null=True, blank=True)
#     delivery_add_run_id = models.ForeignKey(delivery_add_run, on_delete=models.CASCADE, null=True, blank=True)
#     class Meta:
#         db_table = 'Delivery_Runsheet'




class add_voucher(models.Model):
    i_VR_NO = models.CharField(max_length=100, null=False)
    i_Vid_No = models.IntegerField()
    s_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    d_voucher_date = models.DateField()
    s_voucher_type = models.CharField(max_length=100)
    by_or_to = models.CharField(max_length=100)
    s_perticular = models.CharField(max_length=100,null=True)
    s_debit = models.CharField(max_length=100,null=True)
    s_credit = models.CharField(max_length=100,null=True)
    s_total_debit = models.CharField(max_length=100,null=True)
    s_total_credit = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = 'add_voucher'
        ordering = ['-id']


########  COde of ledger Account ####


# class LedgerGroup(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Ledger(models.Model):
    s_ledger_name = models.CharField(max_length=100)
    s_Group = models.ForeignKey(Group,on_delete=models.CASCADE)
    s_ac_name = models.CharField(max_length=100,null=True)
    s_ac_no = models.CharField(max_length=100,null=True)
    s_ifsc_code = models.CharField(max_length=100,null=True)
    s_swift_code = models.CharField(max_length=100, blank=True)
    s_bank_name = models.CharField(max_length=100,null=True)
    s_branch_name = models.CharField(max_length=100,null=True)
    t_branch_address = models.TextField(null=True)
    s_under = models.CharField(max_length=100,null=True)
    s_tax_type = models.CharField(max_length=100,null=True)
    d_percentage = models.CharField(max_length=100,null=True)
    d_rounding = models.CharField(max_length=100,null=True)
    s_name = models.CharField(max_length=100,null=True)
    t_address = models.TextField(null=True)
    i_mobile_no = models.BigIntegerField(null=True)
    s_state = models.CharField(max_length=100,null=True)
    s_country = models.CharField(max_length=100,null=True)
    d_date = models.DateField(null=True)



    def __str__(self):
        return self.s_ledger_name
    
    class Meta:
        db_table = 'Ledger'


class Trial_Balance(models.Model):
    s_Branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    s_ledger = models.ForeignKey(Ledger,on_delete=models.CASCADE,null=True)
    opening_debit = models.IntegerField()
    opening_credit = models.IntegerField()
    transaction_debit = models.IntegerField()
    transaction_credit = models.IntegerField()
    closing_debit = models.IntegerField()
    closing_credit = models.IntegerField()
    d_date = models.DateField(null=True)


    def __str__(self):
        return self.s_Branch
    
    class Meta:
        db_table = 'Trial_Balance'


class Profit_Loss(models.Model):
    s_Branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    income_perticular = models.CharField(max_length=100,null=True)
    income_perticular_amount = models.IntegerField()
    expense_perticular = models.CharField(max_length=100,null=True)
    expense_perticular_amount = models.IntegerField()

    def __str__(self):
        return self.income_perticular
    
    class Meta:
        db_table = 'Profit_Loss'

class Balance_Sheet(models.Model):
    s_Branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    liabilities = models.CharField(max_length=100,null=True)
    cr_amount = models.IntegerField()
    asset = models.CharField(max_length=100,null=True)
    dr_amount = models.IntegerField()

    def __str__(self):
        return self.liabilities
    
    class Meta:
        db_table = 'Balance_Sheet'












# class BankAccount(models.Model):
#     ledger = models.OneToOneField(Ledger, on_delete=models.CASCADE)
#     ac_name = models.CharField(max_length=100)
#     ac_no = models.CharField(max_length=100)
#     ifsc_code = models.CharField(max_length=100)
#     swift_code = models.CharField(max_length=100, blank=True)
#     bank_name = models.CharField(max_length=100)
#     branch_name = models.CharField(max_length=100)
#     branch_address = models.TextField()

#     def __str__(self):
        # return self.ac_name

# class GST(models.Model):
#     ledger = models.OneToOneField(Ledger, on_delete=models.CASCADE)
#     under = models.CharField(max_length=100)
#     tax_type = models.CharField(max_length=100)
#     percentage = models.DecimalField(max_digits=5, decimal_places=2)
#     rounding = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return str(self.ledger)


# class Account(models.Model):
#     ledger = models.OneToOneField(Ledger, on_delete=models.CASCADE)
#     ac_no = models.CharField(max_length=100)


#     def __str__(self):
#         return str(self.ledger)
    
# class MailingDetails(models.Model):
#     ledger = models.OneToOneField(Ledger, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     address = models.TextField()
#     mobile_no = models.PositiveIntegerField()
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name






        



          


 








       