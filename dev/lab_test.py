#grading script lab2

#set grading paths
grade_path = "/lab2_to_grade/"
score_path = "/lab2_scores/"
lab_number = "2"

import re
import os
import crw
import testing_module_2
directory_path = os.path.dirname(os.path.realpath(__file__))

labs = os.listdir(directory_path + grade_path)
data = []
reject = []
capture_string ="((.*)_lab"+lab_number+").py"

for lab in labs:
    capture = re.compile(capture_string)
    s = capture.findall(lab)
    if s != []:
        score = testing_module_2.test(s[0][0], s[0][1], path = directory_path + grade_path + s[0][0]+ ".py")
        data.append(score)
        print("Graded:", s[0][0], "\n")
    else:
        reject.append(lab)
        
if data:
    crw.setData(path = directory_path + score_path , title = "lab2_scores", data = data)
    if reject:
        print("Files not graded", reject)
else:
    print("No labs were graded.")
