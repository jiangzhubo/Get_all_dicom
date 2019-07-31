
import os 
import shutil
import filetype
def get_dicom(path):
  '''this function is used to select Dicom type file'''
  '''
      input:
         path: where the dicom locates
      output: all the dicom files' path
  '''
  Dicom_path = {}
  
  for root, dirs, files in os.walk(path, topdown=False):
       Dicom_file = []
       for name in files:
           kind  = []
           file = os.path.join(root, name)
           kind = filetype.guess(file)
           if  'extension' in dir(kind) :
             if kind.extension in ['dcm','DCM','dicom','DICOM']:
               # DICOM extension is dcm
                  if file.split('/')[-1] not in ['DICOMDIR']:
                     Dicom_file.append( name)
       if len(Dicom_file) >0:
           Dicom_path[root] = Dicom_file
  return Dicom_path


print(get_dicom('./'))
