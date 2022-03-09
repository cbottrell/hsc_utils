from hsc_utils import hsc_psf

object_id,ra,dec,out_dir = '36411448540270969',30.611445,-6.475494,'PSFs'

hsc_psf.get_psfs(object_id,ra,dec,out_dir,dr='dr4',rerun='s21a_wide',filters='GRIZY')