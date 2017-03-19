THis directory contains files used for activating and deactivating users
in the L.O.S.T. database. Activating a user will create a new account if
the given username does not exist, otherwise will reactivate disabled
users. Revoking users will deactivate an account, preventing them from
logging into the L.O.S.T. application.

* activate_user.py
Usage: python3 activate_user.py <host_url> <username> <password> <role>
<host_url> - The host part of the URL (if running in Linux image, will be 'http://127.0.0.1:8080/').
<username> - The username of the account to activate.
<password> - The password to give the new account, or replaces the old one if already exists.
<role> - The role to assign to the user, will be 'logofc' or 'facofc'.
* revoke_user.py
Usage: python3 revoke_user.py <host_url> <username>
<host_url> - The host part of the URL (if running in Linux image, will be 'http://127.0.0.1:8080/').
<username> - The username of the account to deactivate.

...
|
|-- activate_user.py
|-- revoke_user.py
|
