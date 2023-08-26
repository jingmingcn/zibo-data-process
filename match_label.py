import csv

filename_label = {}

with open('filename.csv',newline='') as csvfile:
  with open('filename_label.csv') as labelfile:
    with open('datafile.csv') as datafile:
      csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
      datareader = csv.DictReader(datafile)
      fieldnames = ['filename','id_card','label']
      writer = csv.DictWriter(labelfile, fieldnames=fieldnames)
      writer.writeheader()
      for row in csvreader:
        flag = False
        patient_id = row['filename'].split('_')[1]
        patient_date = row['filename'].split('_')[2][:8]
        patient_date = '-'.join([patient_date[0:4],patient_date[4:6],patient_date[6:8]])
        for data in datareader:
          date = data[5][:10]
          if(patient_id == data[0] and patient_date == date ):
            flag = True
            writer.writerow({
              'filename':row['filename'],
              'id_card':data[2],
              'label':data[4]
                             })
        if(not flag):
          print(patient_id)
