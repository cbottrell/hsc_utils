# hsc_utils

A collection of python tools for acquiring catalogue and image data from the HSC data archive server (DAS) and SQL Catalogue Archive Server (CAS).
 
The package can be copied to the site-packages directory of your python/conda environment or kept in your working directory. The package includes 3 core data acquisition tools: hsc_image, hsc_psf, and hsc_sql. Each requires that the following environment variables are set to your STARS account info (e.g. in ~/.bash_profile):
```
export SSP_IDR_USR='STARS_USRNAME'
export SSP_IDR_PWD='STARS_PASSWRD'
```
Support for public data releases has not been developed yet.
 
These tools interface directly with the DAS and CAS so they can be used on any machine. Example usage of each of the tools are provided in separate example_[image/psf/sql].py scripts with the package. 
 
Large SQL queries to the CAS (>100,000 objects) can take a long time. It is best to run such queries overnight or in queue mode on a cluster. PSF and Cutout requests are limited to 1000 objects each (including different filters). Therefore, one can use the hsc_image.make_cutout_list and hsc_psf.make_psf_list to first generate individual request files for each (ra,dec) target, then concatenate them (remember to remove headers). This has higher performance than acquiring each individual object. 
