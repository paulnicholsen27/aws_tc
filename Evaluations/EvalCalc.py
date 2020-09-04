import csv
import sys

with open(sys.argv[1], mode='r') as evalfile:
        reader = csv.reader(evalfile)
        ncols = len(next(reader)) + 1
        evalfile.seek(0)
        mapval = {'strongly agree': 5, 'agree': 4, 'neutral': 3, 'disagree': 2, 'strongly disagree': 1}
        column_sum = [0] * ncols
        divisor = [0] * ncols
        question = [None] * ncols
        row_position = 0
        feedback = ''
        for row in reader:
            row_position = row_position + 1
            item_position = 0
            for item in row:
                item_position = item_position + 1
                if row_position == 2:
                    question[item_position] = item.replace("\n", " ")
                if mapval.get(item.lower()):
                    column_sum[item_position] = column_sum[item_position] + mapval.get(item.lower())
                    divisor[item_position] = divisor[item_position] + 1
                elif item and row_position > 2:
                    feedback = feedback + ' - ' + item + '\n'

        item_position = 0

        instructor_sum = 0
        instructor_div = 0
        overall_sum = 0
        overall_div = 0

        for pos in range(ncols):
            val = divisor[pos]
            if val > 0:
                print('%.2f' % float(column_sum[pos]/val), question[pos])
                overall_div = overall_div + val
                overall_sum = overall_sum + column_sum[pos]
                if 'instructor' in question[pos]:
                    instructor_div = instructor_div + val
                    instructor_sum = instructor_sum + column_sum[pos]

        print('')
        print('%.2f' % float(instructor_sum/instructor_div), 'Instructor CSAT')
        print('%.2f' % float(overall_sum/overall_div), 'Overall CSAT')
        print('')
        print('Additional Feedback')
        print(feedback)