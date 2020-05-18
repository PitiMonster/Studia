# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, normalize
import csv
from matplotlib import pyplot as plt
from scipy import sparse
import pandas as pd


# %%
# get data from movies.csv file
movies_csv = open('movies.csv', encoding='utf8')
movies_data = list(csv.reader(movies_csv, skipinitialspace=True))

# get data from ratings.csv file
ratings_csv = open('ratings.csv')
ratings_data = list(csv.reader(ratings_csv, delimiter=','))


movies_csv.close()
ratings_csv.close()


# %%
# Linear regression performed on the whole set
def whole_set(x, y):
    # training a model
    model = LinearRegression().fit(x, y)
    # testing a model
    y_pred = model.predict(x)

    # dividing length x into sections of one
    g = np.linspace(1, len(x), len(x))
    plt.scatter(g, (y-y_pred),s=2)
    plt.xlabel('Userzy, którzy ocenili Toy Story')
    plt.ylabel("Różnica pomiędzy poprawną, a przewidzianą oceną")
    plt.show()

# Linear regression performed on training and test set
def training_set(x, y):
    # training a model on partial data set
    model = LinearRegression().fit(x[:200], y[:200])
    # testing a model on whole data set 
    y_pred = model.predict(x)
    print("Poprawne oceny: ", y[-15:])
    print("Przewidywane oceny:", y_pred[-15:])

    g = np.linspace(200, 215, 15)
    plt.plot(g, y_pred[-15:], label="Predicted values")
    plt.scatter(g, y[-15:], label="Correct values")
    plt.xlabel("User id")
    plt.ylabel("Movie rating")
    plt.legend()
    plt.show()

# Prepare data for use in model training
def main():

    users_id = []
    m = 10000
    current_used_ratings = []

    # get all users id who rated Toy Story movie
    for row in ratings_data:
        if row[1] == '1':
            users_id.append(row[0])

    x = np.zeros((len(users_id), m))
    y = np.zeros((len(users_id), 1))

    # prepare matrixes with ratings
    for row in ratings_data[1:]:
        if int(row[1]) <= m+1 and row[0] in users_id:
            user_index = users_id.index(row[0])
            movie_id = int(row[1])
            if movie_id == 1:
                y[user_index][movie_id-1] = float(row[2])
            else:
                x[user_index][movie_id-2] = float(row[2])
        
    y = y.reshape((-1,1))

    whole_set(x, y)
    training_set(x, y)

if __name__ == "__main__":
    main()


# %%
def main():

    users_movies_ratings_matrix = np.zeros((611,9019))
    my_ratings = np.zeros((9019,1))

    my_ratings[2571] = 5
    my_ratings[32] = 4
    my_ratings[260] = 5
    my_ratings[1097] = 4
    my_ratings_norm = my_ratings/np.linalg.norm(my_ratings)

    # creating matrix with ratings
    for row in ratings_data[1:]:
        if int(row[1]) <= 9018:
            users_movies_ratings_matrix[int(row[0])][int(row[1])] = float(row[2])

    # calculation of a standardised matrix
    matrix_norm = np.nan_to_num(users_movies_ratings_matrix/np.linalg.norm(users_movies_ratings_matrix, axis=0))

    # computing cosine similarity with every user
    cos_similarity = np.dot(matrix_norm, my_ratings_norm)
    result = np.dot(matrix_norm.T, cos_similarity/np.linalg.norm(cos_similarity))

    x = np.sort(result, axis=0)
    x = np.flip(x, 0)
    for i in range(10):
        id = np.where(result == x[i])[0][0]
        movie_name = [x[1] for x in movies_data[1:] if int(x[0]) == int(id)][0]
        print((x[i][0], id, movie_name))



if __name__ == '__main__':
    main()


# %%
def main():

    df = pd.read_csv("ml-latest\\ratings.csv", delimiter=',',
                     usecols=['userId', 'movieId', 'rating'],
                     dtype={"userId": int, "movieId": int, "rating": float}, skipinitialspace=True)

    movies = pd.read_csv("ml-latest\\movies.csv",delimiter=',',
                         usecols=['movieId', 'title'], dtype={"movieId":int}, skipinitialspace=True)

    movies_id = list(movies['movieId'])

    # lists for data from csv file
    user_id = []
    movie_id = []
    ratings = []
    # numpt array for my ratings
    my_ratings = np.zeros((193887,1))
    # filling up my_ratings array
    my_ratings[2571] = 5
    my_ratings[32] = 4
    my_ratings[260] = 5
    my_ratings[1097] = 4
    # normalizing my_ratings array
    my_ratings_norm = my_ratings/np.linalg.norm(my_ratings)

    # creating coo_matrix from data from csv file
    coo_user_matrix = sparse.coo_matrix((df['rating'][1:],
                                         (df['userId'][1:], df['movieId'][1:])))

    # cast coo_matrix to csr_matrix
    csr_user_matrix = sparse.csr_matrix(coo_user_matrix)
    # normalize csr_matrix
    sparse_matrix_norm = sparse.csr_matrix(normalize(csr_user_matrix,  axis=0))
    # cast my_ratings numpy array to csr_matrix
    sparse_my_ratings = sparse.csr_matrix(my_ratings)
    sparse_my_ratings_norm = sparse.csr_matrix(normalize(sparse_my_ratings))

    # compute cosine similarity
    cos_similarity = sparse.csr_matrix(sparse_matrix_norm * sparse_my_ratings_norm)

    # normalize cos_similarity and cast it to csr_matrix
    cos_similarity_norm = sparse.csr_matrix(normalize(cos_similarity))
    # get probability of likelihood
    result = sparse.csr_matrix(sparse_matrix_norm.transpose() *cos_similarity_norm).toarray()

    # sorted array of probabilities of likelihood
    x = np.sort(result, axis=0)
    # reverse numpy array vertically
    x = np.flip(x, axis=0)
    printed_titles = []
    title = ''
    for i in range(10):
        k = 0
        # ids of each movie with the probability = x[i]
        ids = np.where(result == x[i])
        while title in printed_titles or title == '':
            id = ids[0][k]

            index = movies_id.index(id) 
            title = movies['title'][index]
            k += 1

        printed_titles.append(title)
        print((x[i][0], id, title))



if __name__ == '__main__':
    main()


# %%



