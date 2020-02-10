### About Pagination

'''

    [Pagination]
    
    [Available methods on the posts object (Pagination object)]
    
    Returns:
            - print(dir(posts)) - Sell all available methods on object
            - print('Has next?: ' + 'True' if posts.has_next else 'False')
            - print('Has prev?: ' + 'True' if posts.has_prev else 'False')
            - print('Next page: ' + str(posts.next_num))
            - print('Prev page?: ' + str(posts.prev_num))
            - print('Total Items ' + str(posts.total))
            - print(posts.items) - the real posts
            - print('Posts per page: ' + str(posts.per_page))
            - print('Current page: ' + str(posts.page))
'''