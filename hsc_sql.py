import os
import pandas as pd

def load_sql_df(csv_name,dr='dr3',usr_env='SSP_IDR_USR',pwd_env='SSP_IDR_PWD',sql_cmd='SELECT now()'):
    '''Query data base with sql_cmd if csv_name does not exist, else load existing csv file.'''
    if os.access(csv_name,0):
        return pd.read_csv(csv_name,comment='#')
    base_sql_path = os.path.dirname(__file__)
    os.system(f'echo "{sql_cmd}" > cmd.sql')
    sys_cmd = [f'python {base_sql_path}/hscSspQuery3.py',
               f'--user {os.getenv(usr_env)}',
               f'--password-env {pwd_env}',
               f'--nomail',
               f'--release-version {dr}',
               f'--delete-job',
               f'cmd.sql > {csv_name}']
    os.system(' '.join(sys_cmd))
    if os.access('cmd.sql',0): os.remove('cmd.sql')
    with open(csv_name,'r') as f:
        lines = f.readlines()
        col_names = lines[4].replace('# ','')
        lines[4] = col_names
    with open(csv_name,'w') as f:
        f.writelines(lines)
    return pd.read_csv(csv_name,comment='#')

def hsc_coadd_cnds(rerun):
    '''Conditions that HSC coadds must be at final data quality.'''
    if 'dud' in rerun:
        cnds = [
            'g_inputcount_value>=28',
            'r_inputcount_value>=28',
            'i_inputcount_value>=38',
            'z_inputcount_value>=63',
            'y_inputcount_value>=38',
        ]
    else:
        cnds = [
            'g_inputcount_value>=4',
            'r_inputcount_value>=4',
            'i_inputcount_value>=6',
            'z_inputcount_value>=6',
            'y_inputcount_value>=6',
        ]
    return cnds

def main():
    '''Example usage.'''
    # tables
    dr='dr3'
    rerun = 's20a_wide'
    # output catalogue as csv dataframe
    csv_name = f'HSC-{dr}-{rerun}-Catalogue.csv'
    # query
    sql_cmd=f'SELECT f.object_id, f.ra, f.dec FROM {rerun}.forced as f LIMIT 10'
    df = load_sql_df(csv_name,dr=dr,sql_cmd=sql_cmd)
    
    print(df.head(10))
    
if __name__=='__main__':
    main()
