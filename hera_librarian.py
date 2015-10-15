import hera_rpc

# RPC to create a file
#
def create_file(name, size, md5, store_name):
    config = get_config('.hera_librarian')
    req = {'operation': 'create_file',
        'authenticator': config['authenticator'],
        'name': name,
        'size': size,
        'md5': md5,
        'store_name': store_name}
    return do_http_post(req, config['server'])

#create_file('filename2', 2e9, 'ajfjfkdjffjf', 'UCB RAID')