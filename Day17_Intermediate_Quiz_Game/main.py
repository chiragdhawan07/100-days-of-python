from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create list of Question objects
question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

# Start quiz
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("🎉 You've completed the quiz!")
print(f"Your final score: {quiz.score}/{len(question_bank)}")
