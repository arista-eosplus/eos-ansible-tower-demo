from ansible import errors
import re


def split_lines(value):
    return [s.strip() for s in value.splitlines()]


def filter_vms(value, id):
    output = []
    for vm in value['vms']:
        vlan = re.sub(r'[v|V]lan', '', id)
        if vm['vlan'] == vlan:
            output.append(vm)
    return output


def format_commands(value, encoding='json'):
    commands = split_lines(value)
    formatted = list()
    for cmd in commands:
        formatted.append(dict(command=cmd, output=encoding))
    return formatted


def format_stdout(value, input_commands):
    output = list()
    for i, result in enumerate(value):
        cmd = '* Command: %s' % input_commands[i]['command']
        output.append('*' * len(cmd))
        output.append(cmd)
        output.append('*' * len(cmd))
        for res in result.splitlines():
            output.append(res)
    return output


def get_packet_loss(value):
    print value
    loss = re.search(r'(\d+)%\s+packet\sloss', value, re.M)
    if loss:
        return loss.group(1)
    else:
        return 100


class FilterModule(object):
    def filters(self):
        return {
            'split_lines': split_lines,
            'format_commands': format_commands,
            'format_stdout': format_stdout,
            'packet_loss': get_packet_loss,
            'filter_vms': filter_vms,
        }
