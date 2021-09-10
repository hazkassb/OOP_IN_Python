import student

as1 = student.ArtsStudent('Peter Johnson', 19012, 'History', 11000.65, 'A')
print(as1)

cs1 = student.CommerceStudent('Larry Faith', 19126, 'Digital Marketing', 21000.0, 'Digital Consultancy')
print(cs1)

ts1 = student.TechStudent('Alan Goh', 19111, 'Computer Science', 13400.67, 'Kyla Tech', 'A')
print(ts1)

if(ts1 < cs1):
    print('The annual fee of Technical Student is less than that of Commerce Student')
else:
    print('The annual fee of Technical Student is greater than that of Commerce Student')

if(as1 < ts1):
    print('The annual fee of Art Student is less than that of Technical Student')
else:
    print('The annual fee of Art Student is greater than that of Technical Student')