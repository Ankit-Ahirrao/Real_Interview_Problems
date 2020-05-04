1. Balanced ArrayGiven an array of numbers, find the index of the smallest array element (the pivot), for which the sums of all elements to the left and to the right are equal. The array may not be reordered.Examplearr=[1,2,3,4,6]the sum of the first three elements, 1+2+3=6. The value of the last element is 6.Using zero based indexing, arr[3]=4 is the pivot between the two subarrays.The index of the pivot is 3.Function DescriptionComplete the function balancedSum in the editor below.balancedSum has the following parameter(s):int arr[n]: an array of integersReturns:int: an integer representing the index of the pivotConstraints3 ≤ n ≤ 1051 ≤ arr[i] ≤ 2 × 104, where 0 ≤ i < nIt is guaranteed that a solution always exists.

def balancedSum(sales):
    total = sum(sales)
    cur_total = 0
    for i, v in enumerate(sales):
        if i == 0: continue
        cur_total += sales[i-1]
        if cur_total == (total - v)/2: return i
    return -1


2. Most Active AuthorsIn this challenge, the REST API contains information about a collection of users and articles they created. Given the threshold value, the goal is to use the API to get the list of most active authors. Specifically, the list of usernames of users with submission count strictly greater than the given threshold. The list of usernames must be returned in the order the users appear in the results.To access the collection of users perform HTTP GET request to:https://jsonmock.hackerrank.com/api/article_users?page=<pageNumber>where <pageNumber> is an integer denoting the page of the results to return.For example, GET request to:https://jsonmock.hackerrank.com/api/article_users/search?page=2will return the second page of the collection of users. Pages are numbered from 1, so in order to access the first page, you need to ask for page number 1.The response to such request is a JSON with the following 5 fields:page: The current page of the resultsper_page: The maximum number of users returned per page.total: The total number of users on all pages of the result.total_pages: The total number of pages with results.data: An array of objects containing users returned on the requested pageEach user record has the following schema:id: unique ID of the userusername: the username of the userabout: the about information of the usersubmitted: total number of articles submitted by the userupdated_at: the date and time of the last update to this recordsubmission_count: the number of submitted articles that are approvedcomment_count: the total number of comments the user madecreated_at: the date and time when the record was createdFunction DescriptionComplete the function getUsernames in the editor below.getUsernames has the following parameter(s):threshold: integer denoting the threshold value for the number of submission countThe function must return an array of strings denoting the usernames of the users whose submission count is strictly greater than the given threshold. The usernames in the array must be ordered in the order they appear in the API response.

import requests

def get_data():
    has_next = True
    cur_page = 1
    url = "https://jsonmock.hackerrank.com/api/article_users"
    while has_next:
        r = requests.get(url, params={"page": cur_page}).json()
        has_next = True if int(r["page"]) < r["total_pages"] else False
        cur_page = cur_page if not has_next else cur_page + 1
        yield r["data"]


def getUsernames(threshold):
    ret = []
    for data in get_data():
        filter_by_count = filter(lambda x: x["submission_count"] > threshold, data)
        usernames = map(lambda x: x["username"], filter_by_count)
        ret.extend(usernames)
    return ret