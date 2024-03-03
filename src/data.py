import pandas as pd


def get_questions(id=None):
    questions = pd.read_csv("data/questions.csv", header=0, index_col=0)
    if id is None:
        return questions
    else:
        return questions.loc[id]


def add_question(question):
    try:
        questions = pd.read_csv("data/questions.csv", header=0, index_col=0)
    except:
        questions = pd.DataFrame(question, index=[0])
        questions.to_csv("data/questions.csv", index=True)
        return
    question = pd.DataFrame(question, index=[questions.index.max() + 1])
    questions = pd.concat([questions, question], axis=0, ignore_index=False)
    questions.to_csv("data/questions.csv")


def edit_question(id, question):
    questions = pd.read_csv("data/questions.csv", header=0, index_col=0)
    if id not in questions.index:
        raise ValueError("Nonexistent index")
    questions.loc[id] = question
    questions.to_csv("data/questions.csv")


def delete_question(id):
    questions = pd.read_csv("data/questions.csv", header=0, index_col=0)
    questions = questions.drop(index=id)
    questions.to_csv("data/questions.csv")


def add_user(user):
    try:
        users = pd.read_csv("data/users.csv", header=0, index_col=0)
    except:
        users = pd.DataFrame(user).set_index(["username", "password"])
        users.to_csv("data/users.csv", index=True)
        return
    user = pd.DataFrame(user).set_index(["username", "password"])
    users = pd.concat([users, user], axis=0, ignore_index=False)
    users.to_csv("data/users.csv")


def find_user(user):
    users = pd.read_csv("data/users.csv", header=0, index_col=0)

    # check to find if the user can be found in the dataframe
    if user not in users.index:
        return False
    return True


def delete_user(username):
    users = pd.read_csv("data/users.csv", header=0, index_col=0)
    users = users.drop(index=username)
    users.to_csv("data/users.csv")
