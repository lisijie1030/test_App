import os

base_path=os.path.dirname(os.path.dirname(__file__))

app_path=os.path.join(base_path + '/app/FKHL-LGAPP-1.1.21-prod-release')

app_config_data_path=os.path.join(base_path +'/config/app_config_data.yaml')

picture_file=os.path.join(base_path,'picture')

recording_file=os.path.join(base_path,'recording')

record_data_path=os.path.join(base_path +'/data/record_data.xlsx')

data_path=os.path.join(base_path,'data')

