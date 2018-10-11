__author__ = 'kosala atapattu'
import time
from ansible import errors

def report_format (values, columns):

    table = []
    header = []
    max_width = []

    output = ''

    for hitem in values['json']['result'][0]:
        header.append(hitem)
        table.append([hitem, []])
        max_width.append([hitem, 0])

    for item in values['json']['result']:
        for key, val in enumerate(table):
            table[key][1].append(item[val[0]])
        if max_width[key][1] == 0:
            max_width[key][1] = len(item[val[0]])
        elif max_width[key][1] < len(item[val[0]]):
            max_width[key][1] = len(item[val[0]])
    
    # Print the headers
    for cols , hitem in enumerate(table):
        output += str(hitem[0]).ljust(max_width[int(cols)][1]+5) + '\t'
    output += "\n"
    for cols , hitem in enumerate(table):
        output += str('-').ljust(max_width[int(cols)][1]+5, '-') + '\t'
    output += "\n"

    for rows, vals in enumerate(table[0][1]):
        for cols, item in enumerate(table):
            output += str(item[1][int(rows)]).ljust(max_width[int(cols)][1]+5) + '\t' 
        output += "\n"
    
    return output

def format_command (cmd):
    cmd_portions = str(cmd).split(' ')
    if len(cmd_portions) == 1:
        return cmd + "?"
    main_cmd = cmd_portions[0] + "?"

    cmd_opt = ''

    for opt in cmd_portions[1:]:
        if opt[0] == '-':
            if cmd_opt == '':
                cmd_opt += opt[1:]
            else:
                cmd_opt += "&" + opt[1:]
        else:
            cmd_opt += "=" + opt

    main_cmd += cmd_opt
    return  main_cmd

class FilterModule(object):
    def filters(self):
        return {
            'report_format': report_format,
            'format_command': format_command
            }
