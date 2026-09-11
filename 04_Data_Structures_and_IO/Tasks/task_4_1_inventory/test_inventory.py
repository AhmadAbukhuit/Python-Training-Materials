def run_test():
    print("Running automated test for Inventory Manager...\n")
    try:
        from inventory import get_unique_items
        
        raw_data = ["apple", "banana", "apple", "orange", "banana"]
        expected = ["apple", "banana", "orange"] # Sorted alphabetically
        
        result = get_unique_items(raw_data)
        
        if result == expected:
            print(f"✅ Success! Expected {expected} and got {result}.")
            print("\n🏆 All tests passed!")
        else:
            print(f"❌ Failed: Expected {expected} but got {result}.")
            print("Did you remember to sort the final list?")
            
    except ImportError:
        print("❌ Failed: Could not find 'inventory.py' or the 'get_unique_items' function.")
    except Exception as e: 
        print(f"❌ Script crashed with error: {e}")

if __name__ == "__main__":
    run_test()