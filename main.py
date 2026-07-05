import argparse
import json

def convert_value(value, from_unit, to_unit):
    # Load unit definitions
    with open('units.json') as f:
        units = json.load(f)
    
    # Get conversion factors
    from_def = units[from_unit]
    to_def = units[to_unit]
    
    # Perform calculation
    return value * (from_def['factor'] / to_def['factor'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert between units')
    parser.add_argument('value', type=float, help='Value to convert')
    parser.add_argument('--from', required=True, help='Source unit')
    parser.add_argument('--to', required=True, help='Target unit')
    args = parser.parse_args()
    
    result = convert_value(args.value, args.from, args.to)
    print(f'{args.value} {args.from} = {result:.6f} {args.to}')