from flask import Flask, jsonify
import facebook
import urllib
from urllib.parse import urlparse
import subprocess
import warnings
import ast

app = Flask(__name__)

@app.route("/")
def access_token():
    # Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
    warnings.filterwarnings('ignore', category=DeprecationWarning)


    # Parameters of your app and the id of the profile you want to mess with.
    FACEBOOK_APP_ID     = '1084981295453162'
    FACEBOOK_APP_SECRET = '1f259c36c298a53e4a6600cada8960bc'
    # FACEBOOK_PROFILE_ID = 'XXXXXX'


    # Trying to get an access token. Very awkward.
    oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                    client_secret = FACEBOOK_APP_SECRET,
                    grant_type    = 'client_credentials')
    oauth_curl_cmd = ['curl',
                    'https://graph.facebook.com/oauth/access_token?' + urllib.parse.urlencode(oauth_args)]
    oauth_response = subprocess.Popen(oauth_curl_cmd,
                                    stdout = subprocess.PIPE,
                                    stderr = subprocess.PIPE).communicate()[0]

    doauth_response = oauth_response.decode("UTF-8")
    moauth_response = ast.literal_eval(doauth_response)

    # print(moauth_response["access_token"])

    mAccess_Token = "EAAPayOS0EZBoBACNbUx56FYShgZB5ppD5ktFVajZBXnzTL8ggdZB5nyZBFhrL58RC6bgieFvj1EgUVm1JGkZAAm9KAGhBc3MwPZCwE0WwVUkmcJoxyqN3BXYZBL1zKRQ9O5AClO1YJqAZBtmNJ1IPB5YFnMDUT4oKUQbh928Y69R86i9tPt4kbjAyHU2rF4f3NZAGLI8TORjqbIH7VkiS0NPJChqpfdw4YEtb4nbUVcC8r1m7ZAKbeKOntG9lrGX5pZAjhcZD"

    mGraph = facebook.GraphAPI(mAccess_Token)

    mID = mGraph.get_object("me")["id"]

    mPermission = mGraph.get_permissions(user_id=mID)

    mPublicProfile = mGraph.get_connections(id=mID, connection_name="friends")

    print(mPublicProfile)

    return "200"