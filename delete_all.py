import urllib.request
import json

def get_profits():
    try:
        with urllib.request.urlopen('http://localhost:8000/api/profits') as response:
            data = json.loads(response.read().decode('utf-8'))
            return data
    except Exception as e:
        print(f"Error getting profits: {e}")
        return []

def delete_profit(profit_id):
    req = urllib.request.Request(f'http://localhost:8000/api/profits/{profit_id}', method='DELETE')
    try:
        with urllib.request.urlopen(req) as response:
            return response.status
    except Exception as e:
        print(f"Error deleting {profit_id}: {e}")
        return None

if __name__ == "__main__":
    profits = get_profits()
    print(f"Found {len(profits)} entries to delete.")
    for p in profits:
        status = delete_profit(p['id'])
        if status == 204:
            print(f"Deleted {p['id']}")
        else:
            print(f"Failed to delete {p['id']}")
    print("Deletion complete.")