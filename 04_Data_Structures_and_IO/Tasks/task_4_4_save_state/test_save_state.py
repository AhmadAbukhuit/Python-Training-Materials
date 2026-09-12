import os

def run_test():
    print("Running automated test for Save State...\n")
    try:
        from save_state import save_data, load_data
        
        test_file = "test_stats.json"
        test_data = {"player": "Alice", "score": 9500, "level": 4}
        
        # 1. Test Writing
        save_data(test_data, test_file)
        if not os.path.exists(test_file):
            print("❌ Failed: The file was not created. Did you use the 'w' mode?")
            return
            
        # 2. Test Reading
        loaded = load_data(test_file)
        if loaded.get("score") == 9500:
            print("✅ Successfully wrote data to JSON and loaded it back into a dictionary!")
            print("\n🏆 All tests passed!")
        else:
            print("❌ Failed: The data loaded from the file did not match the original data.")
            
    except ImportError:
        print("❌ Failed: Could not find 'save_state.py' or one of the required functions.")
    except Exception as e:
        print(f"❌ Script crashed with error: {e}")
    finally:
        # Clean up the test file so we don't clutter their directory
        if os.path.exists("test_stats.json"):
            os.remove("test_stats.json")

if __name__ == "__main__":
    run_test()