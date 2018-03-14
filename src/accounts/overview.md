# Accounts #

According to the [Accounts documentation](https://developer.engineyard.com/accounts), there are four basic uses for the endpoint:

* List all accounts (GET a collection of accounts visible to the current user)
* List all all accounts for a given user (GET a collection of accounts that are visible to the current user and associated with the given user)
* Show an account (GET a single account)
* Update an account's emergency contact (PUT new data for the account)

Two of these are problematic right off the top. For one, it appears that the docs don't actually tell us anything about the Users endpoint. Also, while the last use is described only in terms of updating the emergency contact, the parameter list for the use case implies that we can also update the account name.

Before we actually implement any of those, though, let's go ahead and define the Entity for this module ...
