from hsc_utils import hsc_image

object_id,ra,dec='36411448540270969',30.611445,-6.475494
out_dir='/lustre/work/connor.bottrell/RealSim_HSC/Cutouts'

hsc_image.get_cutouts(object_id,ra,dec,out_dir,dr='dr4',rerun='s21a_wide',filters='GRIZY',fov_arcsec=120)