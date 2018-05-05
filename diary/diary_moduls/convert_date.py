import datetime
import time

#�� ���� ���� ��������� ������� ������� �������� ���������� ����, ��� ����� ������
def check_date(date, format):
    try:
        datetime.datetime.strptime(date, format)
        return date
    except ValueError:
        return None
        
        
# converter in unix date format
def convert_to_unix_format(date, format='%d.%m.%Y %H:%M'):
    return int(time.mktime(time.strptime(date, format)))
    

# converter in normal date format
def convert_to_date_format(date):
    date = int(date)
    return time.strftime("%d.%m.%Y %H:%M", time.localtime(date))