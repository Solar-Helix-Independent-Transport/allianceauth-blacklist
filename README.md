# allianceauth-blacklist

**You Shall Not Pass!**

## Installation

1. Install from pip `pip install allianceauth-blacklist`
2. Add `'blacklist'` to INSTALLED_APPS in local.py
3. Run the management command to update AA's State system `python myauth/manage.py blacklist_state`
4. Give permissions
5. done ski

## Features

- Integration with Alliance Auth's State System, creates an maintains a Blacklisted State to ensure no services access is granted to Blacklisted users
- Notes
- Comments on Notes

## Permissions

Category | Perm | Admin Site | Auth Site
--- | --- | --- | ---
Access |view_basic_eve_notes | Can View own corps notes | nill
Access |view_eve_blacklist | Can View the Blacklist | nill
Access |view_eve_notes | Can view all eve notes | nill
Notes | add_basic_eve_notes | Can Add own corp members to notes | nill
Notes | add_new_eve_notes | Can add new eve notes | nill
Notes | view_restricted_eve_notes | Can View restricted eve notes | nill
Notes | add_restricted_eve_notes | Can Add restricted eve notes | nill
Notes | add_to_blacklist | Can add/remove from the Blacklist | nill
Comments | view_eve_note_comments | Can view eve note comments | nill
Comments | view_eve_note_restricted_comments | Can view restricted eve note comments | nill
Comments | add_new_eve_note_comments | Can add comments on eve notes | nill
Comments | add_new_eve_note_restricted_comments | Can add new restricted comments to eve notes | nill

## Contributing

Make sure you have signed the [License Agreement](https://developers.eveonline.com/resource/license-agreement) by logging in at <https://developers.eveonline.com> before submitting any pull requests. All bug fixes or features must not include extra superfluous formatting changes.
