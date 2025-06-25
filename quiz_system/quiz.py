import sqlite3

def connect_db():
    return sqlite3.connect('quiz.db')

def add_question():
    print("\n--- Add New Question ---")
    question = input("Enter question: ")
    a = input("Option A: ")
    b = input("Option B: ")
    c = input("Option C: ")
    d = input("Option D: ")
    correct = input("Correct Option (a/b/c/d): ").lower()

    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, a, b, c, d, correct))
    conn.commit()
    conn.close()
    print("✅ Question added successfully.\n")

def take_quiz():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions")
    questions = cur.fetchall()
    conn.close()

    if not questions:
        print("❌ No questions found. Please ask Admin to add questions first.\n")
        return

    print("\n--- Quiz Started ---")
    score = 0

    for q in questions:
        print(f"\n{q[1]}")
        print(f"a) {q[2]}")
        print(f"b) {q[3]}")
        print(f"c) {q[4]}")
        print(f"d) {q[5]}")
        answer = input("Your answer: ").lower()
        if answer == q[6]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q[6]}")

    print(f"\n🏁 Quiz finished! Your score: {score}/{len(questions)}")

def menu():
    while True:
        print("\n=== Online Quiz System ===")
        print("1. Add Question (Admin)")
        print("2. Take Quiz (User)")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            add_question()
        elif choice == '2':
            take_quiz()
        elif choice == '3':
            print("🔚 Exiting the system.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
