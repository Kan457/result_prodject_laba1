from hospital import Patient
from work_file import load_hospital_from_xml

print('===Поликлиника===')
Hospital1 = load_hospital_from_xml('hospital_data.xml')
Hospital1.Work_patient()
print("\n========Выберите пациента=========")
polis_first = Hospital1.choose_patient()
#if polis_first:
print("\n=======Выберите что сделать========")
patient_obj = Patient(polis_first)
patient_obj.Work_actions(polis=polis_first)
#========================================================