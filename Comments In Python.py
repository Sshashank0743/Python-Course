#!/usr/bin/env python
# coding: utf-8

# ## Comments

# Almost all programming languages have dedicated syntax for comments. Comments are to be ignored by compilers or interpreters and hence they have no effect to the programming flow or logic. But with comments, we are easier to read the code.

# ## Unnecessary and distracting comment lines:

# In[1]:


import datetime
 
timestamp = datetime.datetime.now()  # Get the current date and time
x = 0    # initialize x to zero


# ## Good comments should be telling why we are doing something.

# In[2]:


def adadelta(objective, derivative, bounds, n_iter, rho, ep=1e-3):
    # generate an initial point
    solution = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # lists to hold the average square gradients for each variable and
    # average parameter updates
    sq_grad_avg = [0.0 for _ in range(bounds.shape[0])]
    sq_para_avg = [0.0 for _ in range(bounds.shape[0])]
    # run the gradient descent
    for it in range(n_iter):
        gradient = derivative(solution[0], solution[1])
        # update the moving average of the squared partial derivatives
        for i in range(gradient.shape[0]):
            sg = gradient[i]**2.0
            sq_grad_avg[i] = (sq_grad_avg[i] * rho) + (sg * (1.0-rho))
        # build a solution one variable at a time
        new_solution = list()
        for i in range(solution.shape[0]):
            # calculate the step size for this variable
            alpha = (ep + sqrt(sq_para_avg[i])) / (ep + sqrt(sq_grad_avg[i]))
            # calculate the change and update the moving average of the squared change
            change = alpha * gradient[i]
            sq_para_avg[i] = (sq_para_avg[i] * rho) + (change**2.0 * (1.0-rho))
            # calculate the new position in this variable and store as new solution
            value = solution[i] - change
            new_solution.append(value)
        # evaluate candidate point
        solution = asarray(new_solution)
        solution_eval = objective(solution[0], solution[1])
        # report progress
        print('>%d f(%s) = %.5f' % (it, solution, solution_eval))
    return [solution, solution_eval]


# The function above is implementing AdaDelta algorithm. 

# # Some common “best practice” on commenting code as listed as follows:

# - Comments should not restate the code, but to explain it
# - Comments should not cause confusion, but to eliminate it
# - Put comments on code that is not trivial to understand, for example, state the unidiomatic use of syntax, name the algorithm being used, or explain the intent or assumptions
# - Comments should be concise and simple
# - Keep a consistent style and use of language in commenting
# - Always prefer to have a better written code that needs no additional comment

# ## Multi-line comments

# In[3]:


async def main(indir):
    # Scan dirs for files and populate a list
    filepaths = []
    for path, dirs, files in os.walk(indir):
        for basename in files:
            filepath = os.path.join(path, basename)
            filepaths.append(filepath)
 
    """Create the "process pool" of 4 and run asyncio.
    The processes will execute the worker function
    concurrently with each file path as parameter
    """
    loop = asyncio.get_running_loop()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        futures = [loop.run_in_executor(executor, func, f) for f in filepaths]
        for fut in asyncio.as_completed(futures):
            try:
                filepath = await fut
                print(filepath)
            except Exception as exc:
                print("failed one job")


# Python supports to declare a string literal spanning across multiple lines if it is delimited with triple quotation marks (""").

# In[ ]:


from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
"""
X, y = make_classification(n_samples=5000, n_features=2, n_informative=2,
                           n_redundant=0, n_repeated=0, n_classes=2,
                           n_clusters_per_class=1,
                           weights=[0.01, 0.05, 0.94],
                           class_sep=0.8, random_state=0)
"""
import pickle
with open("dataset.pickle", "wb") as fp:
    X, y = pickle.load(fp)
 
clf = LogisticRegression(random_state=0).fit(X, y)


# The string literal in Python as comment has a special purpose if it is at the first line under a function. The string literal in that case is called the “docstring” of the function.

# In[5]:


def square(x):
    """Just to compute the square of a value
    
    Args:
        x (int or float): A numerical value
 
    Returns:
        int or float: The square of x
    """
    return x * x


# ### Use Union[int,float] to mean int type or float type, List[str] to mean a list that every element is a string, and use Any to mean anything.

# In[7]:


from typing import Any, Union,List

def square(x: Union[int, float]) -> Union[int, float]:
    return x * x

def append(x: List[Any], y: Any) -> None:
    x.append(y)


# In[ ]:




