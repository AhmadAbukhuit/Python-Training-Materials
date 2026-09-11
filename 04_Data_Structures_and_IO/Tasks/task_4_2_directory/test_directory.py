def run_test():
    print("Running automated test for Safe Directory...\n")
    try:
        from directory import get_salary, update_salary
        
        db = {
            "emp_01": {"name": "Alice", "salary": 85000},
            "emp_02": {"name": "Bob", "salary": 72000}
        }
        
        # Test 1: Safe Get (Existing)
        if get_salary(db, "emp_01") != 85000:
            print("❌ Failed: get_salary did not return the correct salary for emp_01.")
            return
            
        # Test 2: Safe Get (Missing)
        if get_salary(db, "emp_99") != "Not Found":
            print("❌ Failed: get_salary crashed or did not return 'Not Found' for a missing ID.")
            print("Are you using the .get() method with a default value?")
            return
            
        # Test 3: Update
        update_salary(db, "emp_02", 75000)
        if db["emp_02"]["salary"] != 75000:
            print("❌ Failed: update_salary did not correctly update the dictionary.")
            return
            
        print("✅ All dictionary operations worked flawlessly.")
        print("\n🏆 All tests passed!")
        
    except ImportError:
        print("❌ Failed: Could not find 'directory.py' or one of the required functions.")
    except Exception as e:
        print(f"❌ Script crashed with error: {e}")

if __name__ == "__main__":
    run_test()