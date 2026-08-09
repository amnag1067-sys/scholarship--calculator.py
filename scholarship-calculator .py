print("=== WELCOME TO THE INTERNATIONAL SCHOLARSHIP ELIGIBILITY SYSTEM ===")


run_again = "yes"

while run_again.lower() == "yes":
    student_name = input("\nEnter student name: ")
    high_school_score = int(input("Enter High School Score (out of 1200): "))
    ielts_score = float(input("Enter IELTS Band Score: "))
    
    percentage = (high_school_score / 1200) * 100
    print(f"\nProcessing profile for {student_name}...")
    print(f"Academic Percentage: {percentage:.1f}%")
    
    
    if percentage >= 75 and ielts_score >= 6.5:
        print("🎉 STATUS: HIGHLY ELIGIBLE FOR 100% FULLY FUNDED SCHOLARSHIPS!")
        print("Recommendation: Target top-tier public universities in any country.")
    elif percentage >= 60 and ielts_score >= 5.5:
        print("👍 STATUS: ELIGIBLE FOR PARTIAL SCHOLARSHIPS / REGIONAL AID.")
        print("Recommendation: Focus on regional financial need-based documents.")
    else: 
        print("❌ STATUS: BELOW SCHOLARSHIP THRESHOLD.")
        print("Recommendation: Consider taking a foundation layer course.")
        
    
    run_again = input("\nDo you want to check another student profile? (yes/no): ")

print("\nThank you for using the system. Program terminated successfully.")