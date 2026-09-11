def run_test():
    print("Running automated test for Data Optimizer...\n")
    try:
        from optimizer import filter_evens, get_top_word
        
        # Test 1: Comprehension
        nums = [1, 2, 3, 4, 5, 6]
        if filter_evens(nums) != [2, 4, 6]:
            print("❌ Failed: filter_evens did not return the correct list of even numbers.")
            return
            
        # Test 2: Counter
        words = ["error", "warning", "error", "info", "error", "warning"]
        top_word = get_top_word(words)
        
        # Handle cases where they return the tuple ('error', 3) instead of just the word
        if top_word == "error" or (isinstance(top_word, tuple) and top_word[0] == "error"):
            print("✅ Successfully filtered evens and used Counter for text analysis.")
            print("\n🏆 All tests passed!")
        else:
            print(f"❌ Failed: get_top_word returned {top_word} instead of 'error'.")
            
    except ImportError:
        print("❌ Failed: Could not find 'optimizer.py' or one of the required functions.")
    except Exception as e:
        print(f"❌ Script crashed with error: {e}")

if __name__ == "__main__":
    run_test()