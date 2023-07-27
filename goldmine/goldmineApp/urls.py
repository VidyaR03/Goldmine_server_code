from django.urls import path
from . import views
from django.urls import path
from .views import ReportView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',views.fn_Login_User_View, name='login_user_url'),
    path('dashboard_view/',views.fn_Dashboard_View, name='dashboard_url'),


    path('',views.fn_Login_User_View, name='admin_login_url'),
    path('logout_admin/',views.fn_Logout_User_View, name='admin_logout_url'),


    path('masters_page/',views.fn_Masters_View, name='masters_url'),

    # Group urls
    path('group_add/',views.fn_Group_Add_View, name='group_add_url'),
    path('group_list/',views.fn_Group_List_View, name='group_list_url'),
    path('group_update/<int:id>/',views.fn_Group_Update_View, name='group_update_url'),
    path('group_delete/<int:id>/',views.fn_Group_Delete_View, name='group_delete_url'),

    # Account urls
    path('account_add/',views.fn_Account_Add_View, name='account_add_url'),
    path('account_list/',views.fn_Account_List_View, name='account_list_url'),
    path('account_details/<int:id>/',views.fn_Account_Details_View, name='account_details_url'),
    path('account_update/<int:id>/',views.fn_Account_Update_View, name='account_update_url'),
    path('account_delete/<int:id>/',views.fn_Account_Delete_View, name='account_delete_url'),

    # Branch urls
    path('branch_add/',views.fn_Branch_Add_View, name='branch_add_url'),
    path('branch_list/',views.fn_Branch_List_View, name='branch_list_url'),
    path('branch_update/<int:id>/',views.fn_Branch_Update_View, name='branch_update_url'),
    path('branch_delete/<int:id>/',views.fn_Branch_Delete_View, name='branch_delete_url'),


    # Expense urls
    path('expence_add/',views.fn_Expence_Add_View, name='expence_add_url'),
    path('expence_list/',views.fn_Expence_List_View, name='expence_list_view'),
    path('expence_update/<int:id>/',views.fn_Expence_Update_View, name='expence_update_url'),
    path('expence_delete/<int:id>/',views.fn_Expence_Delete_View, name='expence_delete_url'),


    # Vehicle urls
    path('vehicle_add/',views.fn_Vehicle_Add_View, name='vehicle_add_url'),
    path('vehicle_list/',views.fn_Vehicle_List_View, name='vehicle_list_url'),
    path('vehicle_update/<str:s_vehicle_number>/',views.fn_Vehicle_Update_View, name='vehicle_update_url'),
    path('vehicle_delete/<str:s_vehicle_number>/',views.fn_Vehicle_Delete_View, name='vehicle_delete_url'),

    # # Driver urls
    path('driver_add/',views.fn_Driver_Add_View, name='driver_add_url'),
    path('driver_list/',views.fn_Driver_List_View, name='driver_list_url'),
    path('driver_update/<int:id>/',views.fn_Driver_Update_View, name='driver_update_url'),
    path('driver_delete/<int:id>/', views.fn_Driver_Delete_View, name='driver_delete_url'),

    # Location urls
    path('location_add/',views.fn_Location_Add_View, name='location_add_url'),
    path('location_list/',views.fn_Location_List_view, name='location_list_url'),
    path('location_update/<int:id>/',views.fn_Location_Update_View, name='location_update_url'),
    path('location_delete/<int:id>/',views.fn_Location_Delete_View, name='location_delete_url'),
   
    # # Delivery_Type urls
    path('delivery_type_add/',views.fn_Delivery_Type_Add_View, name='delivery_type_add_url'),
    path('delivery_type_list/',views.fn_Delivery_Type_List_View, name='delivery_type_list_url'),
    path('delivery_type_update/<int:id>/',views.fn_Delivery_Type_Update_View, name='delivery_type_update_url'),
    path('delivery_type_delete/<int:id>/',views.fn_Delivery_Type_Delete_View, name='delivery_type_delete_url'),

    #Pay_Type urls
    path('pay_type_add/',views.fn_Pay_Type_Add_View, name='pay_type_add_url'),
    path('pay_type_list/',views.fn_Pay_Type_List_View, name='pay_type_list_url'),
    path('pay_type_update/<int:id>/',views.fn_Pay_Type_Update_View, name='pay_type_update_url'),
    path('pay_type_delete/<int:id>/',views.fn_Pay_Type_Delete_View, name='pay_type_delete_url'),

    # # City urls
    path('city_add/',views.fn_City_Add_View, name='city_add_url'),
    path('city_list/',views.fn_City_List_View, name='city_list_url'),
    path('city_update/<int:id>/',views.fn_City_Update_View, name='city_update_url'),
    path('city_delete/<int:id>/',views.fn_City_Delete_View, name='city_delete_url'),


    # # Consignee urls
    path('consignee_add/',views.fn_Consignee_Add_View, name='consignee_add_url'),
    path('consignee_list/',views.fn_Consignee_List_view, name='consignee_list_url'),
    path('consignee_update/<int:id>/',views.fn_Consignee_Update_View, name='consignee_update_url'),
    path('consignee_delete/<int:id>/',views.fn_Consignee_Delete_View, name='consignee_delete_url'),
    
    # # Consignor urls
    path('consignor_add/',views.fn_Consignor_Add_View, name='consignor_add_url'),
    path('consignor_list/',views.fn_Consignor_List_view, name='consignor_list_url'),
    path('consignor_update/<int:id>/',views.fn_Consignor_Update_View, name='consignor_update_url'),
    path('consignor_delete/<int:id>/',views.fn_Consignor_Delete_View, name='consignor_delete_url'), 



