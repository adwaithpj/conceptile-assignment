from django.db import migrations


def create_initial_questions(apps, schema_editor):
    # Get the Question and Choice models
    Question = apps.get_model("quiz", "Question")
    Choice = apps.get_model("quiz", "Choice")

    # Sample questions with choices
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": [
                ("London", False),
                ("Paris", True),
                ("Berlin", False),
                ("Rome", False),
            ],
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": [
                ("Venus", False),
                ("Mars", True),
                ("Jupiter", False),
                ("Saturn", False),
            ],
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "choices": [
                ("Charles Dickens", False),
                ("William Shakespeare", True),
                ("Mark Twain", False),
                ("Jane Austen", False),
            ],
        },
        {
            "question": "What is the largest ocean on Earth?",
            "choices": [
                ("Atlantic Ocean", False),
                ("Indian Ocean", False),
                ("Arctic Ocean", False),
                ("Pacific Ocean", True),
            ],
        },
        {
            "question": "What is the boiling point of water?",
            "choices": [
                ("90°C", False),
                ("100°C", True),
                ("120°C", False),
                ("80°C", False),
            ],
        },
        {
            "question": "What is the smallest prime number?",
            "choices": [
                ("1", False),
                ("2", True),
                ("3", False),
                ("0", False),
            ],
        },
        {
            "question": "Which animal is known as the 'King of the Jungle'?",
            "choices": [
                ("Tiger", False),
                ("Elephant", False),
                ("Lion", True),
                ("Leopard", False),
            ],
        },
        {
            "question": "What is the square root of 144?",
            "choices": [
                ("10", False),
                ("12", True),
                ("14", False),
                ("16", False),
            ],
        },
        {
            "question": "What is the chemical symbol for gold?",
            "choices": [
                ("Ag", False),
                ("Au", True),
                ("Go", False),
                ("Gd", False),
            ],
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "choices": [
                ("Oxygen", False),
                ("Nitrogen", False),
                ("Carbon Dioxide", True),
                ("Helium", False),
            ],
        },
        {
            "question": "Who discovered gravity?",
            "choices": [
                ("Galileo Galilei", False),
                ("Albert Einstein", False),
                ("Isaac Newton", True),
                ("Nikola Tesla", False),
            ],
        },
        {
            "question": "Which is the tallest mountain in the world?",
            "choices": [
                ("Mount Kilimanjaro", False),
                ("Mount Everest", True),
                ("Mount Fuji", False),
                ("K2", False),
            ],
        },
        {
            "question": "What is the chemical symbol for water?",
            "choices": [
                ("CO2", False),
                ("H2O", True),
                ("O2", False),
                ("N2", False),
            ],
        },
        {
            "question": "Who painted the Mona Lisa?",
            "choices": [
                ("Vincent van Gogh", False),
                ("Leonardo da Vinci", True),
                ("Pablo Picasso", False),
                ("Claude Monet", False),
            ],
        },
        {
            "question": "What is the speed of light?",
            "choices": [
                ("300,000 km/s", True),
                ("150,000 km/s", False),
                ("1,000 km/s", False),
                ("30,000 km/s", False),
            ],
        },
        {
            "question": "How many continents are there on Earth?",
            "choices": [
                ("5", False),
                ("6", False),
                ("7", True),
                ("8", False),
            ],
        },
        {
            "question": "Which is the longest river in the world?",
            "choices": [
                ("Amazon River", False),
                ("Nile River", True),
                ("Yangtze River", False),
                ("Ganges River", False),
            ],
        },
        {
            "question": "What does DNA stand for?",
            "choices": [
                ("Deoxyribose Nitric Acid", False),
                ("Deoxyribonucleic Acid", True),
                ("Dicarboxylic Nucleic Acid", False),
                ("Dioxynucleotide Acid", False),
            ],
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "choices": [
                ("China", False),
                ("Japan", True),
                ("South Korea", False),
                ("Vietnam", False),
            ],
        },
        {
            "question": "What is the largest organ in the human body?",
            "choices": [
                ("Heart", False),
                ("Brain", False),
                ("Skin", True),
                ("Liver", False),
            ],
        },
    ]

    # Create questions and choices
    for q in questions:
        question_obj = Question.objects.create(text=q["question"])
        for choice_text, is_correct in q["choices"]:
            Choice.objects.create(
                question=question_obj, text=choice_text, is_correct=is_correct
            )


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0001_initial"),  # Replace with your actual last migration name
    ]

    operations = [
        migrations.RunPython(create_initial_questions),
    ]
