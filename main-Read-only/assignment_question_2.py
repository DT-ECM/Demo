import sys
sys.path.append('./')
import Assignment_Submission;
text = input().split(",")
input_param = [int(a) for a in text]
print(Assignment_Submission.question2(input_param))