############################################# Operations urls #############################################################

    path('oprations_page/',views.fn_Operations_View, name='operations_url'),

    # Pickup Request urls
    path('pickup_request_add/',views.fn_Pickup_Request_Add_View, name='pickup_request_add_url'), 
    path('pickup_Request_list/',views.fn_Pickup_Request_List_View, name='pickup_request_list_url'),
    path('pickup_request_details/<int:id>/',views.fn_Pickup_Request_Details_View, name='pickup_request_details_url'),
    path('pickup_request_update/<int:id>/',views.fn_Pickup_Request_Update_View, name='pickup_request_update_url'),
    path('pickup_request_delete/<int:id>/',views.fn_Pickup_Request_Delete_View, name='pickup_request_delete_url'),
    path('get_user_info_pickup/<str:user_name>/', views.get_user_info, name='get_user_info_pickup'),

    ##URL for Consignee _auto address
    path('get_consi_info_pickup/<str:consi_name>/', views.get_consi_info, name='get_consi_info_pickup'),

    #path('get_user_info/<str:user_name>/', views.get_user_info, name='get_user_info'),
     ##URL for Consignor auto address
    # path('get_pick_user_info/<str:user_name>/', views.get_user_info, name='get_user_info'),



    path('get_user_info/<str:user_name>/', views.get_user_info, name='get_user_info'),
    ##URL for Consignee auto address
    path('get_consi_info/<str:consi_name>/', views.get_consi_info, name='get_consi_info'),


    path('run_get_consi_no_info/<str:consi_no>/', views.run_get_consi_no_info, name='run_get_consi_no_info'),
    # path('get_consi_no_info/<str:consi_no>/',views. run_get_consi_no_info, name='get_consi_no_info'),



    

    # Cosignment No urls
    path('consignment_no_add/',views.fn_Consignment_No_Add_View, name='consignment_no_add_url'),
    path('consignment_no_list/',views.fn_Consignment_No_List_View, name='consignment_no_list_url'),
    path('consignment_no_details/<int:id>/',views.fn_Consignment_No_Deatails_View, name='consignment_no_details_url'),
    path('consignment_no_update/<int:id>/',views.fn_Consignment_No_Update_View, name='consignment_no_update_url'),
    path('consignment_no_delete/<int:id>/',views.fn_Consignment_No_Delete_View, name='consignment_no_delete_url'),
    path('generate_cn_pdf/<int:id>/', views.generate_cn_pdf, name='generate_cn_pdf'),

    
    path('pdf/', views.generate_pdf, name='generate_pdf'),
    
    
    # Pickup Runsheet No urls
    path('pickup_runsheet_add/',views.fn_Pickup_Runsheet_Add_View, name='pickup_runsheet_add_url'), 
    path('pickup_runsheet_list/',views.fn_Pickup_Runsheet_List_View, name='pickup_runsheet_list_url'),
    path('pickup_runsheet_list_of_pickup_request/',views.fn_Pickup_Runsheet_List_of_Pickup_request_View, name='pickup_runsheet_list_of_pickup_request_url'),
    path('pickup_runsheet_update/<int:id>/',views.fn_Pickup_Runsheet_Update_View, name='pickup_runsheet_update_url'),
    path('pickup_runsheet_delete/<int:id>/',views.fn_Pickup_Runsheet_Delete_View, name='pickup_runsheet_delete_url'),
    path('addrun/',views.addrunsheet, name='addrun'),
    path('pickup_runsheet_details/<int:id>/',views.fn_Pickup_Runsheet_Details_View, name='pickup_runsheet_details_url'),
    path('generate_cn_pdf/<int:id>/', views.generate_pdf, name='generate_cn_pdf'),
    path('pickup_runsheet_show/',views.fn_Pickup_Runsheet_List_of_Pickup_request_View, name='pickup_runsheet_show_url'),


     
   
    # Manifest Load urls

    path('manifest_load_list_view/',views.fn_Manifest_Load_List_View, name='manifest_load_list_url'),

    path('manifest_delete_view/<int:id>/',views.fn_Manifest_Delete_View, name='manifest_delete_url'),

    path('manifest_update_view/<int:id>/',views.fn_Manifest_Update_View, name='manifest_update_url'),

    path('manifest_details/<int:id>/',views.fn_Manifest_Details_View, name='manifest_details_url'),

    path('add_manifest_load/',views.fn_Add_Manifest_View, name='add_new_manifest_url'),


    # Trip sheet urls
    path('trip_sheet_add/',views.fn_Trip_Sheet_Add_View,name='trip_sheet_add_url'),
    path('trip_sheet_list/',views.fn_Trip_Sheet_List_View,name='trip_sheet_list_url'),
    path('trip_sheet_details_view/<int:id>/',views.fn_Trip_Sheet_Details_View,name='trip_sheet_details_url'),
    path('trip_sheet_update/<int:id>/',views.fn_Trip_Sheet_Update_View,name='trip_sheet_update_url'),
    path('trip_sheet_delete/<int:id>/',views.fn_Trip_Sheet_Delete_View,name='trip_sheet_delete_url'), 
    
    path('get_mani_info/<str:mani_no>/', views.get_mani_info, name='get_mani_info'),

    
    # Manifest Unload urls
    path('manifest_unload_list/',views.fn_Manifest_Unload_List_View, name='manifest_unload_list_url'),
    path('manifest_unload_details/<int:id>/',views.fn_Manifest_Unload_Details_View, name='manifest_unload_details_url'),
    path('manifest_unload_add/',views.fn_Add_Manifest_Unload_View, name='manifest_unload_add_url'),
    path('manifest_unload_update/<int:id>/',views.fn_Manifest_Unload_Update_View, name='manifest_unload_update_url'),  
    path('manifest_unload_dalete/<int:id>/',views.fn_Manifest_Unload_Delete_View, name='manifest_unload_delete_url'),
    
    #Delivery Runsheet
    path('delivery_runsheet_add/',views.new_add,name='delivery_runsheet_add_url'),
    path('delivery_runsheet_list_view/',views.fn_Delivery_Runsheet_List_View, name='delivery_runsheet_list_url'),
    path('delivery_runsheet_details/<int:id>/',views.fn_Delivery_Runsheet_Details_View, name='delivery_runsheet_details_url'),
    path('delivery_runsheet_update/<int:id>/',views.fn_Delivery_Runsheet_Update_View, name='delivery_runsheet_update_url'),
    path('delivery_runsheet_delete_view/<int:id>/',views.fn_Delivery_Runsheet_Delete_View, name='delivery_runsheet_delete_url'),
    # path('delivery_runsheet_print/<int:id>/',views.fn_Delivery_Runsheet_Print_View, name='delivery_runsheet_print_url'),
    
    path('report/', ReportView, name='report'),
    path('branch_report/', views.Branch_ReportView, name='branch_report'),
    
    path('upload/',views.upload_image, name='upload_image'),
    path('display/',views.display_image, name='display_image'),
   

    

     # Invoice urls
    path('invoice_list/',views.fn_Invoice_List_View, name='invoice_list_url'),
    path('invoice_add_datewise_view/',views.fn_Invoice_Add_Datewise_View, name='invoice_add_datewise_url'),
    path('invoice_add_view/',views.fn_Invoice_Add_View, name='invoice_add_url'),
    path('invoice_details/<int:id>/',views.fn_Invoice_Details_View, name='invoice_details_url'),
    path('invoice_update/<int:id>/',views.fn_Invoice_Update_View, name='invoice_update_url'),
    path('invoice_delete_view/<int:id>/',views.fn_Invoice_Delete_View, name='invoice_delete_url'),
   
    
    

    # Delivery Runseet 
    path('delivery_runsheet_add/',views.new_add,name='delivery_runsheet_add_url'),
    path('delivery_runsheet_list_view/',views.fn_Delivery_Runsheet_List_View, name='delivery_runsheet_list_url'),
    path('delivery_runsheet_details/<int:id>/', views.fn_Delivery_Runsheet_Details_View, name='delivery_runsheet_details_url'),
    #path('delivery_runsheet_list_of_consignment_no/',views.fn_Delivery_Runsheet_List_of_consignment_View, name='delivery_runsheet_list_of_consignment_no_url'),

    path('delivery_runsheet_update/<int:id>/',views.fn_Delivery_Runsheet_Update_View, name='delivery_runsheet_update_url'),
    path('delivery_runsheet_delete_view/<int:id>/',views.fn_Delivery_Runsheet_Delete_View, name='delivery_runsheet_delete_url'),
    path('addconsi/',views.addconsignment, name='addconsi'),
    path('dpdf/<int:id>/', views.generate_invoice_dpdf, name='generate_invoice_dpdf'),    
    path('allreport/',views.fn_all_report, name='allreport'),

   ######### Path for Finance model

    ######## Add Voucher
    path('add_voucher_list_view/',views.fn_add_voucher_list_view, name = 'add_voucher_list_url'),
    path('add_voucher_add_view/',views.fn_add_voucher_add_view, name = 'add_voucher_add_url'),
    path('add_voucher_update_view/<int:id>/',views.fn_add_voucher_edit_view, name = 'add_voucher_update_url'),
    path('add_voucher_details_view/<int:id>/',views.fn_add_voucher_details_view, name = 'add_voucher_details_url'),
    path('add_voucher_delete/<int:id>/',views.fn_Add_voucher_Delete_View, name='add_voucher_delete_url'),

       ######## Add Ledger
    path('ledger_list/',views.ledger_List_View, name = 'ledger_list'),
    path('add_ledger/',views.create_ledger, name = 'add_ledger'),
    path('edit_ledger/<int:id>/',views.ledger_edit, name = 'edit_ledger'),
    path('ledger_details/<int:id>/',views.fn_ledger_Details_View, name = 'ledger_details'),
    path('delete_ledger/<int:id>/',views.ledger_delete, name='delete_ledger'),

           ######## Trial Balance
    path('trial_balance_list/',views.fn_list_trial_balance, name = 'trial_balance_list'),
    path('add_trial_balance_list/',views.fn_add_trial_balance, name = 'add_trial_balance_list'),
    path('edit_trial_balance/<int:id>/',views.fn_edit_trial_balance, name = 'edit_trial_balance'),
    path('trial_details/<int:id>/',views.fn_trial_Details_View, name = 'trial_details'),
    path('delete_trial/<int:id>/',views.fn_delete_trial_balance, name='delete_trial'),
    

    ####Profit Loss
    path('profit_loss/',views.fn_profit_loss_View, name = 'profit_loss'),
    path('balance_sheet/',views.fn_balance_sheet_View, name = 'balance_sheet'),



            ######## Trial Balance
    path('balance_sheet_list/',views.fn_balance_sheet_View, name = 'balance_sheet_list'),
    path('add_balance_sheet_list/',views.create_balance_sheet, name = 'add_balance_sheet_list'),
    path('edit_balance_sheet_list/<int:id>/',views.balance_edit, name = 'edit_balance_sheet_list'),
    path('balance_sheet_details/',views.fn_balance_Details_View, name = 'balance_sheet_details'),
    path('delete_balance_sheet/<int:id>/',views.balance_delete, name='delete_balance_sheet'),





    ######## Listing Voucher
    # path('listing_voucher_list_view/',views.fn_listing_voucher_list_view, name = 'listing_voucher_list_url'),
    # path('listing_voucher_Delete_View/<int:id>/',views.fn_listing_voucher_Delete_View, name = 'listing_voucher_Delete_url'),









   
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


