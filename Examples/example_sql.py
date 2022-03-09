from hsc_utils import hsc_sql
import pandas as pd

dr='dr3'
rerun = 's20a_wide'
csv_name = f'HSC-{dr}-{rerun}-test.csv'

sql_cmd=f'SELECT f.object_id, f.ra, f.dec FROM {rerun}.forced as f LIMIT 10'
df = hsc_sql.load_sql_df(csv_name,dr=dr,sql_cmd=sql_cmd)

print(df.head(10))