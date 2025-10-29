import xml.etree.ElementTree as ET
from hospital import Hospital

def load_hospital_from_xml(xml_file):
    """
    Загружает данные больницы из XML файла и создает объект Hospital
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Извлекаем основную информацию о больнице
    hospital_info = root.find('hospital_info')
    name = hospital_info.find('name').text
    address = hospital_info.find('address').text
    chief_medical = hospital_info.find('chief_medical').text
    mail = hospital_info.find('mail').text
    
    # Создаем словарь врачей
    doctor_dict = {}
    for spec in root.find('doctor_dict'):
        spec_name = spec.get('name')
        doctor_dict[spec_name] = {}
        for doctor in spec.findall('doctor'):
            doctor_name = doctor.get('name')
            doctor_id = doctor.get('id')
            doctor_dict[spec_name][doctor_name] = doctor_id
    
    # Создаем словарь пациентов
    patient_dict = {}
    for patient in root.find('patient_dict'):
        patient_name = patient.get('name')
        patient_policy = patient.get('policy')
        patient_dict[patient_name] = patient_policy
    
    # Создаем объект Hospital
    hospital = Hospital(
        name=name,
        addres=address,
        chief_medical=chief_medical,
        mail=mail,
        doctor_dict=doctor_dict,
        patient_dict=patient_dict
    )
    
    return hospital